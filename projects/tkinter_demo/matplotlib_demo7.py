from tkinter import Tk, Button, Frame, Canvas, Scrollbar
import tkinter as tk
import math

from matplotlib import pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def add_scrolling_figure(figure, frame):

    canvas = Canvas(frame)

    canvas.grid(row=0, column=0, sticky=tk.NSEW)

    x_scrollbar = Scrollbar(frame, orient=tk.HORIZONTAL)

    y_scrollbar = Scrollbar(frame)

    x_scrollbar.grid(row=1, column=0, sticky=tk.EW)

    y_scrollbar.grid(row=0, column=1, sticky=tk.NS)

    canvas.config(xscrollcommand=x_scrollbar.set)

    x_scrollbar.config(command=canvas.xview)

    canvas.config(yscrollcommand=y_scrollbar.set)

    y_scrollbar.config(command=canvas.yview)

    # plug in the figure

    fig_agg = FigureCanvasTkAgg(figure, canvas)

    mpl_canvas = fig_agg.get_tk_widget()

    mpl_canvas.grid(sticky=tk.NSEW)

    # and connect figure with scrolling region

    canvas.create_window(0, 0, window=mpl_canvas)

    canvas.config(scrollregion=canvas.bbox(tk.ALL))

def change_size(figure, factor, frame=None):

    old_size = figure.get_size_inches()

    print(f"old size is {old_size}")

    new_side = [old_size[0]*factor, old_size[1]]

    # figure.set_size_inches([factor * s  for s in old_size])
    figure.set_size_inches(new_side)

    print(f"new size is {figure.get_size_inches()}")

    print()
    plt.plot(range(int(10*factor)), [math.sin(x) for x in range(int(10*factor))])

    # plt.show()
    add_scrolling_figure(figure, frame)

    figure.canvas.draw()

if __name__ == "__main__":

    root = Tk()

    root.rowconfigure(0, weight=1)

    root.columnconfigure(0, weight=1)

    frame = Frame(root)

    frame.grid(column=0, row=0, sticky=tk.NSEW)

    frame.rowconfigure(0, weight=1)

    frame.columnconfigure(0, weight=1)

    figure = plt.figure(dpi=150, figsize=(4, 4))

    plt.plot(range(10), [math.sin(x) for x in range(10)])

    add_scrolling_figure(figure, frame)

    buttonFrame = Frame(root)

    buttonFrame.grid(row=0, column=1, sticky=tk.NS)

    biggerButton = Button(buttonFrame, text="larger",

                          command=lambda : change_size(figure, 1.5, frame))

    biggerButton.grid(column=0, row=0)

    smallerButton = Button(buttonFrame, text="smaller",

                           command=lambda : change_size(figure, .5, frame))

    smallerButton.grid(column=0, row=1)

    root.mainloop()