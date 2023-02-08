import tkinter as tk
from pytube import YouTube
import os
from pytube import Playlist
import moviepy.editor as mp
import re


def Download_Video():
	yt = str(link.get())
	purl = Playlist(yt)
	for video in purl.videos:
		st = video.streams.get_highest_resolution()
		st.download()
		#video.streams.first.download()

	folder = os.getcwd()
	for file in os.listdir(folder):
		if re.search('mp4', file):
			mp4_path = os.path.join(folder,file)
			mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
			new_file = mp.AudioFileClip(mp4_path)
			new_file.write_audiofile(mp3_path)
			os.remove(mp4_path)
	tk.Label(window, text = 'Your playlist is downloaded!', font = 'arial 15',fg="White",bg="#0000FF").place(x= 10 , y = 140)
			
window = tk.Tk()
window.geometry("600x200")
window.config(bg="#0000FF")
window.resizable(width=False,height=False)
window.title('YouTube playlist to Mp3 converter')
 
link = tk.StringVar()
 
tk.Label(window,text = '                   Youtube playlist to MP3                    ', font ='arial 20 bold',fg="white",bg="blue").pack()
tk.Label(window,text = 'Paste your YouTube playlist link here:', font = 'arial 19 bold',fg="Black",bg="#0000FF").place(x= 5 , y = 60)
 
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="white").place(x = 5, y = 100)
 
tk.Button(window,text = 'Download', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=250 ,y = 140)

window.mainloop()