import tkinter as tk
from tkinter import ttk
from tkinter import Menu
# from tkinter import messagebox as mBox
# from tooltips import createToolTip
# from sptrader import SpTrader
from info_pannel import InfoPanel
from product_pannel import ProductPanel
# from product_chart import ProductChart


class ApplicationUI(tk.Tk):
    HEADINGS = ['DIFF', 'DEA', 'MACD', 'KDJ_K', 'KDJ_D', 'KDJ_J']

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('交易控制界面')
        self.wm_resizable(0, 0) # 不允许改变窗口大小

        self.menu_config = {
            '产品': [('添加产品', self.add_product), ('删除产品', self.delete_product),
                   ('separator', None), ('导出数据', self.export_data),('退出', None) ],
            '指标': [('添加指标', self.add_feature),('删除指标', self.delete_product)]
        }

        self.product_panels = {}

        self._create_widgets()
        self.update()
        self.mainloop()

    def _create_widgets(self):
        self.tab_control = ttk.Notebook(self)
        self.tab1 = InfoPanel(self.tab_control)
        self.tab_control.add(self.tab1, text='信息汇总')
        # tab_test = ProductChart(self.tab_control)
        # self.tab_control.add(tab_test,text='test')
        self.tab_control.pack(expand=1, fill='both')
        menu_bar = MyMenu(self, **self.menu_config)
        self.configure(menu=menu_bar)

    def add_product_panels(self, text=''):
        tab = ProductPanel(master=self.tab_control, name=text, headings=self.HEADINGS)
        self.tab_control.add(tab, text=text)
        self.product_panels[text] = tab

    def add_product(self):
        pass

    def delete_product(self):
        pass

    def export_data(self):
        pass

    def add_feature(self):
        pass

    def delete_feature(self):
        pass

    def update(self):
        pass


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


class MyMenu(Menu):

    def __init__(self, master=None, **funcs):
        Menu.__init__(self, master)
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

    def _quit(self):
        self.master.quit()
        self.master.destroy()
        exit()


if __name__ == '__main__':
    ApplicationUI()


