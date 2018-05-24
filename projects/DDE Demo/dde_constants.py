from ctypes import POINTER, c_void_p, c_ulong, c_char_p
from ctypes.wintypes import DWORD   # , UINT

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
DDE_FNOTPROCESSED = 0x0000
DDE_FBUSY = 0x4000

XTYP_ADVSTART = 0x1030
XTYP_ADVSTOP = 0x8040
XTYP_EXECUTE = 0x4050
XTYP_POKE = 0x4090
XTYP_REQUEST = 0x20B0

TIMEOUT_ASYNC = 0xFFFFFFFF