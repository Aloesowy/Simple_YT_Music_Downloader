import tkinter
import customtkinter
from pytube import YouTube
from tkinter import messagebox

#Funcion to get link from user input
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        music = ytObject.streams.get_audio_only()
        music.download()
        messagebox.showinfo("YouTubeDownloader", "Download Complete")
    except:
        messagebox.showinfo("YouTubeDownloader", "That link is invalid")

#Main Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#Application window
app = customtkinter.CTk()
app.geometry("800x425")
app.title("YouTube Music Downloader")

#UI
title = customtkinter.CTkLabel(app, text='Insert link here to YT video you want to download as mp3')
title.pack(padx=10,pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack()

#Download button 
button = tkinter.Button(app, text="Download", command=startDownload)
button.pack()

#App loop
app.mainloop()

