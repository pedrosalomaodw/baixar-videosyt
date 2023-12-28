import tkinter as tk
import threading 
import os 
from pytube import YouTube 

root = tk.Tk()

root.geometry('350x200')
root.maxsize(350,200)
root.minsize(350,200)
root.title('Video Download')

nomepasta = os.environ['USERNAME']


def capturar():
    link = links.get(1.0,tk.END+'')
    yt = YouTube(link)
    video = yt.streams.filter(type='mp4')
    video = yt.streams.get_highest_resolution()
    video.download(rf'C:\Users\{nomepasta}\Downloads')
    os.joinpath(rf'C:\Users\{nomepasta}\Downloads')

def baixar():
    t = threading.Thread(target=capturar)
    t.start()


texto1 = tk.Label(root, text='Link:')
texto1.place(x=10, y=10, )
links = tk.Text(root ,height=2,width=30)
links.pack()

downloads = tk.Button(root, height=2,width=30, text='Baixar', command=baixar)
downloads.place(x=70, y=100)

instagram = tk.Label(root, text='Instagram: pedrosalomao.dev')
instagram.place(x=100, y=175)

root.mainloop()