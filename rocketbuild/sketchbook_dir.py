import ctypes.wintypes
import os
from os.path import expanduser, join
CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

def sketchbook_dir():
    rootpath = ""
    if os.name == 'nt':
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        rootpath = buf.value
    else:
        rootpath = expanduser("~")
    return join(rootpath, 'Arduino', 'Libraries')