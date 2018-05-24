from tkinter import ttk
import tkinter as tk
from sptrader import SpTrader
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class ProductChart(ttk.Frame):

    def __init__(self, master=None, name=''):
        ttk.Frame.__init__(self, master)
        self.name = name
        self._create_widgets()
        self.draw()

    def _create_widgets(self):
        f1 = ttk.Frame(self)
        f1.grid(column=0, row=0, padx=4, pady=4, sticky='E')
        self.fig = Figure(figsize=(15, 6), dpi=100)
        self.ax1 = self.fig.add_subplot(411)
        self.ax2 = self.fig.add_subplot(412, sharex=self.ax1)
        self.ax3 = self.fig.add_subplot(413, sharex=self.ax1)
        self.ax4 = self.fig.add_subplot(414, sharex=self.ax1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=f1)
        self.hbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hbar.grid(column=0, row=1, sticky=tk.EW)
        # self.vbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        # self.vbar.grid(column=1, row=0, sticky=tk.NS)
        self.canvas.get_tk_widget().configure(xscrollcommand=self.hbar.set)
        # self.canvas.get_tk_widget().configure(yscrollcommand=self.vbar.set)
        self.hbar.configure(command=self.canvas.get_tk_widget().xview)
        # self.vbar.configure(command=self.canvas.get_tk_widget().yview)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=tk.NSEW)
        # self.draw()

        self._create_k_frame()
        self._create_macd_frame()
        self._create_kdj_frame()

    def _create_k_frame(self):
        pass

    def _create_macd_frame(self):
        pass

    def _create_kdj_frame(self):
        pass


    def draw(self):
        import numpy as np
        x = np.random.randint(0, 50, size=100)
        y = np.random.randint(0, 50, size=100)

        self.ax1.clear()
        self.ax1.scatter(x, y, s=3)
        self.ax1.set_title('Candle Figure')
        self.ax1.xaxis.set_visible(False)

        self.ax2.clear()
        self.ax2.scatter(x, y, s=4)
        self.ax2.set_title('Volume')
        self.ax2.xaxis.set_visible(False)


        self.ax3.clear()
        self.ax3.scatter(x, y, s=5)
        self.ax3.set_title('KDJ')
        self.ax3.xaxis.set_visible(False)


        self.ax4.clear()
        self.ax4.scatter(x, y, s=6)
        self.ax4.set_title('MACD')

        self.canvas.show()
        self.after(1000, self.draw)


if __name__ == '__main__':
    pass


