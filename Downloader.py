from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk

import shutil



screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#functions for the features
def selectPath():
    path = filedialog.askdirectory() #allows user to select a path from the computer
    path_l.config(text=path)

def downloadFile():
    #getting user path
    get_l = link_f.get()
    user_p = path_l.cget("text")
    screen.title('Downloading please wait!')

    #downloading
    dv = YouTube(get_l).streams.get_highest_resolution().download()
    vid = VideoFileClip(dv)
    vid.close()

    #move to selected directory
    shutil.move(dv, user_p)
    messagebox.showinfo(title='Information', message='Download completed')

#image  
#logo_img = ImageTk.PhotoImage(height = 100, width=100, Image.open('yt.png'))
#canvas.create_image(50, 80, image=logo_img)

#adding the link
link_f = Entry(screen, width=50)
link_l = Label(screen, text="Enter the download link")

#adding it to canvas
canvas.create_window(250, 170, window=link_l)
canvas.create_window(250, 200, window=link_f)

#select path feature
path_l = Label(screen, text="Select path to store download")
path_b = Button(screen , text ="Browse", command=selectPath)

#adding path feature to canvas
canvas.create_window(250, 230, window=path_l)
canvas.create_window(250, 260, window=path_b)

#adding the buttons

download_b = Button(screen , text ="Download File", command=downloadFile)

#adding buttons to the screen
canvas.create_window(250, 295, window=download_b)

screen.mainloop()