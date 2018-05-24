import ctypes
from win32com.client import Dispatch
# MessageBox = ctypes.windll.user32.MessageBoxA
import time
import datetime

xlApp = Dispatch("Excel.Application")
#hide app and alerts
xlApp.Visible = 0
xlApp.Application.DisplayAlerts = 0
nChan = xlApp.Application.DDEInitiate("SPtrader", "Price")
time.sleep(1) # wait for the dde to load 
sSecurity = 'spHSIH8'
while True:
    vrtResult = xlApp.DDErequest(nChan, sSecurity)
    vrtResult = list(vrtResult)
    vrtResult[0] = str(datetime.timedelta(days=vrtResult[0]))
    if vrtResult[-3] != ' ':
        vrtResult[-3] = str(datetime.datetime(1899,12,30) + datetime.timedelta(days=vrtResult[-3])).split(' ')[0]
    if vrtResult[-9] != ' ':
        ratio = round(vrtResult[-9]*100 + 0.005, 2) if vrtResult[-9]>0 else round(vrtResult[-9]*100 - 0.005, 2)
        vrtResult[-9] = f'{ratio}%'
    print('\t'.join([str(i) for i in vrtResult]))
    
    time.sleep(5)
    