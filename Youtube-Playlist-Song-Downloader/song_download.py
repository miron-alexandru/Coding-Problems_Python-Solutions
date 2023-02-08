import tkinter as tk
from pytube import YouTube
import os
from pytube import Playlist
import moviepy.editor as mp
import re


def Download_Video():
	yt = YouTube(str(link.get()))
	video = yt.streams.filter(only_audio=True).first()
	destionation = os.getcwd()
	out_file = video.download(output_path=destionation)
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)
	tk.Label(window, text = 'Your song is downloaded!', font = 'arial 15',fg="White",bg="#0000FF").place(x= 10 , y = 140)
	

window = tk.Tk()
window.geometry("600x200")
window.config(bg="#0000FF")
window.resizable(width=False,height=False)
window.title('YouTube video to Mp3 converter')
 
link = tk.StringVar()
 
tk.Label(window,text = '                   Youtube to MP3                    ', font ='arial 20 bold',fg="white",bg="blue").pack()
tk.Label(window,text = 'Paste your YouTube link here:', font = 'arial 19 bold',fg="Black",bg="#0000FF").place(x= 5 , y = 60)
 
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="white").place(x = 5, y = 100)
 
tk.Button(window,text = 'Download', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=250 ,y = 140)
 
window.mainloop()

