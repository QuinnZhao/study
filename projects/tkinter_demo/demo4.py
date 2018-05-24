import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Spinbox
from tkinter import scrolledtext
from tkinter import messagebox as mBox

class TooTips:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d'%(x,y))

        label = tk.Label(tw, text= self.text, justify=tk.LEFT,
                         bg='#ffffe0', relief=tk.SOLID,
                         borderwidth=1, font=('黑体', 8, 'normal'))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def createToolTip(widget, text):
    toolTip = TooTips(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Python 图形用户界面')
        self.wm_resizable(0, 0) # 不允许改变窗口大小
        self._create_widgets()
        self.mainloop()

    def _create_widgets(self):
        tab_control = ttk.Notebook(self)
        tab_control = ttk.Notebook(self)
        # tab1 = ttk.Frame(tab_control)
        tab1 = Tab1(tab_control)
        tab_control.add(tab1, text='第一页')
        # tab2 = ttk.Frame(tab_control)
        tab2 = Tab2(tab_control)
        tab_control.add(tab2, text='第二页')
        # tab3 = ttk.Frame(tab_control)
        tab3 = Tab3(tab_control)
        tab_control.add(tab3, text='第三页')
        tab_control.pack(expand=1, fill='both')
        menu_bar = MyMenu(self)
        self.configure(menu=menu_bar)

class Tab1(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self._create_widgets()

    def _create_widgets(self):
        lbf = ttk.LabelFrame(self, text='控件示范区1')
        lbf.grid(column=0, row=0, padx=8, pady=4)
        ttk.Label(lbf, text='输入文字:').grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        name_entered = ttk.Entry(lbf, width=12, textvariable=self.name)
        name_entered.grid(column=0, row=1, sticky='W')
        self.action = ttk.Button(lbf, text='点击我之后\n按钮失效', width=10, command=self._click_me)
        self.action.grid(column=2, row=1, rowspan=2, ipady=7)

        ttk.Label(lbf, text='请选择一本书：').grid(column=1, row=0, sticky='W')
        book = tk.StringVar()
        book_chosen = ttk.Combobox(lbf, width=12, textvariable=book)
        book_chosen['values'] = ['爱的教育', '情商密码', 'Python cook book', 'tkinter docs']
        book_chosen.grid(column=1, row=1)
        book_chosen.current(0)

        self.spb1 = Spinbox(lbf, from_=10, to=25, width=5, bd=8, command=self._spin1)
        self.spb1.grid(column=0, row=2)
        self.spb2 = Spinbox(lbf,
                        values=['Python 3', 'C++', 'Java', 'Go', 'Open CV'],
                        width=13, bd=3, command=self._spin2)
        self.spb2.grid(column=1, row=2, sticky='W')

        scrol_w, scrol_h = 10, 5
        self.scr = scrolledtext.ScrolledText(lbf, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        createToolTip(self.spb1, '这是一个Spinbox')
        createToolTip(self.spb2, '这是一个Spinbox')
        createToolTip(self.action, '这是一个Button')
        createToolTip(name_entered, '这是一个Entry')
        createToolTip(book_chosen, '这是一个Combbox')
        createToolTip(self.scr, '这是一个ScrolledText')

        # 一次性控制各控件之间的距离
        for child in lbf.winfo_children():
            child.grid_configure(padx=3, pady=1)
        # 独立设置Button的距离
        self.action.grid(column=2, row=1, rowspan=2, padx=6)


    def _click_me(self):
        self.action.configure(text='你好！ \n' + self.name.get())
        self.action.configure(state='disabled')

    def _spin1(self):
        value = self.spb1.get()
        self.scr.insert(tk.INSERT, value + '\n')

    def _spin2(self):
        value = self.spb2.get()
        self.scr.insert(tk.INSERT, value + '\n')

class Tab2(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self._create_widgets()

    def _create_widgets(self):
        self.lbf = lbf = ttk.LabelFrame(self, text='控件示范区2')
        lbf.grid(column=0, row=0, padx=8, pady=4)
        ch_var_dis = tk.IntVar()
        check1 = tk.Checkbutton(lbf, text='失效选项', variable=ch_var_dis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        self.ch_var_un = tk.IntVar()
        self.check2 = tk.Checkbutton(lbf, text='遵从内心', variable=self.ch_var_un)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W)

        self.ch_var_en = tk.IntVar()
        self.check3 = tk.Checkbutton(lbf, text='屈于现实', variable=self.ch_var_en)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)

        self.ch_var_un.trace('w', lambda unused0, unused1, unused2: self._check_callback())
        self.ch_var_en.trace('w', lambda unused0, unused1, unused2: self._check_callback())

        self.values = values = ['富强民主', '文明和谐', '自由平等', '公正法治',
                  '爱国敬业', '诚信友善'
                  ]
        self.rad_var = tk.IntVar()
        self.rad_var.set(99)
        for col in range(4):
            cur_rad = tk.Radiobutton(lbf, text=values[col], variable=self.rad_var, value=col, command=self._rad_call)
            cur_rad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
        for col in range(4,6):
            cur_rad = tk.Radiobutton(lbf, text=values[col], variable=self.rad_var, value=col, command=self._rad_call)
            cur_rad.grid(column=col-4, row=7, sticky=tk.W, columnspan=3)

        style = ttk.Style()
        style.configure('BW.TLabel', font=('黑体', '10', 'bold'))
        ttk.Label(lbf, text='社会主义核心价值观', style='BW.TLabel').grid(column=2, row=7,
                                                                 columnspan=2, sticky=tk.W)

        lbf1 = ttk.LabelFrame(lbf, text='嵌套区域')
        lbf1.grid(column=0, row=8, columnspan=4)
        ttk.Label(lbf1, text='你还年轻，你可以成为任何想成为的人！').grid(column=0, row=0)
        ttk.Label(lbf1, text='不要在乎一城一池的得失，要执着！').grid(column=0, row=1, sticky=tk.W)

        for child in lbf1.winfo_children():
            child.grid_configure(padx=8, pady=4)


    def _rad_call(self):
        self.lbf.configure(text=self.values[self.rad_var.get()])

    def _check_callback(self, *ignored_args):
        if self.ch_var_un.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.ch_var_en.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

class Tab3(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='#AFEEEE')
        self._create_widgets()

    def _create_widgets(self):
        for i in range(2):
            canvas = 'canvas' + str(i)
            canvas = tk.Canvas(self, width=162, height=95, highlightthickness=0, bg='#FFFF00')
            canvas.grid_configure(row=i, column=i)

class MyMenu(Menu):

    def __init__(self, master=None):
        Menu.__init__(self, master)
        self._create_menus()

    def _create_menus(self):
        file_menu= Menu(self, tearoff=0)
        file_menu.add_command(label='新建')
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=self._quit)
        self.add_cascade(label='文件', menu=file_menu)

        msg_menu = Menu(self, tearoff=0)
        msg_menu.add_command(label='通知', command=self._msg_notify)
        msg_menu.add_command(label='警告', command=self._msg_warn)
        msg_menu.add_command(label='错误', command=self._msg_error)
        msg_menu.add_separator()
        msg_menu.add_command(label='判断', command=self._msg_judge)
        self.add_cascade(label='消息框', menu=msg_menu)

    def _msg_notify(self):
        mBox.showinfo('Python Message Info Box', '通知：一切正常')

    def _msg_warn(self):
        mBox.showwarning('Python Message Warning Box', '警告：出现错误，请检查')

    def _msg_error(self):
        mBox.showerror('Python Message Error Box', '错误：严重错误，请退出')

    def _msg_judge(self):
        answer = mBox.askyesno('Python Message Dual Choice Box', '你喜欢？ \n你的选择是：')
        if answer:
            mBox.showinfo('Python Message Info Box', '你的选择是Yes，谢谢参与')
        else:
            mBox.showinfo('Python Message Info Box', '你的选择是No，谢谢参与')

    def _quit(self):
        self.master.quit()
        self.master.destroy()
        exit()


if __name__ == '__main__':
    Application()


