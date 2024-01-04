import tkinter as tk
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get() 
        yt = YouTube(ytlink)  
        video_stream = yt.streams.get_highest_resolution()
        download_folder = 'C:\Users\kachi\Documents\Devs\youtubepy'
        video_stream.download(download_folder)
        print(f'Download complete. Saved to: {download_folder}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Downloader')

title = customtkinter.CTkLabel(app, text='Insert a Youtube Link', font=('Arial', 20))
title.pack(padx=10, pady=10)

video_url = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=video_url)
link.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack()

app.mainloop()
import tkinter as tk
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()  
        yt = YouTube(ytlink)  
        video_stream = yt.streams.get_highest_resolution()
        download_folder = '../downloads'
        video_stream.download(download_folder)
        print(f'Download complete. Saved to: {download_folder}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Downloader')

title = customtkinter.CTkLabel(app, text='Insert a Youtube Link', font=('Arial', 20))
title.pack(padx=10, pady=10)

video_url = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=video_url)
link.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack()

app.mainloop()
