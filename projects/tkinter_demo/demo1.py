
__author__ = 'Quinn Zhao'

from tkinter import Tk, PhotoImage, Frame, Button, Label
from panedwindow import Horizontal_PanedWindow, Vertical_PanedWindow
from constants import *


class Application(Tk):

    def __init__(self, image_h=None, image_v=None):
        Tk.__init__(self)
        self._create_widgets()
        self.mainloop()

    def _create_widgets(self):
        self.title('tkinter GUI 编程练习--PanedWindow')
        image_logo = PhotoImage(data=DATA_LOGO)
        self.tk.call('wm', 'iconphoto', self._w, image_logo)

        panedwindow = Horizontal_PanedWindow(self, sashpad=3, image=None)
        panedwindow.pack(fill="both", expand=True)
        image_sash = PhotoImage(data=DATA_SASH)
        for color in ('', "gray", "green"):
            if color:
                frame = Frame(panedwindow, width=200, height=200, bg=color)
                panedwindow.add(frame, stretch="always")
            else:
                panewindow1 = Vertical_PanedWindow(panedwindow, sashpad=3, image=image_sash)
                panedwindow.add(panewindow1)
                for c in ('red', 'blue'):
                    frame = Frame(panewindow1, width=200, height=200, bg=c)
                    panewindow1.add(frame, stretch='always')


if __name__ == "__main__":
    Application()
