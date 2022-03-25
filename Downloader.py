from tkinter import *
from turtle import width
from pytube import YouTube
from tkinter import filedialog


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("500x500+550+200")
root.resizable(width=False, height=False)
root.iconbitmap("logo.ico")
backgroundColor = Label(bg="#A9A9A9", width=500, height=500)
backgroundColor.place(x=0, y=0)

def dosyaKonumu():
    root.filename = filedialog.askdirectory(initialdir="/", title="Klasör Seçin")


def YoutubeUrlal():
    youtubeurl = entry1.get() 
    yt = YouTube(youtubeurl)
    dl = yt.streams.get_highest_resolution()
    dl.download(root.filename)
    sonLabel = Label(text="İndirme tamamlandı...", font="bold")
    sonLabel.pack()

label1 = Label(text="Youtube Url", bg="#A9A9A9")
label1.place(x=25, y=25)

entry1 = Entry(width=50)
entry1.place(x=25, y=50)

konumSec = Button(text="Dizin Seçin", command=dosyaKonumu)
konumSec.place(x=25, y=75)

yükle = Button(text="Yükle", command=YoutubeUrlal)
yükle.place(x=25, y=110)

root.mainloop()
