import socket
import threading
from tkinter import *
import get_ernie_vilg_pic


class SubThread(threading.Thread):
    def run(self):
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.bind(('127.0.0.1', 774))

        while True:
            s1.listen(10)
            sock, addr = s1.accept()
            info = sock.recv(1024).decode()
            global thelist
            thelist.insert(END, 'ta:' + info)


def send():
    s2 = socket.socket()
    s2.connect(('127.0.0.1', 775))
    global v
    keyword = v.get()
    result = ""
    try:
        result = get_ernie_vilg_pic.get_create_pic_url(keyword)
    except:
        print("存在敏感词或额度不够")
    if result:
        s2.send(result.encode())
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
    thelist.insert(END, 'player4')
    theentry = Entry(root, textvariable=v)
    theentry.grid(row=11, column=1, columnspan=4)
    p1 = SubThread()
    p1.start()
    mainloop()