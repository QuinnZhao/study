import matplotlib

matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk


class Application(tk.Tk):
    '''
    文件夹选择程序
        界面与逻辑分离
    '''

    def __init__(self):
        '''初始化'''
        super().__init__()  # 有点相当于tk.Tk()
        self.wm_title("Embed matplotlib in tkinter")

        self.createWidgets()

    def createWidgets(self):
        '''界面'''
        fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        footframe = tk.Frame(master=self).pack(side=tk.BOTTOM)

        tk.Button(master=footframe, text='重画', command=self.draw).pack(side=tk.BOTTOM)
        tk.Button(master=footframe, text='退出', command=self._quit).pack(side=tk.BOTTOM)

        self.draw()  # 绘图

    def draw(self):
        '''绘图逻辑'''
        x = np.random.randint(0, 50, size=100)
        y = np.random.randint(0, 50, size=100)

        # self.fig.clf()                  # 方式一：①清除整个Figure区域
        # self.ax = self.fig.add_subplot(111)    # ②重新分配Axes区域
        self.ax.clear()  # 方式二：①清除原来的Axes区域

        self.ax.scatter(x, y, s=3)  # 重新画

        self.canvas.show()

    def _quit(self):
        '''退出'''
        self.quit()  # 停止 mainloop
        self.destroy()  # 销毁所有部件


if __name__ == '__main__':
    # 实例化Application
    app = Application()

    # 主消息循环:
    app.mainloop()