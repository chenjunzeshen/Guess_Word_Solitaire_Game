import socket
import threading
from tkinter import *


class SubThread(threading.Thread):
    def run(self):
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.bind(('127.0.0.1', 771))

        while True:
            s1.listen(10)
            sock, addr = s1.accept()
            info = sock.recv(1024).decode()
            global thelist
            thelist.insert(END, 'ta:' + info)


def send():
    s2 = socket.socket()
    s2.connect(('127.0.0.1', 772))
    global v
    s2.send(v.get().encode())
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
    thelist.insert(END, 'player1')
    theentry = Entry(root, textvariable=v)
    theentry.grid(row=11, column=1, columnspan=4)
    p1 = SubThread()
    p1.start()
    mainloop()