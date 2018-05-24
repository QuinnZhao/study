
__author__ = 'Quinn Zhao'

from tkinter import Tk, PhotoImage, Frame, Button, Label, Text, INSERT, END, Scrollbar, filedialog
from panedwindow import Horizontal_PanedWindow, Vertical_PanedWindow
from constants import *
from translation1 import Translator1
import chardet


class Application(Tk):

    def __init__(self, image_h=None, image_v=None):
        Tk.__init__(self)
        self._create_widgets()
        self.mainloop()

    def _create_widgets(self):
        self.title('翻译软件')
        self.tk.call('wm','iconphoto', self._w, PhotoImage(data=DATA_LOGO))
        main_frame = Frame(self, width=800, height=600, bg=MAIN_FRAME_BG)
        main_frame.pack(expand=1, fill='both') # 窗口随最大化或者拖动而自动变化
        Label(main_frame, text='\n翻  译  软  件\n', font=('黑体', 20, 'bold'), bg=LB_GB, fg=LB_FG).pack(pady=10)
        btn1  = Button(main_frame, text='--翻--译-->',
                       # command=self._translation,
                       width=20, font=('黑体', 12, ''))
        btn1.pack()
        btn1['command'] = self._translation

        panedwindow = Horizontal_PanedWindow(main_frame, sashpad=3, image=None)
        #panedwindow = Horizontal_PanedWindow(self, sashpad=3, image=None)

        panedwindow.pack(fill="both", expand=True)
        panes = []
        for color in PANE_COLORS:
            frame = Frame(panedwindow, width=400, height=300, bg=color)
            panedwindow.add(frame, stretch="always")
            panes.append(frame)
        self.left_text = Text(panes[0], width=40, font=('黑体', 16, ''))
        self.right_text = Text(panes[1], width = 40, font=('黑体', 16, ''))
        Label(main_frame, text= '请在左边的输入框内输入你需要翻译的内容，并点击<翻译>按钮，谢谢！\n' +
                        '也可以点击上传按钮加载文本文件并点击<翻译>按钮',
              font=('黑体', 16, 'bold'), bg=LB_GB, fg=LB_FG).pack()
        scrollbar_l = Scrollbar(panes[0], orient="vertical",command=self.left_text.yview)
        scrollbar_r = Scrollbar(panes[1], orient="vertical",command=self.right_text.yview)
        self.left_text['yscrollcommand'] = scrollbar_l.set
        self.right_text['yscrollcommand'] = scrollbar_r.set
        scrollbar_l.pack(side='right', fill='y')
        scrollbar_r.pack(side='right', fill='y')
        self.left_text.pack(expand=1, fill='both')
        self.right_text.pack(expand=1, fill='both')
        Button(panes[0], text='上传文件', font=('黑体', 12, ''), command=self._upload).pack(pady=5)
        Button(panes[1], text='下载&保存', font=('黑体', 12, ''), command=self._download).pack(side='left', padx= 40,pady=5)
        Button(panes[1], text='拷贝', font=('黑体', 12, ''), command=self._copy).pack(side='right', padx=30, pady=5)

    def _upload(self):
        file_name = filedialog.askopenfilename(filetypes=(('Text文件', '*.txt'),
                                                        #  ('HTML 文件', '*.html;*.htm'),
                                                         #('Word 文件', '*.doc;*.docx'),
                                                         ("All files", "*.*")
                                                         ))
        with open(file_name, 'rb') as f:
            contents_bytes = f.read()
            # print(type(contents_bytes))
            encoding = chardet.detect(contents_bytes)
            print(encoding)
            contents = contents_bytes.decode(encoding=encoding['encoding'])
            # print(len(contents))
            self.left_text.delete('1.0', END)
            self.left_text.insert(INSERT, contents)

    def _download(self):
        print('downloading')
        f_out = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        f_out.write(str(self.right_text.get('0.0', END)))
        f_out.close()

    def _copy(self):
        self.right_text.clipboard_clear()
        self.right_text.clipboard_append(str(self.right_text.get('0.0', END)))

    def _translation(self):
        result = []
        text = self.left_text.get('1.0', END)
        blocks = self._split_to_blocks()
        for block in blocks:
            # Translator1(self.left_text.get('1.0', END), result)
            Translator1(block, result)
            self.right_text.delete('1.0', END)
            if not result:
                return
            for item in result:
                self.right_text.insert(INSERT, item)

    def _split_to_blocks(self):
        contents = self.left_text.get('1.0', END)
        if len(contents) < 4800:
            return [contents]
        contents += '\n' * (4800 - len(contents) % 4800)
        blocks = [contents[i: i + 4800] for i in range(0, len(contents), 4800)]
        blocks[-1] = blocks[-1].strip()
        return blocks

if __name__ == "__main__":
    Application()
