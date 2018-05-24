from dde_client import DdeClient
from data_process import DataProcess

class SpTrader:
    MARKET_INFO_ITEMS = [
        '更新时间', '净头寸', '总量', '代号', '名称', '状况',
        '买入量', '买入价',
        '沽出价', '沽出量',
        '成交价', '平衡价',
        '成交量', '升跌', '升跌百分比', '总成交量',
        '最高', '最低', '开市', '前收市', '收市日期'
    ]

    def __init__(self):
        self.ddec1 = DdeClient('SPtrader', 'Price')
        self.ddec2 = DdeClient('SPtrader', 'Chart')
        # self.ddec3 = DdeClient('Excel', '[trader_demo.xlsx]sheet1')
        self.products = []
        self.charts = []
        self.k_data = []
        self.d_data = []
        self.product_market_info = {}

    def add_product(self, product_name):
        product = Product(product_name, self.ddec1)
        self.products.append(product)
        self.product_market_info[product_name] = product.get_market_info()

    def add_chart(self, indicator_num):
        self.charts.append(Chart(indicator_num, self.ddec2))

    def get_products(self):
        return self.products


class Product:

    def __init__(self, product_name, ddec):
        self.name = product_name
        self.ddec = ddec
        self.request_item = f'sp{product_name}'
        self.market_info = []
        self.product_data_process = DataProcess()

    def get_market_info(self):
        data = self.ddec.request(self.request_item).decode('gbk')
        data = data.strip().split('\t')
        prices = data[10].split('/')         # 拆分成交价和平衡价
        if len(prices) == 1:
            prices.append(' ')
        data = data[:10] + prices + data[11:]
        # print(data)
        self.market_info = data
        self.product_data_process.add_data(data)
        return data

    def ask_price(self):
        return float(self.market_info[8])

    def bid_price(self):
        return float(self.market_info[7])

    def low_price(self):
        return float(self.market_info[17])

    def high_price(self):
        return float(self.market_info[16])

    def close_price(self):
        return float(self.market_info[-2])

    def open_price(self):
        return float(self.market_info[-3])

    def volume(self):
        return int(self.market_info[12])

    def net_position(self):
        return int(self.market_info[1])

    def get_name(self):
        return self.name


class Chart:

    def __init__(self, indicator_number, ddec):
        self.num = indicator_number
        self.ddec = ddec
        self.request_item = f'indicator_{self.num}'
        self.data = []

    def get_features(self):
        data = self.ddec.request(self.request_item).decode('gbk')
        data = data.strip().split('\t')
        print(data)
        self.data = data
        return data

    def get_num(self):
        return self.num

    def get_name(self):
        return self.data[1]

    def get_value(self):
        return self.data[-1]

    def get_win(self):
        return self.data[-2]

