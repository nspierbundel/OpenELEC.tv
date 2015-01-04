import urllib2
import xbmc
import xbmcgui
import xbmcplugin
import os
import inspect


def getResponse(url, size):
    try:
        req = urllib2.Request(url)
       
        if size > 0:
            size = int(size)
            req.add_header('Range', 'bytes=%d-' % size)

        resp = urllib2.urlopen(req, timeout=10)
        return resp
    except:
        return None


def download(url, dest, title=None):
    if not title:
        title  = 'XBMC Download'
                
    script = inspect.getfile(inspect.currentframe())    
    cmd    = 'RunScript(%s, %s, %s, %s)' % (script, url, dest, title)
    
    xbmc.executebuiltin(cmd)


def doDownload(url, dest, title):
    file = dest.rsplit(os.sep, 1)[-1]

    #workaround bug that causes Frodo to lockup when stop is called       
    xbmc.executebuiltin('ActivateWindow(%d)' % 10025)       
    xbmc.Player().stop()   
    
    resp = getResponse(url, 0)
    
    if not resp:
        xbmcgui.Dialog().ok(title, dest, 'Download failed', 'No response from server')
        return

    try:    content = int(resp.headers['Content-Length'])
    except: content = 0
    
    try:    resumable = 'bytes' in resp.headers['Accept-Ranges'].lower()
    except: resumable = False
    
    #print "Download Header"
    #print resp.headers
    if resumable:
        print "Download is resumable"
    
    if content < 1:
        xbmcgui.Dialog().ok(title, file, 'Unknown filesize', 'Unable to download')
        return
    
    size = 1024 * 1024
    mb   = content / (1024 * 1024)

    if content < size:
        size = content
        
    total   = 0
    notify  = 0
    errors  = 0
    count   = 0
    resume  = 0
    sleep   = 0
    
    if xbmcgui.Dialog().yesno(title + ' - Confirm Download', file, 'Complete file is %dMB' % mb, 'Continue with download?', 'Confirm',  'Cancel') == 1:
        return
                
    f = open(dest, mode='wb')
    
    chunk  = None
    chunks = []
    
    while True:
        downloaded = total
        for c in chunks:
            downloaded += len(c)
        percent = min(100 * downloaded / content, 100)
        if percent >= notify:
            xbmc.executebuiltin( "XBMC.Notification(%s,%s,%i)" % ( title + ' - Download Progress - ' + str(percent)+'%', dest, 10000))
            notify += 10

        chunk = None
        error = False

        try:        
            chunk  = resp.read(size)
            if not chunk:                
                if percent < 99:                   
                    error = True
                else:                     
                    while len(chunks) > 0:
                        c = chunks.pop(0)
                        f.write(c)
                        del c
                
                    f.close()
                    print '%s download complete' % (dest)
                    xbmcgui.Dialog().ok(title, dest, '' , 'Download finished')
                    return
        except Exception, e:
            print str(e)
            error = True
            sleep = 10
            errno = 0
            
            if hasattr(e, 'errno'):
                errno = e.errno
                
            if errno == 10035: # 'A non-blocking socket operation could not be completed immediately'
                pass
            
            if errno == 10054: #'An existing connection was forcibly closed by the remote host'
                errors = 10 #force resume
                sleep  = 30
                
            if errno == 11001: # 'getaddrinfo failed'
                errors = 10 #force resume
                sleep  = 30
                        
        if chunk:
            errors = 0      
            chunks.append(chunk)           
            if len(chunks) > 5:
                c = chunks.pop(0)
                f.write(c)
                total += len(c)
                del c
                
        if error:
            errors += 1
            count  += 1
            print '%d Error(s) whilst downloading %s' % (count, dest)
            xbmc.sleep(sleep*1000)

        if (resumable and errors > 0) or errors >= 10:
            if (not resumable and resume >= 10) or resume >= 100:
                #Give up!
                print '%s download canceled - too many error whilst downloading' % (dest)
                xbmcgui.Dialog().ok(title, dest, '' , 'Download failed')
                return
            
            resume += 1
            errors  = 0
            if resumable:
                chunks  = []
                #create new response
                print 'Download resumed (%d) %s' % (resume, dest)
                resp = getResponse(url, total)
            else:
                #use existing response
                pass


if __name__ == '__main__': 
    if 'download.py' in sys.argv[0]:       
        doDownload(sys.argv[1], sys.argv[2], sys.argv[3])