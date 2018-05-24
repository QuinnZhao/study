import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
# from tooltips import createToolTip
from sptrader import SpTrader
from info_pannel import InfoPanel
from product_pannel import ProductPanel



class Application(tk.Tk):

    BUY_QUANTITY = 1
    SELL_QUANTITY = 1

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('交易控制界面')
        self.wm_resizable(0, 0) # 不允许改变窗口大小
        self.trader = SpTrader()
        self.trader.add_product('HSIH8')
        self.trader.add_product('HHIH8')
        self.trader.add_product('HSIJ8')
        self.trader.add_chart('63')
        self.trader.add_chart('64')
        self.menu_config = {
            '产品': [('添加产品', self.add_product), ('删除产品', self.delete_product),
                   ('separator', None), ('导出数据', self.export_data),('退出', None) ],
            '指标': [('添加指标', self.add_feature),('删除指标', self.delete_product)]
        }
        self.market_info = {}
        self.data = {}
        for product in self.trader.products: # 初始化产品数据
            self.data[product.name] = {}
        self.product_panels = {}
        self.update_en = True
        self._create_widgets()
        self.update()
        self.mainloop()

    def _create_widgets(self):
        tab_control = ttk.Notebook(self)
        self.tab1 = InfoPanel(tab_control)
        # for _ in self.trader.products:
        # self.tab1.create_table_info_row()
        tab_control.add(self.tab1, text='信息汇总')
        for product in self.trader.products:
            tab = ProductPanel(master=tab_control, name=product.name)
            tab_control.add(tab, text=product.name)
            self.product_panels[product.name] = tab
        tab_control.pack(expand=1, fill='both')
        menu_bar = MyMenu(self, **self.menu_config)
        self.configure(menu=menu_bar)

    def add_product(self):
        i = 2
        for _ in range(1, len(self.trader.products)):
                self.tab1.create_table_info_row(i)
                i +=1

    def delete_product(self):
        pass

    def export_data(self):
        pass

    def add_feature(self):
        pass

    def delete_feature(self):
        pass

    def update(self):
        self.update_data()
        self.after(1000, self.update)

    def update_data(self):
        self.get_maket_info()
        self.update_product_panel()
        # self.get_k_data()
        # self.get_d_data()
        # self.update_program()

    def get_maket_info(self):
        for product in self.trader.products:
            data = product.get_market_info()
            self.market_info[product.name] = data
            if data[0] not in self.data[product.name].keys():
                self.data[product.name][data[0]] = data
                self.update_en = True
            else:
                self.update_en = False
        # print(self.market_info)
        # print(self.data)

    def update_product_panel(self):
        for product in self.trader.products:
            data = self.market_info[product.name]
            # print(data[0])
            # print(data[0] in self.data[product.name].keys())
            if self.update_en:
                self.product_panels[product.name].set_market_info(data)
                self.product_panels[product.name].update()

    # def get_maket_info(self):
    #     for product in self.trader.products:
    #         data = product.get_market_info()
    #         self.tab1.update_info(data)
    #         self.product_panels[product.name].set_market_info(data)
    #         self.product_panels[product.name].update_panel()
    #         self.data = data

    def get_k_data(self):
        # self.trader.get_k_data()
        # k_data = self.trader.k_data
        k_data = self.trader.charts[0].get_features()
        self.tab1.v_k_number.set(k_data[0])
        self.tab1.v_k_ind.set(k_data[1])
        self.tab1.v_k_win.set(k_data[2])
        self.tab1.v_k_data.set(k_data[3])
        self.k_data = k_data

    def get_d_data(self):
        # self.trader.get_d_data()
        # d_data = self.trader.d_data
        d_data = self.trader.charts[1].get_features()
        self.tab1.v_d_number.set(d_data[0])
        self.tab1.v_d_ind.set(d_data[1])
        self.tab1.v_d_win.set(d_data[2])
        self.tab1.v_d_data.set(d_data[3])
        self.d_data = d_data

    def update_program(self):
        # 简单策略：如果D=K>=20，买入；如果D=K>=80，卖出
        k = float(self.k_data[-1])
        d = float(self.d_data[-1])
        ask = float(self.data[8])
        low = float(self.data[17])
        high = float(self.data[16])
        bid = float(self.data[7])
        if d == k >= 20:
            self.tab1.v_buy_quantity.set(self.BUY_QUANTITY)
            self.tab1.v_buy_price.set(ask if ask < low else 0)
            self.trader.ddec3.poke('R2C3',str(self.BUY_QUANTITY).encode(encoding='utf-8'))
            self.trader.ddec3.poke('R2C2', str(ask if ask < low else 0).encode(encoding='utf-8'))
        elif d == k >= 80:
            self.tab1.v_sell_quantity.set(self.SELL_QUANTITY)
            self.tab1.v_sell_price.set(bid if bid > high else 0)
            self.trader.ddec3.poke('R3C3', str(self.SELL_QUANTITY).encode(encoding='utf-8'))
            self.trader.ddec3.poke('R3C2', str(bid if bid > high else 0).encode(encoding='utf-8'))
        else:
            self.tab1.v_sell_price.set(0)
            self.tab1.v_sell_quantity.set(0)
            self.trader.ddec3.poke('R3C2', '0'.encode(encoding='utf-8'))
            self.trader.ddec3.poke('R3C3', '0'.encode(encoding='utf-8'))
            self.tab1.v_buy_price.set(0)
            self.tab1.v_buy_quantity.set(0)
            self.trader.ddec3.poke('R2C2', '0'.encode(encoding='utf-8'))
            self.trader.ddec3.poke('R2C3', '0'.encode(encoding='utf-8'))


class ConfigurePannel(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self._create_widgets()

    def _create_widgets(self):
        lbf1 = ttk.LabelFrame(self, text='配置表')
        lbf1.grid(column=0, row=0, padx=8, pady=4, columnspan=2)
        btn1 = ttk.Button(lbf1, text='button', command=self.click_me)
        btn1.pack()

    def click_me(self):
        print('click!', self.master.master.tab1.market_info[-1])

# class ConfigurePannel(ttk.Frame):
#
#     def __init__(self, master=None):
#         ttk.Frame.__init__(self, master)
#         self._create_widgets()
#
#     def _create_widgets(self):
#         self.lbf = lbf = ttk.LabelFrame(self, text='控件示范区2')
#         lbf.grid(column=0, row=0, padx=8, pady=4)
#         ch_var_dis = tk.IntVar()
#         check1 = tk.Checkbutton(lbf, text='失效选项', variable=ch_var_dis, state='disabled')
#         check1.select()
#         check1.grid(column=0, row=0, sticky=tk.W)
#
#         self.ch_var_un = tk.IntVar()
#         self.check2 = tk.Checkbutton(lbf, text='遵从内心', variable=self.ch_var_un)
#         self.check2.deselect()
#         self.check2.grid(column=1, row=0, sticky=tk.W)
#
#         self.ch_var_en = tk.IntVar()
#         self.check3 = tk.Checkbutton(lbf, text='屈于现实', variable=self.ch_var_en)
#         self.check3.deselect()
#         self.check3.grid(column=2, row=0, sticky=tk.W)
#
#         self.ch_var_un.trace('w', lambda unused0, unused1, unused2: self._check_callback())
#         self.ch_var_en.trace('w', lambda unused0, unused1, unused2: self._check_callback())
#
#         self.values = values = ['富强民主', '文明和谐', '自由平等', '公正法治',
#                   '爱国敬业', '诚信友善'
#                   ]
#         self.rad_var = tk.IntVar()
#         self.rad_var.set(99)
#         for col in range(4):
#             cur_rad = tk.Radiobutton(lbf, text=values[col], variable=self.rad_var, value=col, command=self._rad_call)
#             cur_rad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
#         for col in range(4,6):
#             cur_rad = tk.Radiobutton(lbf, text=values[col], variable=self.rad_var, value=col, command=self._rad_call)
#             cur_rad.grid(column=col-4, row=7, sticky=tk.W, columnspan=3)
#
#         style = ttk.Style()
#         style.configure('BW.TLabel', font=('黑体', '10', 'bold'))
#         ttk.Label(lbf, text='社会主义核心价值观', style='BW.TLabel').grid(column=2, row=7,
#                                                                  columnspan=2, sticky=tk.W)
#
#         lbf1 = ttk.LabelFrame(lbf, text='嵌套区域')
#         lbf1.grid(column=0, row=8, columnspan=4)
#         ttk.Label(lbf1, text='你还年轻，你可以成为任何想成为的人！').grid(column=0, row=0)
#         ttk.Label(lbf1, text='不要在乎一城一池的得失，要执着！').grid(column=0, row=1, sticky=tk.W)
#
#         for child in lbf1.winfo_children():
#             child.grid_configure(padx=8, pady=4)
#
#
#     def _rad_call(self):
#         self.lbf.configure(text=self.values[self.rad_var.get()])
#
#     def _check_callback(self, *ignored_args):
#         if self.ch_var_un.get():
#             self.check3.configure(state='disabled')
#         else:
#             self.check3.configure(state='normal')
#         if self.ch_var_en.get():
#             self.check2.configure(state='disabled')
#         else:
#             self.check2.configure(state='normal')

class Tab3(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='#AFEEEE')
        self._create_widgets()

    def _create_widgets(self):
        for i in range(2):
            canvas = 'canvas' + str(i)
            canvas = tk.Canvas(self, width=162, height=95, highlightthickness=0, bg='#FFFF00')
            canvas.grid_configure(row=i, column=i)


class Tab4(ttk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self._create_widgets()

    def _create_widgets(self):
        self.var = tk.StringVar()
        self.scale = tk.Scale(self, from_=-100, to=100, sliderrelief=tk.RAISED, width=10,
                         orient=tk.HORIZONTAL,
                         length=200
                              , command=self.resize
                          , variable=self.var
                              )
        self.scale.pack()
        self.label = ttk.Label(self, text='')
        self.label.pack(fill='x')

    def resize(self, text): # 这个回调函数需要一个参数text
        self.label.configure(text=self.var.get())



class MyMenu(Menu):

    def __init__(self, master=None, **funcs):
        Menu.__init__(self, master)
        # if len(funcs) < 5:
        #     print('Error: 方法数量少于5')
        #     self._quit()
        self.funcs = funcs
        self._create_menus()

    def _create_menus(self):
         for key, value in self.funcs.items():
            menu = Menu(self, tearoff=0)
            for item in value:
                if item[0] == '退出':
                    command = self._quit
                else:
                    command = item[1]
                if item[0] == 'separator':
                    menu.add_separator()
                else:
                    menu.add_command(label=item[0], command=command)
            self.add_cascade(label=key, menu=menu)

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


