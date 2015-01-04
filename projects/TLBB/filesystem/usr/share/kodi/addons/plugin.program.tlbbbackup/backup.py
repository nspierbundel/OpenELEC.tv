import tarfile, os, sys
import ftplib
from ftplib import FTP
import xbmc
import time
import requests
from utils import BASE_URL
from utils import DBG

server = 'backups.thelittleblackbox.com'
username = 'tlbbbackups'
password = 'TlbbBB2014!!'
'''
server = '127.0.0.1'
username = 'vir'
password = '1234
'''

folder  =  xbmc.translatePath('special://home')

class upload_in_chunks(object):
    def __init__(self, dp, filename, chunksize=1 << 13):
        self.dp = dp
        self.filename = filename
        self.chunksize = chunksize
        self.totalsize = os.path.getsize(filename)
        self.readsofar = 0

    def __iter__(self):
        with open(self.filename, 'rb') as file:
            while True:
                data = file.read(self.chunksize)
                if not data:
                    sys.stderr.write("\n")
                    break
                self.readsofar += len(str(data))
                percent = self.readsofar * 1e2 / self.totalsize
                self.dp.update(int(percent))
                yield data

    def __len__(self):
        return self.totalsize

class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = len(iterable)

    def read(self, size=-1): # TBD: add buffer for `len(data) > size` case
        return next(self.iterator, b'')

    def __len__(self):
        return self.length

def zipdir(path, zip):
    zip.add(path, arcname=os.path.relpath(path, folder))

def make_zip(backup_name):
    zipname = folder + backup_name + '.tar.gz'
    addons_folder = os.path.join(folder,'addons')
    userdata_folder = os.path.join(folder, 'userdata')
    zipf = tarfile.TarFile(zipname, 'a')
    try: 
        zipdir(addons_folder, zipf)
        zipdir(userdata_folder, zipf)
    except Exception as e:
        DBG(e)
    zipf.close()

    return zipname

def upload_wrapper(dp, user, validateString, backup_name,backup_password,force=0):

    URL = BASE_URL + '/upload/' 
    URL = URL + '?password=' + backup_password + '&validateString=' + validateString + "&user=" + user + "&force=" + str(force)

    if force == 1:
        ret = verifyPassword(user, validateString, backup_name,  backup_password)
        if ret != "ok":
            return ret

    zipname = make_zip(backup_name)
    zipname = os.path.join(folder,zipname)
    #zipname = "/home/prashant/.xbmc/456.tar.gz"
    dp.update(0,"Uploading ...")
    URL = URL + "&fileName=" + os.path.basename(zipname)
    try:
        it = upload_in_chunks(dp, zipname, 1000)
        r = requests.post(URL, data=IterableToFileAdapter(it))
        os.remove(zipname)
        DBG(r.text,'testUpload')
        ret = r.text
        return ret
    except Exception as e:
        DBG(e)
        return -1

def verifyPassword(user, validateString, backupName, password):
    try:
        URL = BASE_URL + "/verifyPassword/"
        URL = URL + "?user=" + user + "&password=" + password + "&validateString=" + validateString + "&backupName=" + backupName
        r = requests.get(URL)
        ret = r.text
        return ret
    except Exception as e:
        DBG(e)

def is_exist(user, validateString, backup_name):
    try:
        URL = BASE_URL + "/isExist/"
        URL = URL + "?user=" + user + "&backupName=" + backup_name + "&validateString=" + validateString
        r = requests.get(URL).text
        if r == "exist":
            return 1
        else:
            return 0
    except Exception as e:
        DBG(e)
