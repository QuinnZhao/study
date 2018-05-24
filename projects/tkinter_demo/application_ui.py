
__author__ = 'Quinn Zhao'

from tkinter import Tk, PhotoImage, Frame, Button, Label, Text, INSERT, END, Scrollbar, filedialog
from panedwindow import Horizontal_PanedWindow
from constants import DATA_LOGO,MAIN_FRAME_BG, LB_FG, LB_GB, PANE_COLORS
import chardet


class ApplicationUI(Tk):
    # 翻译器UI类定义
    # 定义基本的界面和简单逻辑，与具体的翻译操作无关

    def __init__(self, image_h=None, image_v=None):
        Tk.__init__(self)
        self._create_widgets()
        self.mainloop()

    def _create_widgets(self):
        self.title('自动翻译器++')
        self.tk.call('wm','iconphoto', self._w, PhotoImage(data=DATA_LOGO))
        main_frame = Frame(self, width=800, height=600, bg=MAIN_FRAME_BG)
        main_frame.pack(expand=1, fill='both') # 窗口随最大化或者拖动而自动变化
        Label(main_frame, text='\n自动检测语言， 快速翻译\n', font=('黑体', 20, 'bold'), bg=LB_GB, fg=LB_FG).pack(pady=10)
        btn1  = Button(main_frame, text='--翻--译-->',
                       # command=self._translation,
                       width=20, font=('黑体', 12, ''))
        btn1.pack()
        btn1['command'] = self._translation

        panedwindow = Horizontal_PanedWindow(main_frame, sashpad=3, image=None)

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
        Button(panes[0], text='上传文件', font=('黑体', 12, ''),
               command=self._upload).pack(side='left', padx=40, pady=5)
        Button(panes[0], text='清空输入', font=('黑体', 12, ''),
               command=self._clear).pack(side='right', padx=30, pady=5)
        Button(panes[1], text='下载&保存', font=('黑体', 12, ''),
               command=self._download).pack(side='left', padx= 40,pady=5)
        Button(panes[1], text='拷贝', font=('黑体', 12, ''),
               command=self._copy).pack(side='right', padx=30, pady=5)

    def _clear(self):  # 清空输入框
        self.left_text.delete('0.0', END)

    def _upload(self):  # 上传文件并显示在输入框中
        file_name = filedialog.askopenfilename(filetypes=(('Text文件', '*.txt'),
                                                        #  ('HTML 文件', '*.html;*.htm'),
                                                         #('Word 文件', '*.doc;*.docx'),
                                                         ("All files", "*.*")
                                                         ))
        with open(file_name, 'rb') as f:
            contents_bytes = f.read()
            encoding = chardet.detect(contents_bytes)
            contents = contents_bytes.decode(encoding=encoding['encoding'])
            self.left_text.delete('1.0', END)
            self.left_text.insert(INSERT, contents)

    def _download(self):  # 下载并保存输出框的内容
        f_out = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f_out:
            f_out.write(str(self.right_text.get('0.0', END)))
            f_out.close()

    def _copy(self):  # 拷贝输出框内容
        self.right_text.clipboard_clear()
        self.right_text.clipboard_append(str(self.right_text.get('0.0', END)))

    def _translation(self): # 翻译方法，需要在子类中进行重载重定义
        print('请添加合适的业务逻辑！')


if __name__ == "__main__":
    ApplicationUI()
