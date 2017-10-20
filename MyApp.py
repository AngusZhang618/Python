# -*- coding: utf-8 -*-
import tkinter as Tk


class MyApp(object):
    """ 假装此处有文档说明"""

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        btn = Tk.Button(self.frame, text="Open frame", command=self.openFrame)
        btn.pack()

    def hide(self):
        """"""
        self.root.withdraw()

    def openFrame(self):
        """"""
        self.hide()
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("800x600")
        otherFrame.title("other Frame")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = Tk.Button(otherFrame, text="Close", command=handler)
        btn.pack()

    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    def show(self):
        """"""
        # self.root.update()
        self.root.deiconify()


if __name__ == '__main__':
    root = Tk.Tk()
    root.geometry("400x300")
    app = MyApp(root)
    root.mainloop()
