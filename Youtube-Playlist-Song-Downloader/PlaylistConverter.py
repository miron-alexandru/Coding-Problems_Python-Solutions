import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os
from pytube import Playlist
import moviepy.editor as mp
import re
import threading

stop_event = threading.Event()

def Download_Video():
    global stop_event
    stop_event.clear()
    yt = str(link.get())
    purl = Playlist(yt)
    num_videos = len(purl.videos)
    for i, video in enumerate(purl.videos):
        if stop_event.is_set():
            break
        mp4_stream = video.streams.filter(file_extension='mp4').first()
        mp4_stream.download(download_directory)

        folder = download_directory
        for file in os.listdir(folder):
            if re.search('mp4', file):
                mp4_path = os.path.join(folder, file)
                mp3_path = os.path.splitext(mp4_path)[0] + '.mp3'
                clip = mp.AudioFileClip(mp4_path)
                clip.write_audiofile(mp3_path)
                os.remove(mp4_path)
        progress_bar["value"] = int((i + 1) / num_videos * 100)
        window.update()
        window.update_idletasks()
        
    tk.Label(window, text='Success!', font='arial 19', fg="Black", bg="#0000FF").place(x=10, y=25)

def stop_downloading():
    global stop_event
    stop_event.set()

def choose_download_directory():
    global download_directory
    download_directory = filedialog.askdirectory(initialdir = "/", title = "Select download directory")

download_directory = os.getcwd()

window = tk.Tk()
window.geometry("600x230")
window.config(bg="blue")
window.resizable(width=False,height=False)
window.title('YouTube playlist to Mp3 converter')
 
link = tk.StringVar()

tk.Label(window, text='Progress:', font='arial 15', fg="Black", bg="#0000FF").place(x=10, y=140)
tk.Label(window,text = '                   Youtube playlist to MP3                    ', font ='arial 20 bold',fg="white",bg="blue").pack()
tk.Label(window,text = 'Paste your YouTube playlist link here:', font = 'arial 19 bold',fg="Black",bg="#0000FF").place(x= 5 , y = 60)
 
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="white").place(x = 5, y = 100)

progress_bar = ttk.Progressbar(window, length=200, mode='determinate')
progress_bar.place(x=110, y=145)

tk.Button(window,text = 'Download location', font = 'arial 13 bold',fg="black",bg="#0000FF", padx = 2, command=choose_download_directory).place(x=10, y = 180)
tk.Button(window,text = 'Stop', font = 'arial 15 bold' ,fg="white",bg = 'red', padx = 2,command=stop_downloading).place(x=520 ,y = 140)
download_button = tk.Button(window,text = 'Start', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video)
download_button.place(x=360, y = 140)
download_button.config(command=lambda: threading.Thread(target=Download_Video, args=(), daemon=True).start())
window.mainloop()

