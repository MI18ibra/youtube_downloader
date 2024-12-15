from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL


def hight_quality():
    try:
        url = entry.get()

        ydl_opts = {

            'fromat': 'best',
            'outtmpl': 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

            messagebox.showwarning("","the vedio has been downloaded")

    except Exception as e:
        messagebox.showwarning("","Error downloading")



def low_quality():
    try:
        url = entry.get()

        ydl_opts = {

            'fromat': 'worst',
            'outtmpl': 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

            messagebox.showwarning("","the vedio has been downloaded")

    except Exception as e:
        messagebox.showwarning("","Error downloading")



def get_audio():
    try:
        url = entry.get()

        ydl_opts = {

            'fromat': 'bestaudio',
            'outtmpl': 'downloads%(titles)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

            messagebox.showwarning("","the vedio has been downloaded")

    except Exception as e:
        messagebox.showwarning("","Error downloading")



window = Tk()
window.title ("GET VIDEO OR AUDIO APPLICATION")
window.geometry("600x350")
window.configure(bg = "#333333")


label = Label(window, text = "PLEASE PUT YOUR YOUTUBE LINK HERE👇", font = "bold" , bg = window['bg'], fg="white")
label.place(x= 110, y = 30)

entry =  Entry(window, width = 60, justify="center")
entry.place(x= 130, y = 100)

label = Label(window, text = "CHOSE WHAT YOU WANT FROM THIS LINK", font = "bold" , bg = window['bg'],fg="white")
label.place(x= 100, y = 170)

hight = Button(window, text= "Vedio Hight Quality" , command= hight_quality , font = "bold" , activeforeground= "green")
hight.place(x= 40, y = 230)

low = Button(window, text= "Video Low Quality" , command= low_quality, font = "bold" , activeforeground= "red")
low.place(x=233, y = 230)

audio = Button(window, text= "Get The Audio" , command= get_audio, font = "bold" , activeforeground= "blue")
audio.place(x= 420, y = 230)

window.mainloop()