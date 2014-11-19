import zipfile
import os

def all(_in, _out, dp=None):
    if dp:
        return allWithProgress(_in, _out, dp)

    return allNoProgress(_in, _out)
        

def allNoProgress(_in, _out):

    try:
        zin       = zipfile.ZipFile(_in, 'r')
        addonname = zin.namelist()[0]
        zin.extractall(_out)
    except Exception, e:
        zin.close()
        return False

    zin.close()
    return addonname.split(os.sep)[:1][0]


def allWithProgress(_in, _out, dp):

    zin       = zipfile.ZipFile(_in,  'r')

    nFiles    = float(len(zin.infolist()))
    addonname = zin.namelist()[0]
    count     = 0

    try:
        for item in zin.infolist():
            count += 1
            update = count / nFiles * 100
    
            dp.update(int(update))
            zin.extract(item, _out)
    except Exception, e:
        zin.close()
        return False
    
    zin.close
    return addonname.split(os.sep)[:1][0]
