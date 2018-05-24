"""
# Author: Quinn Zhao
# function: Send DDE Execute command to running program

"""

import time
from ctypes import WINFUNCTYPE,  c_int
from ctypes.wintypes import BOOL, LPCWSTR, UINT
from dde_constants import *


def get_winfunc(libname, funcname, restype=None, argtypes=(), _libcache=None):
    """Retrieve a function from a library, and set the data types."""
    from ctypes import windll

    if not _libcache:
        _libcache = {}
    if libname not in _libcache:
        _libcache[libname] = windll.LoadLibrary(libname)
    func = getattr(_libcache[libname], funcname)
    func.argtypes = argtypes
    func.restype = restype

    return func


DDECALLBACK = WINFUNCTYPE(HDDEDATA, UINT, UINT, HCONV, HSZ, HSZ, HDDEDATA,
                          ULONG_PTR, ULONG_PTR)


class Dde:
    """Object containing all the DDE functions"""
    access_data = get_winfunc("user32", "DdeAccessData", LPBYTE, (HDDEDATA, LPDWORD))
    client_transaction = get_winfunc("user32", "DdeClientTransaction", HDDEDATA,
                                     (LPBYTE, DWORD, HCONV, HSZ, UINT, UINT, DWORD, LPDWORD))
    connect = get_winfunc("user32", "DdeConnect", HCONV, (DWORD, HSZ, HSZ, PCONVCONTEXT))
    create_string_handle = get_winfunc("user32", "DdeCreateStringHandleW", HSZ, (DWORD, LPCWSTR, UINT))
    disconnect = get_winfunc("user32", "DdeDisconnect", BOOL, (HCONV,))
    get_last_error = get_winfunc("user32", "DdeGetLastError", UINT, (DWORD,))
    initialize = get_winfunc("user32", "DdeInitializeW", UINT, (LPDWORD, DDECALLBACK, DWORD, DWORD))
    free_data_handle = get_winfunc("user32", "DdeFreeDataHandle", BOOL, (HDDEDATA,))
    free_string_handle = get_winfunc("user32", "DdeFreeStringHandle", BOOL, (DWORD, HSZ))
    query_string = get_winfunc("user32", "DdeQueryStringA", DWORD, (DWORD, HSZ, LPSTR, DWORD, c_int))
    unaccess_data = get_winfunc("user32", "DdeUnaccessData", BOOL, (HDDEDATA,))
    uninitialize = get_winfunc("user32", "DdeUninitialize", BOOL, (DWORD,))
    create_data_handle = get_winfunc('user32', 'DdeCreateDataHandle', HDDEDATA, (DWORD, LPBYTE, DWORD, HSZ, UINT, UINT))


class DdeError(RuntimeError):
    """Exception raise when a DDE error occurs."""

    def __init__(self, msg, id_inst=None):
        if id_inst is None:
            RuntimeError.__init__(self, msg)
        else:
            RuntimeError.__init__(self, f"{msg} (err={hex(Dde.get_last_error(id_inst))})")


class DdeClient:
    """The DDEClient class.
    Use this class to create and manage a connection to a service/topic.  To get
    classbacks subclass DDEClient and overwrite callback."""

    def __init__(self, service, topic):
        """Create a connection to a service/topic."""
        from ctypes import byref

        self._idInst = DWORD(0)
        self._hConv = HCONV()

        self._callback = DDECALLBACK(self._callback)
        res = Dde.initialize(byref(self._idInst), self._callback, 0x00000010, 0)
        if res != DMLERR_NO_ERROR:
            raise DdeError(f"Unable to register with DDEML (err={hex(res)})")

        hszService = Dde.create_string_handle(self._idInst, service, 1200)
        hszTopic = Dde.create_string_handle(self._idInst, topic, 1200)
        self._hConv = Dde.connect(self._idInst, hszService, hszTopic, PCONVCONTEXT())
        Dde.free_string_handle(self._idInst, hszTopic)
        Dde.free_string_handle(self._idInst, hszService)
        if not self._hConv:
            raise DdeError("Unable to establish a conversation with server", self._idInst)

    def __del__(self):
        """Cleanup any active connections."""
        if self._hConv:
            Dde.disconnect(self._hConv)
        if self._idInst:
            Dde.uninitialize(self._idInst)

    def request(self, item, timeout=5000):
        """Request data from DDE service."""
        from ctypes import byref

        hsz_item = Dde.create_string_handle(self._idInst, item, 1200)
        h_dde_data = Dde.client_transaction(LPBYTE(), 0, self._hConv, hsz_item, CF_TEXT,
                                            XTYP_REQUEST, timeout, LPDWORD())
        Dde.free_string_handle(self._idInst, hsz_item)
        p_data = None
        if not h_dde_data:
            raise DdeError("Unable to request item", self._idInst)

        if timeout != TIMEOUT_ASYNC:
            pdw_size = DWORD(0)
            p_data = Dde.access_data(h_dde_data, byref(pdw_size))
        return p_data

    def poke(self, item, data, timeout=5000):
        """Poke (unsolicited) data to DDE server"""
        from ctypes import byref

        hsz_item = Dde.create_string_handle(self._idInst, item, 1200)
        p_data = c_char_p(data)
        cb_data = DWORD(len(data) + 1)
        pdw_result = DWORD(0)
        h_dde_data = Dde.client_transaction(p_data, cb_data, self._hConv, hsz_item, CF_TEXT, XTYP_POKE,
                                          timeout, byref(pdw_result))
        Dde.free_string_handle(self._idInst, hsz_item)

        if h_dde_data == DDE_FACK:
            Dde.free_data_handle(h_dde_data)
            return 0
        elif h_dde_data == DDE_FNOTPROCESSED:
            Dde.free_data_handle(h_dde_data)
            print('data or format is rejected by server')
            return 1
        elif h_dde_data == DDE_FBUSY:
            Dde.free_data_handle(h_dde_data)
            print('server is busy now, please try again later')
            return 2
        '''
        if not hDdeData:
            print("Value of pdwResult: ", pdwResult)
            raise DdeError("Unable to poke to server", self._idInst)

        if timeout != TIMEOUT_ASYNC:
            pdwSize = DWORD(0)
            pData = Dde.access_data(hDdeData, byref(pdwSize))
            if not pData:
                Dde.free_data_handle(hDdeData)
                raise DdeError("Unable to access data in poke function", self._idInst)
            Dde.unaccess_data(hDdeData)
        else:
            pData = None
        Dde.free_data_handle(hDdeData)
        return pData
        '''

    @staticmethod
    def callback(value, item=None):
        """Callback function for advice."""
        print(f"{item}: {value}")

    def _callback(self,
                  # w_type, u_fmt, h_conv, hsz1,
                  hsz2, h_dde_data,
                  # dw_data1, dw_data2
                  ):
        from ctypes import byref, create_string_buffer

        dw_size = DWORD(0)
        p_data = Dde.access_data(h_dde_data, byref(dw_size))
        if p_data:
            item = create_string_buffer('\000' * 128)
            Dde.query_string(self._idInst, hsz2, item, 128, 1004)
            # self.callback(p_data, item.value)
            Dde.unaccess_data(h_dde_data)
            return DDE_FACK
        return 0


if __name__ == "__main__":
    # The following are some example to connect to SPtrader to get price line
    # dde = DdeClient('SPtrader', 'Price')
    # while True:
    #     print(dde.request('spHSIH8').decode('gbk'))  # original return data is byte array encoded by 'gbk'
    #     time.sleep(5)

    dde1 = DdeClient('Excel', 'test11.xlsx')
    data = b'100'
    data1 = b'123'
    dde1.poke('R1C1', data)
    dde1.poke('R2C3', data1)
