import time
import xbmc
import shutil
import zipfile
import urllib, urllib2
import extract
import downloader

url = 'http://www.dropbox.com/s/ci5sd9pu3jmwc9j/Super%20Favourites.zip?dl=1'
lib = '/storage/.kodi/userdata/addon_data/plugin.program.super.favourites/'
libx = '/storage/.kodi/temp/x.zip'
if __name__ == '__main__':
    monitor = xbmc.Monitor() 
    while True:
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(1800):
            # Abort was requested while waiting. We should exit
            break
        if not xbmc.Player().isPlaying():
            downloader.download(url, libx)
            extract.all(libx,lib)

