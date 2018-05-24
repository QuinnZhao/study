import pandas as pd
from numpy import NaN, zeros


class DataProcess:
    MARKET_INFO_ITEMS = [
        '更新时间', '净头寸', '总量', '代号', '名称', '状况',
        '买入量', '买入价',
        '沽出价', '沽出量',
        '成交价', '平衡价',
        '成交量', '升跌', '升跌百分比', '总成交量',
        '最高', '最低', '开市', '前收市', '收市日期'
    ]
    HEADINGS = ['open', 'low', 'high', 'close', 'volume'] +\
               ['DIFF', 'DEA', 'MACD', 'KDJ_K', 'KDJ_D', 'KDJ_J', 'RSV'] + \
               ['EMA_Close12', 'EMA_Close26']

    def __init__(self):
        self.df = pd.DataFrame()
        self.raw_data = None
        self.update_en = True

    def add_data(self, data=None):
        if not data:
            return
        self.raw_data = data.copy()
        self._data_pre_process()
        if self.df.empty:
            self._new_data()
            # print('new data')
            self._data_post_process()
        elif self.update_en:
            # print('add_data')
            self._add_data()
            self._data_post_process()

    def _data_pre_process(self):
        for index, value in enumerate(self.raw_data):
            if self.MARKET_INFO_ITEMS[index] in ['开市', '前收市', '成交量','最高', '最低' ]:
                if not value.strip():
                    self.raw_data[index] = NaN
                else:
                    self.raw_data[index] = int(self.raw_data[index])
        # print(self.df.index)
        if self.raw_data[0] in self.df.index:
            self.update_en = False
        else:
            self.update_en = True
        # print(self.update_en)

    def _data_post_process(self):
        self._macd()
        self._kdj()
        print(self.df)

    def _new_data(self):
        index = [self._get_update_time()]
        self.df = pd.DataFrame(
            {
                'open': self._get_open_price(),
                'low':  self._get_low_price(),
                'high': self._get_high_price(),
                'close': self._get_close_price(),
                'volume': self._get_volume()
            }, index=index, columns=self.HEADINGS)
        # print(self.HEADINGS)
        # self._macd()
        # self._kdj()
        # print(self.df)


    def _get_update_time(self):
        return self.raw_data[0]

    def _get_open_price(self):
        return self.raw_data[-3]

    def _get_low_price(self):
        return self.raw_data[17]

    def _get_high_price(self):
        return self.raw_data[16]

    def _get_close_price(self):
        return self.raw_data[-2]

    def _get_volume(self):
        return self.raw_data[12]

    def _add_data(self):
        index = [self._get_update_time()]
        df = pd.DataFrame(
            {
                'open': self._get_open_price(),
                'low':  self._get_low_price(),
                'high': self._get_high_price(),
                'close': self._get_close_price(),
                'volume': self._get_volume()
            }, index=index,
            columns=self.HEADINGS
        )
        # print(self.df.columns)
        self.df = self.df.append(df)
        # self._macd()
        # self._kdj()
        print(self.df)

    def _ma(self, n):
        return self.df['close'].rolling(window=n).mean()

    def _ema_close(self,n):
        # return pd.ewma(self.df['close'], span=n)
        return self.df['close'].ewm(span=n, min_periods=0, adjust=True, ignore_na=False).mean()

    def _ema_diff(self, n):
        # return pd.ewma(self.df['DIFF'], span=n)
        return self.df['DIFF'].ewm(span=n, min_periods=0,adjust=True, ignore_na=False).mean()

    def _macd(self):
        self.df['EMA_Close12'] = self._ema_close(12)
        self.df['EMA_Close26'] = self._ema_close(26)
        self.df['DIFF'] = diff = self._ema_close(12) - self._ema_close(26)
        self.df['DEA'] = dea = self._ema_diff(9)
        self.df['MACD'] = macd = (diff - dea) * 2
        # return pd.DataFrame({'DIFF': diff, 'DEA': dea, 'MACD': macd})

    def _llv(self, n):
        return self.df['low'].rolling(window=n).min()

    def _hhv(self, n):
        return self.df['high'].rolling(window=n).max()

    def _sma_rsv(self, n, m):
        df = self.df['RSV'].fillna(0)
        z = len(df)
        var = zeros(z)
        var[0] = df[0]
        for i in range(1, z):
            var[i] = (df[i] * m + var[i - 1] * (n - m)) / n
        for i in range(z):
            df[i] = var[i]
        return df

    def _sma_k(self, n, m):
        df = self.df['KDJ_K'].fillna(0)
        z = len(df)
        var = zeros(z)
        var[0] = df[0]
        for i in range(1, z):
            var[i] = (df[i] * m + var[i - 1] * (n - m)) / n
        for i in range(z):
            df[i] = var[i]
        return df

    def _kdj(self):
        close = self.df['close']
        high = self.df['high']
        low = self.df['low']
        self.df['RSV'] = (close - self._llv(9))/(self._hhv(9) - self._llv(9)) * 100
        self.df['KDJ_K'] = k = self._sma_rsv(3, 1)
        self.df['KDJ_D'] = d = self._sma_k(3, 1)
        self.df['KDJ_J'] = j = 3 * k - 2 * d
        # return pd.DataFrame({'KDJ_K': k, 'KDJ_D': d, 'KDJ_J': j})

    def get_table_data(self):
        df = self.df.tail(1)
        # df.pop('RSV')
        return  df.index.tolist() + df.values.tolist()[-1]

    def get_k_line_data(self):
        return self.df.loc[:, ['open', 'low', 'high', 'close']]

    def get_macd_data(self):
        return self.df.loc[:, ['DIFF', 'DEA', 'MACD']]

    def get_kdj_data(self):
        return self.df.loc[:, ['KDJ_K', 'KDJ_D', 'KDJ_J']]


