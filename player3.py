import socket
import threading
from tkinter import *
import cv2
import time
from PIL import Image
import urllib.request
import numpy as np


class SubThread(threading.Thread):
    def run(self):
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.bind(('127.0.0.1', 773))

        while True:
            s1.listen(10)
            sock, addr = s1.accept()
            info = sock.recv(1024).decode()
            global thelist
            thelist.insert(END, 'ta:' + info)
            try:
                resp = urllib.request.urlopen(info)
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)
                image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                image.show()
            except:
                print("获取、打开图像失败，请自行在浏览器打开网址查看图像")


def send():
    s2 = socket.socket()
    s2.connect(('127.0.0.1', 774))
    global v
    s2.send(v.get().encode())
    cv2.destroyAllWindows()
    global thelist
    thelist.insert(END, 'me:' + v.get())
    v.set('')


if __name__ == '__main__':
    root = Tk()
    v = StringVar()
    thebutton = Button(root, text="send", command=send)
    thebutton.grid(row=11, column=5)
    thelist = Listbox(root)
    thelist.grid(row=0, column=1, rowspan=10, columnspan=5)
    thelist.insert(END, 'player3')
    theentry = Entry(root, textvariable=v)
    theentry.grid(row=11, column=1, columnspan=4)
    p1 = SubThread()
    p1.start()
    mainloop()