import os
import re
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import AudioFileClip


class YouTubeConverterGUI:
    """GUI application for downloading YouTube videos and playlists in MP3 format."""
    def __init__(self):
        self.download_directory = os.getcwd()
        self.stop_event = threading.Event()
        self.window = tk.Tk()
        self.window.geometry("600x230")
        self.window.config(bg="#0D47A1")
        self.window.resizable(width=False, height=False)
        self.window.title('YouTube Converter')
        self.link = tk.StringVar()
        self.progress_bar = ttk.Progressbar(self.window, length=200, mode='determinate')
        self.link_enter = None
        self.download_location_button = None
        self.stop_button = None
        self.download_button = None

    def run(self):
        """Start the GUI aplication."""
        self._create_ui()
        self.window.mainloop()

    def _create_ui(self):
        """Create the user interface"""
        tk.Label(self.window, text='Progress:', font='Arial 15 bold',
                 fg="white", bg="#0D47A1").place(x=10, y=140)
        tk.Label(self.window, text='YouTube Converter', font='Arial 25 bold',
                 fg="white", bg="#0D47A1").pack(pady=10)
        tk.Label(self.window, text='Paste YouTube link here:', font='Arial 15 bold',
                 fg="white", bg="#0D47A1").place(x=5, y=60)
        self.link_enter = tk.Entry(self.window, width=53, textvariable=self.link,
                                    font='Arial 15 bold', bg="white")
        self.link_enter.place(x=5, y=100)
        self.progress_bar.place(x=110, y=145)
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 13), foreground='black',
                         background='#1565C0', padding=2, borderwidth=0)
        self.download_location_button = ttk.Button(self.window, text='Download Location',
                                                    style='TButton',
                                                    command=self._choose_download_directory)
        self.download_location_button.place(x=10, y=180)
        self.stop_button = ttk.Button(self.window, text='Stop', style='TButton',
                                       command=self._stop_downloading)
        self.stop_button.place(x=480, y=140)
        self.download_button = ttk.Button(self.window, text='Start', style='TButton',
                                           command=self._download_video)
        self.download_button.place(x=340, y=140)
        self.download_button.config(
            command=lambda: threading.Thread(
                target=self._download_video,
                args=(), daemon=True).start()
            )

    def _download_video(self):
        self.stop_event.clear()
        yt_link = str(self.link.get())
        is_playlist = False
        # Check if the link is a playlist or a single video link
        video_id_match = re.match(
            r"https?://(?:www\.|)youtu(?:be\.com|\.be)/(?:watch\?.*?v=|)([^\s&]+)", 
            yt_link
        )
        playlist_id_match = re.match(
            r"https?://(?:www\.|)youtube\.com/(?:watch\?.*?&|)list=([^\s&]+)|"
            r"https?://youtu\.be/[^\s?]+(?:\?|&)list=([^\s&]+)|"
            r"https?://(?:www\.|)youtube\.com/playlist\?list=([^\s&]+)", 
            yt_link
        )


        if playlist_id_match:
            purl = Playlist(yt_link)
            num_videos = len(purl.video_urls)
            is_playlist = True
        elif video_id_match:
            num_videos = 1
        else:
            # Handle the case where an invalid link is entered
            messagebox.showerror("Error", "Invalid link")
            return

        # Download the video or the playlist
        for i in range(num_videos):
            if self.stop_event.is_set():
                break
            if is_playlist:
                video_url = purl.video_urls[i]
                video = YouTube(video_url)
            else:
                video_id = video_id_match.group(1)
                video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            try:
                audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
                if audio_stream:
                    file_name = re.sub('[^A-Za-z0-9 ]+', '', video.title) + ".mp4"
                    video_file_path = audio_stream.download(output_path=self.download_directory,
                                                             filename=file_name)
                    audio_file_path = os.path.splitext(video_file_path)[0] + ".mp3"
                    with AudioFileClip(video_file_path) as video_clip:
                        video_clip.write_audiofile(audio_file_path)
                    os.remove(video_file_path)
            except Exception as all_ex:
                messagebox.showerror("Error", f"Failed to download: {video.title}\nError: {all_ex}")
                continue

            self.progress_bar["value"] = int((i + 1) / num_videos * 100)
            self.window.update()
            self.window.update_idletasks()

        self.progress_bar["value"] = 0
        success_label = tk.Label(self.window, text='', font='arial 19', fg="white",
                                  bg="#0D47A1", highlightthickness=0)
        success_label.place(x=10, y=25)
        success_label.config(text='Success!')
        success_label.after(5000, success_label.config, {'text': ''})



    def _choose_download_directory(self):
        """Choose the download directory"""
        self.download_directory = filedialog.askdirectory(initialdir = "/",
                                                          title = "Select download directory")

    def _stop_downloading(self):
        self.stop_event.set()


if __name__ == '__main__':
    gui = YouTubeConverterGUI()
    gui.run()