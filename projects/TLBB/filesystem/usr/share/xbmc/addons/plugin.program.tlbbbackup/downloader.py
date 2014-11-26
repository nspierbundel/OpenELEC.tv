import xbmcgui
import urllib
import time
from  utils import progress

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Keyword Installer","Downloading & Copying File",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: progress(nb, bs, fs, dp, start_time))
