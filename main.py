import tkinter as tk
import customtkinter
from pytube import YouTube
from threading import Thread

def startDownload():
    # Disable the download button to prevent multiple clicks
    download.configure(state=tk.DISABLED)

    # Start the download in a separate thread
    download_thread = Thread(target=downloadInBackground)
    download_thread.start()

def downloadInBackground():
    try:
        ytlink = link.get()
        yt = YouTube(ytlink, on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        download_folder = r'C:\Users\kachi\Documents\Devs\youtubepy'
        video_stream.download(download_folder)
        print(f'Download complete. Saved to: {download_folder}')

        # Update the UI in the main thread
        app.after(100, updateUI, yt.title, 'white', 'Downloaded')

    except Exception as e:
        # Update the UI in the main thread
        app.after(100, updateUI, 'Error', 'red', '')

    finally:
        # Re-enable the download button when the download is finished or an error occurs
        download.configure(state=tk.NORMAL)

def updateUI(label_text, text_color, finish_text):
    title.configure(text=label_text, text_color=text_color)
    finishLabel.configure(text=finish_text)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))

    # Update progress in the main thread
    app.after(100, updateProgressUI, per, float(percentage_of_completion) / 100)

def updateProgressUI(percentage, progress):
    pPerentage.configure(text=percentage + '%')
    progressBar.set(progress)

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

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPerentage = customtkinter.CTkLabel(app, text="0%")
pPerentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()
