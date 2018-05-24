from tkinter import ttk
import tkinter as tk
from sptrader import SpTrader


class InfoPanel(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.info_items = SpTrader.MARKET_INFO_ITEMS
        self.info_variables = {
            item : tk.StringVar() for item in self.info_items
        }
        self._create_widgets()

    def _create_widgets(self):
        self._create_market_info()
        self._create_program_info()
        self._create_feature_info()

    def update_info(self, market_info=None):
        if not market_info:
            return

        for i in range(min(len(self.info_items), len(market_info))):
            self.info_variables[self.info_items[i]].set(market_info[i])

    def _create_market_info(self):
        self.lbf1 = ttk.LabelFrame(self, text='实时量价信息')
        self.lbf1.grid(column=0, row=0, padx=8, pady=4, columnspan=2)

        self.create_table_info_heads()
        self.create_table_info_row(1)

    def _create_program_info(self):

        lbf2 = ttk.LabelFrame(self, text='交易指令')
        lbf2.grid(column=0, row=1, padx=8, pady=4, sticky='W')
        ttk.Label(lbf2, text='Program', width=12).grid(column=0, row=0, sticky='W', columnspan=2)
        ttk.Label(lbf2, text='Price').grid(column=2, row=0, sticky='W')
        ttk.Label(lbf2, text='Quantity').grid(column=3, row=0, sticky='W')
        ttk.Label(lbf2, text='Buy').grid(column=0, row=1, sticky='W', columnspan=2)
        ttk.Label(lbf2, text='Sell').grid(column=0, row=2, sticky='W', columnspan=2)
        self.v_buy_price, self.v_sell_price = tk.StringVar(), tk.StringVar()
        for index, item in enumerate([self.v_buy_price, self.v_sell_price]):
            ttk.Entry(lbf2, width=12, textvariable=item,
                      state='readonly').grid(column=2, row=index+1, sticky='W')

        self.v_buy_quantity, self.v_sell_quantity = tk.StringVar(), tk.StringVar()
        for index, item in enumerate([self.v_buy_quantity, self.v_sell_quantity]):
            ttk.Entry(lbf2, width=12, textvariable=item,
                      state='readonly').grid(column=3, row=index+1, sticky='W')


    def _create_feature_info(self):
        lbf3 = ttk.LabelFrame(self, text='实时技术指标')
        lbf3.grid(column=1, row=1, padx=8, pady=8, sticky='W')
        for index, item in enumerate(['Number', 'Indicator', 'Window', 'Data']):
            ttk.Label(lbf3, text=item).grid(column=index, row=0, sticky='W')
        (self.v_k_number, self.v_k_ind, self.v_k_win,
                          self.v_k_data) =  (tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar())
        for index, item in enumerate([self.v_k_number, self.v_k_ind, self.v_k_win, self.v_k_data]):
            ttk.Entry(lbf3, width=12, textvariable=item,
                      state='readonly').grid(column=index, row=1, sticky='W')


        (self.v_d_number, self.v_d_ind,
         self.v_d_win, self.v_d_data) = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        for index, item in enumerate([self.v_d_number, self.v_d_ind, self.v_d_win, self.v_d_data]):
            ttk.Entry(lbf3, width=12, textvariable=item,
                      state='readonly').grid(column=index, row=2, sticky='W')

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