
__author__ = 'Quinn Zhao'

from tkinter import Tk, PhotoImage, Frame, Button, Label, Text, INSERT, END, Scrollbar, filedialog
from panedwindow import Horizontal_PanedWindow, Vertical_PanedWindow
from constants import WORDS_NUM_LIMIT_1
from translation import TranslatorNew
import chardet
# from time import sleep
from application_ui import ApplicationUI


class Application(ApplicationUI):

    def _translation(self):
        result = []
        text = self.left_text.get('1.0', END)
        blocks = self._split_to_blocks
        for block in blocks:
            TranslatorNew(block, result)
            self.right_text.delete('1.0', END)
            if not result:
                return
            for item in result:
                self.right_text.insert(INSERT, item)

    @property
    def _split_to_blocks(self):
        contents = self.left_text.get('1.0', END)
        if len(contents) < WORDS_NUM_LIMIT_1:
            return [contents]
        contents += '\n' * (WORDS_NUM_LIMIT_1 - len(contents) % WORDS_NUM_LIMIT_1)
        blocks = [contents[i: i + WORDS_NUM_LIMIT_1] for i in range(0, len(contents), WORDS_NUM_LIMIT_1)]
        blocks[-1] = blocks[-1].strip()
        return blocks


if __name__ == "__main__":
    Application()
