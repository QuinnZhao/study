from tkinter import ttk
import tkinter as tk
from sptrader import SpTrader
# import matplotlib
# matplotlib.use('TkAgg')
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure

class ProductPanel(ttk.Frame):

    def __init__(self, master=None, name=None, headings=None):
        ttk.Frame.__init__(self, master)
        self.info_items = SpTrader.MARKET_INFO_ITEMS
        self.info_variables = {
            item : tk.StringVar() for item in self.info_items
        }
        if not headings:
            self.headings = ['Time','Open', 'Low', 'High', 'Close', 'Volume']
        else:
            self.headings = ['Time','Open', 'Low', 'High', 'Close', 'Volume'] + headings

        self._create_widgets()
        self.name = name
        self.market_info = None
        self.table_data = None

    def set_market_info(self, market_info=None):
        self.market_info = market_info

    def _create_widgets(self):
        self._create_top()
        self._create_bottom()

    def _create_top(self):
        self.lbf1 = ttk.LabelFrame(self, text='实时量价信息')
        self.lbf1.grid(column=0, row=0, padx=8, pady=4, columnspan=2)

        self.create_table_info_heads()
        self.create_table_info_row(1)

    def _create_bottom(self):
        lbf2 = ttk.LabelFrame(self, text='数据与技术指标', width=150)
        lbf2.grid(column=0, row=1, padx=8, pady=4, sticky='W')
        self.tree = tree = ttk.Treeview(lbf2, show='headings', height=20)  # 隐藏首列
        tree['columns'] = self.headings
        for item in tree['columns']:
            tree.column(item, anchor='center', width=100)
            tree.heading(item, text=item)
        vbar = ttk.Scrollbar(lbf2, orient=tk.VERTICAL, command=tree.yview)

        hbar = ttk.Scrollbar(lbf2, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        tree.grid(row=0, column=0, sticky=tk.NSEW)
        vbar.grid(row=0, column=1, sticky=tk.NS)
        hbar.grid(row=1, column=0, sticky=tk.EW)

    def create_table_info_heads(self):
        for index, item in enumerate(self.info_items):
            width = 8
            if item == '名称':
                width = 12
            ttk.Label(self.lbf1, text=item).grid(column=index, row=0, sticky='W')

    def create_table_info_row(self,i):
        for index, item in enumerate(self.info_items):
            width = 8
            if item == '名称':
                width = 12
            ttk.Entry(self.lbf1, width=width, textvariable=self.info_variables[item],
                      state='readonly').grid(column=index, row=i, sticky='W')

    def update(self, data=None):
        self.update_panel()
        self.update_table(data)

    def update_panel(self):
        if not self.market_info:
            return
        # Update top section
        for i in range(min(len(self.info_items), len(self.market_info))):
            self.info_variables[self.info_items[i]].set(self.market_info[i])

    def update_table(self, data=None):
        if not data:
            time = self.market_info[0]
            open = self.market_info[-3]
            low = self.market_info[17]
            high = self.market_info[16]
            close = self.market_info[-2]
            volume = self.market_info[12]
            self.tree.insert('', '0', values=(time, open, low, high, close, volume)) # 数据在表格第一行之前插入
        else:
            self.tree.insert('', 0, values=data)