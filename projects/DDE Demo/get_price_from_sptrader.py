"""
# Author: Quinn Zhao
# function: Get Price data from SPTrader

"""

from dde_client import DdeClient
import time

if __name__ == "__main__":

    dde = DdeClient('SPtrader', 'Price')
    while True:
        print(dde.request('spHSIH8').decode('gbk'))
        time.sleep(5)
