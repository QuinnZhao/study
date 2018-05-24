import tkinter as tk
from tkinter import ttk
from sptrader import SpTrader
from ui import ApplicationUI
from configparser import ConfigParser


class Application(ApplicationUI):

    BUY_QUANTITY = 1
    SELL_QUANTITY = 1

    def __init__(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.trader = SpTrader()
        if parser.sections():       #  如果已经配置好产品，则直接加载
            for item in parser.sections():
                self.trader.add_product(item)

        self.market_info = {}
        self.data = {}
        for product in self.trader.products: # 初始化产品数据
            self.data[product.name] = {}
        self.update_en = True
        ApplicationUI.__init__(self)

    def _create_widgets(self):    # 重载_create_wigets以确保产品页面可以正确初始化
        ApplicationUI._create_widgets(self)
        for product in self.trader.products:
            self.add_product_panels(product.name)

    def add_product(self):
        for product in self.trader.products:
            self.add_product_panels(product.name)

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

    def get_maket_info(self):
        for product in self.trader.products:
            data = product.get_market_info()
            self.market_info[product.name] = data
            # break

    def update_product_panel(self):
        for product in self.trader.products:
            data = self.market_info[product.name]
            data1 = product.product_data_process.get_table_data()
            print(product.product_data_process.df)
            if self.update_en:
                self.product_panels[product.name].set_market_info(data)
                self.product_panels[product.name].update(data1)
            # break

    def get_k_data(self):
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


if __name__ == '__main__':
    Application()


