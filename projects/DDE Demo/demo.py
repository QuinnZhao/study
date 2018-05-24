from dde_client import DDEClient
import time

if __name__ == '__main__':
    dde1 = DDEClient('SPtrader', 'Price')  # connect to SPtrader to get price data
    dde2 = DDEClient('SPtrader', 'Chart')  # connect to SPtrader to get chart data
    
    while True:
        print(dde1.request('spHSIH8').decode('gbk'))
        for i in range(52,59):
            print(dde2.request(f'indicator_{i}').decode('gbk'))
        
        time.sleep(5)