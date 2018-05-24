import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import sys


root = tk.Tk()
root.wm_title('Embedding in Tk')

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)

a.plot(t,s)
a.set_xlabel('X in axis label')
a.set_ylabel('Y label')

canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
button = tk.Button(master=root, text='Quit', command=sys.exit)
button.pack(side=tk.BOTTOM)
tk.mainloop()