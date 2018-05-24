from tkinter import Tk, Frame, Canvas, Scrollbar, HORIZONTAL, VERTICAL, BOTH, X, Y, BOTTOM, RIGHT, LEFT, S, N, W, E
from numpy import arange, sin
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Test(Tk):
    def __init__(self):
        Tk.__init__(self, None)
        self.frame=Frame(None)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)

        self.frame.grid(row=0,column=0, sticky=W+E+N+S)

        fig = Figure()

        xval = arange(500)/10.
        yval = sin(xval)

        ax1 = fig.add_subplot(111)
        ax1.plot(xval, yval)

        self.hbar=Scrollbar(self.frame,orient=HORIZONTAL)
        self.vbar=Scrollbar(self.frame,orient=VERTICAL)

        self.canvas=FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.get_tk_widget().config(bg='#FFFFFF',scrollregion=(0,0,500,500))
        self.canvas.get_tk_widget().config(width=800,height=500)
        self.canvas.get_tk_widget().config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=W+E+N+S)

        self.hbar.grid(row=1, column=0, sticky=W+E)
        self.hbar.config(command=self.canvas.get_tk_widget().xview)
        self.vbar.grid(row=0, column=1, sticky=N+S)
        self.vbar.config(command=self.canvas.get_tk_widget().yview)

        self.frame.config(width=100, height=100) # this has no effect

if __name__ == '__main__':

    app = Test()
    app.mainloop()
