import tarfile,shutil,xbmc,os
import time

BASE_URL     = 'http://127.0.0.1:8000'   
BASE_URL     = 'http://54.186.247.241'

GUISETTINS = os.path.join( xbmc.translatePath("special://userdata"),"//guisettings.xml")
GUISETTINS_tlbb = os.path.join( xbmc.translatePath("special://userdata"),"//guisettings_tlbb.xml")

UPLOAD_PROGRESS_FAILED		=	"1"
UPLOAD_FILE_WRITE_FAILED	=	"2"
UPLOAD_INVALID_FILE		=	"3"
UPLOAD_FAILED			=	"4"
WRONG_PASSWORD			=	"11"

def DBG(msg,fName=""):
    msg = str(time.time()) + "  :  " + msg
    if fName:
        f = open(fName,'a')
        f.write(msg)
        f.write("\n")
        f.close()
    print msg
        
def all(_in, _out, dp=None):
    if dp:
        return allWithProgress(_in, _out, dp)

    return allNoProgress(_in, _out)


def allNoProgress(_in, _out):
    try:
        zin = tarfile.TarFile(_in, 'r')
        zin.extractall(_out)
    except Exception, e:
        print str(e)
        return False
        shutil.copy(GUISETTINS,GUISETTINS_tlbb)
    return True


def allWithProgress(_in, _out, dp):

    try:
        zin = tarfile.TarFile(_in, 'r')
        zin.extractall(_out)
    except Exception, e:
        print str(e)
        return False
        shutil.copy(GUISETTINS,GUISETTINS_tlbb)
    return True

def progress(numblocks, blocksize, filesize, dp, start_time):
        try:
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
            kbps_speed = numblocks * blocksize / (time.time() - start_time)
            if kbps_speed > 0:
                eta = (filesize - numblocks * blocksize) / kbps_speed
            else:
                eta = 0
            kbps_speed = kbps_speed / 1024
            total = float(filesize) / (1024 * 1024)
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total)
            e = 'Speed: %.02f Kb/s ' % kbps_speed
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e)
        except:
            percent = 100
            dp.update(percent)
        if dp.iscanceled():
            dp.close()

