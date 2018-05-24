"""
# originally from http://code.activestate.com/recipes/577654/ (r1)
# modified by Quinn Zhao for Python 3.6
# function: Send DDE Execute command to running program

"""

import time
from ctypes import POINTER, WINFUNCTYPE, c_void_p, c_int, c_ulong, c_char_p
from ctypes.wintypes import BOOL, DWORD, LPCWSTR, UINT  # , ULONG,BYTE, INT

# DECLARE_HANDLE(name) typedef void *name;
HCONV = c_void_p  # = DECLARE_HANDLE(HCONV)
HDDEDATA = c_void_p  # = DECLARE_HANDLE(HDDEDATA)
HSZ = c_void_p  # = DECLARE_HANDLE(HSZ)
LPBYTE = c_char_p  # POINTER(BYTE)
LPDWORD = POINTER(DWORD)
LPSTR = c_char_p
ULONG_PTR = c_ulong

# See windows/ddeml.h for declaration of struct CONVCONTEXT
PCONVCONTEXT = c_void_p

DMLERR_NO_ERROR = 0

# Predefined Clipboard Formats
# CF_TEXT = 1
# CF_BITMAP = 2
# CF_METAFILEPICT = 3
# CF_SYLK = 4
# CF_DIF = 5
# CF_TIFF = 6
# CF_OEMTEXT = 7
# CF_DIB = 8
# CF_PALETTE = 9
# CF_PENDATA = 10
# CF_RIFF = 11
# CF_WAVE = 12
# CF_UNICODETEXT = 13
# CF_ENHMETAFILE = 14
# CF_HDROP = 15
# CF_LOCALE = 16
# CF_DIBV5 = 17
# CF_MAX = 18

# DDE_FACK = 0x8000
# DDE_FBUSY = 0x4000
# DDE_FDEFERUPD = 0x4000
# DDE_FACKREQ = 0x8000
# DDE_FRELEASE = 0x2000
# DDE_FREQUESTED = 0x1000
# DDE_FAPPSTATUS = 0x00FF
# DDE_FNOTPROCESSED = 0x0000

# DDE_FACKRESERVED = (~(DDE_FACK | DDE_FBUSY | DDE_FAPPSTATUS))
# DDE_FADVRESERVED = (~(DDE_FACKREQ | DDE_FDEFERUPD))
# DDE_FDATRESERVED = (~(DDE_FACKREQ | DDE_FRELEASE | DDE_FREQUESTED))
# DDE_FPOKRESERVED = (~(DDE_FRELEASE))

# XTYPF_NOBLOCK = 0x0002
# XTYPF_NODATA = 0x0004
# XTYPF_ACKREQ = 0x0008

# XCLASS_MASK = 0xFC00
# XCLASS_BOOL = 0x1000
# XCLASS_DATA = 0x2000
# XCLASS_FLAGS = 0x4000
# XCLASS_NOTIFICATION = 0x8000

# XTYP_ERROR = (0x0000 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
# XTYP_ADVDATA = (0x0010 | XCLASS_FLAGS)
# XTYP_ADVREQ = (0x0020 | XCLASS_DATA | XTYPF_NOBLOCK)
# XTYP_ADVSTART = 0x1030   # (0x0030 | XCLASS_BOOL)
# XTYP_ADVSTOP = 0x8040  # (0x0040 | XCLASS_NOTIFICATION)
# XTYP_EXECUTE = 0x4050  # (0x0050 | XCLASS_FLAGS)
# XTYP_CONNECT = (0x0060 | XCLASS_BOOL | XTYPF_NOBLOCK)
# XTYP_CONNECT_CONFIRM = (0x0070 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
# XTYP_XACT_COMPLETE = (0x0080 | XCLASS_NOTIFICATION)
# XTYP_POKE = 0x4090  # (0x0090 | XCLASS_FLAGS)
# XTYP_REGISTER = (0x00A0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
# XTYP_REQUEST = 0x20B0  # (0x00B0 | XCLASS_DATA)
# XTYP_DISCONNECT = (0x00C0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
# XTYP_UNREGISTER = (0x00D0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
# XTYP_WILDCONNECT = (0x00E0 | XCLASS_DATA | XTYPF_NOBLOCK)
# XTYP_MONITOR = (0x00F0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)

# XTYP_MASK = 0x00F0
# XTYP_SHIFT = 4

CF_TEXT = 1

DDE_FACK = 0x8000

XTYP_ADVSTART = 0x1030
XTYP_ADVSTOP = 0x8040
XTYP_EXECUTE = 0x4050
XTYP_POKE = 0x4090
XTYP_REQUEST = 0x20B0

TIMEOUT_ASYNC = 0xFFFFFFFF


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

    # def advise(self, item, stop=False):
    #     """Request updates when DDE data changes."""
    #
    #     hsz_item = Dde.create_string_handle(self._idInst, item, 1200)
    #     h_dde_data = Dde.client_transaction(LPBYTE(), 0, self._hConv, hsz_item, CF_TEXT,
    #                                         XTYP_ADVSTOP if stop else XTYP_ADVSTART, TIMEOUT_ASYNC, LPDWORD())
    #     Dde.free_string_handle(self._idInst, hsz_item)
    #     if not h_dde_data:
    #         raise DdeError(f"Unable to {('stop' if stop else 'start')} advise", self._idInst)
    #     Dde.free_data_handle(h_dde_data)

    # def execute(self, command, timeout=5000):
    #     """Execute a DDE command."""
    #     p_data = c_char_p(command)
    #     cb_data = DWORD(len(command) + 1)
    #     h_dde_data = Dde.client_transaction(p_data, cb_data, self._hConv, HSZ(), CF_TEXT, XTYP_EXECUTE,
    #                                         timeout, LPDWORD())
    #     if not h_dde_data:
    #         raise DdeError("Unable to send command", self._idInst)
    #     Dde.free_data_handle(h_dde_data)

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


'''
def win_msg_loop():
    """Run the main windows message loop."""
    from ctypes import POINTER, byref, c_ulong
    from ctypes.wintypes import BOOL, HWND, MSG, UINT

    LPMSG = POINTER(MSG)
    LRESULT = c_ulong
    get_message = get_winfunc("user32", "GetMessageW", BOOL, (LPMSG, HWND, UINT, UINT))
    translate_message = get_winfunc("user32", "TranslateMessage", BOOL, (LPMSG,))
    dispatch_message = get_winfunc("user32", "DispatchMessageW", LRESULT, (LPMSG,))

    msg = MSG()
    lpmsg = byref(msg)
    while get_message(lpmsg, HWND(), 0, 0) > 0:
        translate_message(lpmsg)
        dispatch_message(lpmsg)
'''

if __name__ == "__main__":
    # The following are some example to connect to SPtrader to get price line
    dde = DdeClient('SPtrader', 'Price')
    while True:
        print(dde.request('spHSIH8').decode('gbk'))  # original return data is byte array encoded by 'gbk'
        time.sleep(5)
