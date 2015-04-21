# -*- coding: cp1252 -*-
#Custom vipplaylist by Blazetamer 
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,urlresolver,xbmc,os,xbmcaddon,main,math,cookielib,os.path, string
from resources.modules import main
import urlresolver
import vipplaylist
from addon.common.addon import Addon
from addon.common.net import Net
from t0mm0.common.net import Net as net
try:
    import CommonFunctions as common
except:
    import commonfunctionsdummy as common
import requests
####################
#
####################

addon_id = 'plugin.video.phstreams'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.phstreams', sys.argv)
ADDON = xbmcaddon.Addon(id='plugin.video.phstreams')
#net = Net(http_debug=True)
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
#========================Alternate Param Stuff=======================
mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
favtype = addon.queries.get('favtype', '')
mainimg = addon.queries.get('mainimg', '')
gomode = addon.queries.get('gomode', '')
iconimage = addon.queries.get('iconimage', '')
artwork = addon.queries.get('artwork', '')
art = addon.queries.get('art', '')
fanart = addon.queries.get('fanart', '')
headers = addon.queries.get('headers', '')
loggedin = addon.queries.get('loggedin', '')
header_dict = addon.queries.get('header_dict', '')
fanart = addon.queries.get('fanart', '')
console = addon.queries.get('console', '')
dlfoldername = addon.queries.get('dlfoldername', '')
ext = addon.queries.get('ext', '')
#======================== END Alternate Param Stuff=======================
#newagent ='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'
#net.set_user_agent(newagent)
#cookiejar = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookiejar = addon.get_profile()
cookiejar = os.path.join(cookiejar,'cookies.lwp')
settings = xbmcaddon.Addon(id='plugin.video.phstreams')
elogo = ''
datapaths = xbmc.translatePath(ADDON.getAddonInfo('profile'))
CookiePath=os.path.join(datapaths,'Cookies')
try: os.makedirs(CookiePath)
except: pass

def LogNotify(title,message,times,icon):
        xbmc.executebuiltin("XBMC.Notification("+title+","+message+","+times+","+icon+")")

#####Start Resolvers========================
class ResolverError(Exception):
    def __init__(self, value, value2):
        value = value
        value2 = value2
    def __str__(self):
        return repr(value,value2)

def resolve_url(murl):
    #stream_url = False
    
    if(murl):
        #try:
            
            if 'project-free-upload' in murl:
                stream_url=resolve_projectfreeupload(murl)
                return stream_url
        
            if 'veehd' in murl :
                stream_url=resolve_veehd(murl)
                print "STREAMURL IS ="+stream_url
                return stream_url
        
            if 'videomega'in murl :
                stream_url=resolve_videomega(murl)
                return stream_url

            if 'youtube' in murl:
                try:murl=murl.split('watch?v=')[1]
                except:
                    try:murl=murl.split('com/v/')[1]
                    except:
                        try:murl=murl.split('videoid=') [1]
                           
                        except: murl=murl.split('com/embed/') [1]              
                stream_url='plugin://plugin.video.youtube/?action=play_video&videoid=' +str(murl)
                return stream_url    
                
            if 'epicshare'in murl:
                stream_url=resolve_epicshare(murl)
                return stream_url

                
            if 'lemuploads'in murl :
                stream_url=resolve_lemupload(murl)
                return stream_url
                
                           
            if 'hugefiles'in murl:
                stream_url=resolve_hugefiles(murl)
                return stream_url

                
            if 'megarelease' in murl:
                stream_url=resolve_megarelease(murl)
                return stream_url
                
            
            if 'bayfiles' in murl:
                stream_url=resolve_bayfiles(murl)
                return stream_url
            
            
            if 'vidspot' in murl:
                stream_url=resolve_vidspot(murl)
                return stream_url

                
            if 'youwatch' in murl:
                stream_url=resolve_youwatch(murl)
                return stream_url

                
            if 'vk.com' in murl:
                stream_url=resolve_VK(murl)
                return stream_url

                
            if '(?i)(firedrive|putlocker)' in murl:
                stream_url=resolve_firedrive(murl)
                return stream_url

                
            
            if 'yify.tv' in murl:
                stream_url=resolve_yify(murl)
                return stream_url

                
            if 'mail.ru' in murl:
                stream_url=resolve_mailru(murl)
                return stream_url

                
            if 'g2g.fm' in murl:
                stream_url=resolve_g2g(murl)
                return stream_url

                
            if 'docs.google' in murl:
                stream_url=resolve_googleDocs(murl)
                return stream_url

                
            if 'mrfile' in murl:
                stream_url=resolve_mrfile(murl)
                return stream_url
                
            
            if 'picasaweb.google' in murl:
                stream_url=resolve_picasaWeb(murl)

            
            if settings.getSetting("use_billion")== 'true'and 'billionuploads' in murl:
                #if 'billionuploads' in murl:
                    stream_url=resolve_billionuploads(murl)
                    return stream_url

            if settings.getSetting("use_movreel")== 'true'and 'movreel' in murl:
                #if 'movreel' in murl:
                    stream_url=resolve_movreel(murl)
                    return stream_url

            if settings.getSetting("use_180upload")== 'true'and '180upload' in murl:
                #if '180upload' in murl: 
                    stream_url=resolve_180upload(murl)
                    return stream_url    
            
            else:
                
                hmf = urlresolver.HostedMediaFile(murl)
                if hmf:
                     host = hmf.get_host()
                     dlurl = urlresolver.resolve(murl)
                     return dlurl
  
                else:
                     return murl
            
    

def logerror(log):
    xbmc.log(log, xbmc.LOGERROR)

class getUrl(object):
    def __init__(self, url, close=True, proxy=None, post=None, mobile=False, referer=None, cookie=None, output='', timeout='10'):
        if not proxy == None:
            proxy_handler = urllib2.ProxyHandler({'http':'%s' % (proxy)})
            opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookie_handler = urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
            opener = urllib2.install_opener(opener)
        if not post == None:
            request = urllib2.Request(url, post)
        else:
            request = urllib2.Request(url,None)
        if mobile == True:
            request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7')
        else:
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0')
        if not referer == None:
            request.add_header('Referer', referer)
        if not cookie == None:
            request.add_header('cookie', cookie)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        else:
            result = response.read()
        if close == True:
            response.close()
        self.result = result


def myjsunpack(script):
    def __itoa(num, radix):
        result = ""
        while num > 0:
            result = "0123456789abcdefghijklmnopqrstuvwxyz"[num % radix] + result
            num /= radix
        return result

    def __unpack(p, a, c, k, e, d):
        while (c > 1):
            c = c -1
            if (k[c]):
                p = re.sub('\\b' + str(__itoa(c, a)) +'\\b', k[c], p)
        return p

    aSplit = script.split(";',")
    p = str(aSplit[0])
    aSplit = aSplit[1].split(",")
    a = int(aSplit[0])
    c = int(aSplit[1])
    k = aSplit[2].split(".")[0].replace("'", '').split('|')
    e = ''
    d = ''
    sUnpacked = str(__unpack(p, a, c, k, e, d))
    return sUnpacked.replace('\\', '')

def captcha(data):
    try:
        captcha = {}

        def get_response(response):
            try:
                dataPath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo("profile"))
                i = os.path.join(dataPath.decode("utf-8"),'img')
                f = xbmcvfs.File(i, 'w')
                f.write(getUrl(response).result)
                f.close()
                f = xbmcgui.ControlImage(450,5,375,115, i)
                d = xbmcgui.WindowDialog()
                d.addControl(f)
                xbmcvfs.delete(i)
                d.show()
                xbmc.sleep(3000)
                t = 'Type the letters in the image'
                c = common.getUserInput(t, '')
                d.close()
                return c
            except:
                return

        solvemedia = common.parseDOM(data, "iframe", ret="src")
        solvemedia = [i for i in solvemedia if 'api.solvemedia.com' in i]

        if len(solvemedia) > 0:
            url = solvemedia[0]
            result = getUrl(url).result
            challenge = common.parseDOM(result, "input", ret="value", attrs = { "id": "adcopy_challenge" })[0]
            response = common.parseDOM(result, "iframe", ret="src")
            response += common.parseDOM(result, "img", ret="src")
            response = [i for i in response if '/papi/media' in i][0]
            response = 'http://api.solvemedia.com' + response
            response = get_response(response)
            captcha.update({'adcopy_challenge': challenge, 'adcopy_response': response})
            return captcha

        recaptcha = []
        if data.startswith('http://www.google.com'): recaptcha += [data]
        recaptcha += common.parseDOM(data, "script", ret="src", attrs = { "type": "text/javascript" })
        recaptcha = [i for i in recaptcha if 'http://www.google.com' in i]

        if len(recaptcha) > 0:
            url = recaptcha[0]
            result = getUrl(url).result
            challenge = re.compile("challenge\s+:\s+'(.+?)'").findall(result)[0]
            response = 'http://www.google.com/recaptcha/api/image?c=' + challenge
            response = get_response(response)
            captcha.update({'recaptcha_challenge_field': challenge, 'recaptcha_challenge': challenge, 'recaptcha_response_field': response, 'recaptcha_response': response})
            return captcha

        numeric = re.compile("left:(\d+)px;padding-top:\d+px;'>&#(.+?);<").findall(data)

        if len(numeric) > 0:
            result = sorted(numeric, key=lambda ltr: int(ltr[0]))
            response = ''.join(str(int(num[1])-48) for num in result)
            captcha.update({'code': response})
            return captcha

    except:
        return captcha

##OPTIONAL RESOLVERS###################
def resolve_180upload(url):
    try:
        url = re.compile('//.+?/([\w]+)').findall(url)[0]
        url = 'http://180upload.com/embed-%s.html' % url

        result = getUrl(url).result

        post = {}
        f = common.parseDOM(result, "form", attrs = { "id": "captchaForm" })[0]
        k = common.parseDOM(f, "input", ret="name", attrs = { "type": "hidden" })
        for i in k: post.update({i: common.parseDOM(f, "input", ret="value", attrs = { "name": i })[0]})
        post = urllib.urlencode(post)

        result = getUrl(url, post=post).result

        result = re.compile('(eval.*?\)\)\))').findall(result)[-1]
        result = myjsunpack(result)

        url = re.compile("'file' *, *'(.+?)'").findall(result)
        url += re.compile("file *: *'(.+?)'").findall(result)
        url += common.parseDOM(result, "embed", ret="src")
        url = 'http://' + url[-1].split('://', 1)[-1]
        return url
    except:
        return

        
def resolve_movreel(url):
    try:    
        user = settings.getSetting("movreel_user")
        password = settings.getSetting("movreel_password")
        login = 'http://movreel.com/login.html'
        post = {'op': 'login', 'login': user, 'password': password, 'redirect': url}
        post = urllib.urlencode(post)
        result = getUrl(url, close=False).result
        result += getUrl(login, post=post, close=False).result
        post = {}
        f = common.parseDOM(result, "Form", attrs = { "name": "F1" })[-1]
        k = common.parseDOM(f, "input", ret="name", attrs = { "type": "hidden" })
        for i in k: post.update({i: common.parseDOM(f, "input", ret="value", attrs = { "name": i })[0]})
        post.update({'method_free': '', 'method_premium': ''})
        post = urllib.urlencode(post)

        result = getUrl(url, post=post).result

        url = re.compile('(<a .+?</a>)').findall(result)
        url = [i for i in url if 'Download Link' in i][-1]
        url = common.parseDOM(url, "a", ret="href")[0]
        return url
    except:
        return
###END OPTIONAL RESOLVERS####################
    
def grab_cloudflare(url):

    class NoRedirection(urllib2.HTTPErrorProcessor):
        # Stop Urllib2 from bypassing the 503 page.    
        def http_response(self, request, response):
            code, msg, hdrs = response.code, response.msg, response.info()

            return response
        https_response = http_response

    cj = cookielib.CookieJar()
    
    opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36')]
    response = opener.open(url).read()
        
    jschl=re.compile('name="jschl_vc" value="(.+?)"/>').findall(response)
    if jschl:
        import time
        jschl = jschl[0]    
    
        maths=re.compile('value = (.+?);').findall(response)[0].replace('(','').replace(')','')

        domain_url = re.compile('(https?://.+?/)').findall(url)[0]
        domain = re.compile('https?://(.+?)/').findall(domain_url)[0]
        
        time.sleep(5)
        
        normal = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        normal.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36')]
        final= normal.open(domain_url+'cdn-cgi/l/chk_jschl?jschl_vc=%s&jschl_answer=%s'%(jschl,eval(maths)+len(domain))).read()
        
        response = normal.open(url).read()

    return response

def millis():
      import time as time_
      return int(round(time_.time() * 1000))
    
def load_json(data):
      def to_utf8(dct):
            rdct = {}
            for k, v in dct.items() :
                  if isinstance(v, (str, unicode)) :
                        rdct[k] = v.encode('utf8', 'ignore')
                  else :
                        rdct[k] = v
            return rdct
      try :        
            from lib import simplejson
            json_data = simplejson.loads(data, object_hook=to_utf8)
            return json_data
      except:
            try:
                  import json
                  json_data = json.loads(data, object_hook=to_utf8)
                  return json_data
            except:
                  import sys
                  for line in sys.exc_info():
                        print "%s" % line
      return None


        
def resolve_mrfile(url):
    try:
        import jsunpack
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix MR.File - Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        embed=re.findall('<IFRAME SRC="(http://mrfile[^"]+)"',html)
        html = net().http_GET(embed[0]).content
        r = re.findall(r'(eval\(function\(p,a,c,k,e,d\)\{while.+?)</script>',html,re.M|re.DOTALL)
        try:unpack=jsunpack.unpack(r[1])
        except:unpack=jsunpack.unpack(r[0])
        try:stream_url=re.findall('<param name="src"value="(.+?)"/>',unpack)[0]
        except:stream_url=re.findall("file: '([^']+)'",html)[0]
        return stream_url
        if dialog.iscanceled(): return None
    except Exception:
        logerror('**** MR.File Error occured: %s' % e)
        xbmc.executebuiltin('[B][COLOR white]MR.File[/COLOR][/B]','[COLOR red]%s[/COLOR]' % e, 5000, elogo)

  

def resolve_g2g(url):
    html3 = net().http_GET(url).content 
    url2 = re.findall('(?sim)<iframe src="(http://g2g.fm/pasmov3p.php.+?)"', html3)[0]
    req = urllib2.Request(url2)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referer', url)
    response = urllib2.urlopen(req)
    html=response.read()
    response.close()
    phpUrl = re.findall('(?sim)<iframe id="ggplayer" src="(.+?php)"', html)[0]
    req = urllib2.Request(phpUrl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referer', url)   
    response = urllib2.urlopen(req)
    html2=response.read()
    response.close()
    googleUrl = re.findall('(?sim)<iframe src="(.+?preview)"', html2)[0]
    return resolve_googleDocs(googleUrl)
     
def unescapes(text):
    if text:
        rep = {"\u003d":"=","\u0026":"&","u003d":"=","u0026":"&","%26":"&","&#38;":"&","&amp;":"&","&#044;": ",","&nbsp;": " ","\n": "","\t": "","\r": "","%5B": "[","%5D": "]",
               "%3a": ":","%3A":":","%2f":"/","%2F":"/","%3f":"?","%3F":"?","%3d":"=","%3D":"=","%2C":",","%2c":",","%3C":"<",
               "%20":" ","%22":'"',"%3D":"=","%3A":":","%2F":"/","%3E":">","%3B":",","%27":"'","%0D":"","%0A":"","%92":"'",
               "&lt;": "<","&gt;": ">","&quot": '"',"&rsquo;": "'","&acute;": "'"}
        for s, r in rep.items():
            text = text.replace(s, r) 
    #except TypeError: pass
    return text

def resolve_picasaWeb(url):
    run = net().http_GET(url)
    cjList=[]
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler())
    req = urllib2.Request(url)
    f = opener.open(req)
    html = f.read()
    for cookie in cj:
            cjList.append(str(cookie).replace('<Cookie ','').replace(' for picasaweb.google.com/>','').replace('for .google.com/>',''))
    Lid=re.search('https://picasaweb.google.com/(.+?)/.+?authkey=(.+?)#([^<]+)',url)
    url='https://picasaweb.google.com/data/entry/base/user/'+Lid.group(1)+'/photoid/'+Lid.group(3)+'?alt=rss&authkey='+Lid.group(2)
    namelist=[]
    urllist=[]
    dialog = xbmcgui.DialogProgress()
    dialog.create('Resolving', 'Resolving Phoenix  Link...')       
    dialog.update(0)
    print 'Phoenix GoogleDoc - Requesting GET URL: %s' % url
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
    req.add_header('cookie', 'xnfo=1; PREF=ID=85556f1a24007f7a:U=dc2692c0a6061b26:FF=0:LD=en:TM=1373784453:LM=1389395973:GM=1:S=qR9eOdnLEbmW_TLb; HSID=A20CRcfWXDjH2t8pM; SSID=AT-HtXZJKl-_80o2K; APISID=Oxz2q50wC6cLlo6-/AGZzvI9THf_52xvSO; SAPISID=kF1H8rjAwWjKPFU6/AjxdPvG1MVo2oU8aT; lh=DQAAAM4AAACjRFpk1gWTm8hUwNXV8b4iTC6-IIL6RsAD8urndnSZYTYKgkuDD4aOktLrRQXWX4--37oGvyHC4c07ooRuZ0AxVdGINz5UCX5n4-63PwQDpKnqvJnFiv4SaS3UQlLrlXsoeSPDs2-bWOpBNn9b7BCfQr9XJXC5OJrpiDFlKOJ3XIjJ8Kh3M0Z2K84u2k3pb7l2ODvIFGjk38GLmn-gPSHENZEmCgV-KsqpgDTQ0EnPU-h03OHch9xEmof7HD4TzzV71YS5X9hNGbYzp3ux5asE;  '+cjList[1]+'; noRedirect=1; SID=DQAAAMwAAABwVBj_2BKoFX1DvzaYSC2Vd7ieIUcNRpOHAmwDkKE4KEmzBiIUPoGedSnY91jnlOUk7wysRSWIaT_NiI6SfpFHRS9FA59wG7XETqInr0vUA2si8J1IefoooMj6i3JBxdsc6wZ-XUYu57czbICcBshac3_al7xJLQJnGd1kz-2Zxn3IVi3c5sDL21pCc_1SegSDBFughkCAY7p7T8prVX6XLqf_JGv34RIx6pPYZ_emGzjEOVbbjswVvX-9uKLvARvYgsjXseS5k3_TMHNLYQWp; '+cjList[0])
    
    response = urllib2.urlopen(req)
    html=response.read()
    response.close()
    dialog.update(100)
    link2=unescapes(html)
    streams_map = str(link2)
    stream= re.compile("url='(http://redirector.googlevideo.com[^']+)' height='([^']+)'").findall(streams_map)
    for stream_url,stream_quality in reversed(stream):
        stream_url = unescapes(stream_url)
        urllist.append(stream_url)
        stream_qlty = stream_quality.upper()
        if (stream_qlty == '720'):
            stream_qlty = 'HD-720p'
        elif (stream_qlty == '480'):
            stream_qlty = 'SD-480p'
        elif (stream_qlty == '360'):
            stream_qlty = 'SD-360p'
        elif (stream_qlty == '240'):
            stream_qlty = 'SD-240p'
        namelist.append(stream_qlty)
    dialog = xbmcgui.Dialog()
    answer =dialog.select("Quality Select", namelist)
    if answer==-1:
        return
    else:
        return urllist[int(answer)]
    
def resolve_googleDocs(url):
    namelist=[]
    urllist=[]
    dialog = xbmcgui.DialogProgress()
    dialog.create('Resolving', 'Resolving Phoenix  Link...')       
    dialog.update(0)
    print 'Phoenix GoogleDoc - Requesting GET URL: %s' % url
    html = net().http_GET(url).content
    dialog.update(100)
    link2=unescapes(html)
    match= re.compile('url_encoded_fmt_stream_map":"(.+?),"').findall(link2)[0]
    if match:
        streams_map = str(match)
    else:
        streams_map = str(link2)
    stream= re.compile('url=(.+?)&type=.+?&quality=(.+?),').findall(streams_map)
    for stream_url,stream_quality in stream:
        stream_url = stream_url
        stream_url = unescapes(stream_url)
        urllist.append(stream_url)
        stream_qlty = stream_quality.upper()
        if (stream_qlty == 'hd1080'):
            stream_qlty = 'HD-1080p'
        elif (stream_qlty == 'hd720'):
            stream_qlty = 'HD-720p'
        elif (stream_qlty == 'latge'):
            stream_qlty = 'SD-480p'
        elif (stream_qlty == 'medium'):
            stream_qlty = 'SD-360p'
        namelist.append(stream_qlty)
    dialog = xbmcgui.Dialog()
    answer =dialog.select("Quality Select", namelist)
    if answer==-1:
        return
    else:
        return urllist[int(answer)]

def resolve_firedrive(url):
    try:
        url=url.replace('putlocker.com','firedrive.com').replace('putlocker.to','firedrive.com')
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Firedrive - Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        dialog.update(50)
        if dialog.iscanceled(): return None
        post_data = {}
        r = re.findall(r'(?i)<input type="hidden" name="(.+?)" value="(.+?)"', html)
        for name, value in r:
            post_data[name] = value
        post_data['referer'] = url
        html = net().http_POST(url, post_data).content
        print html
        embed=re.findall('(?sim)href="([^"]+?)">Download file</a>',html)
        if not embed:
            embed=re.findall("(?sim)'(http://dl.firedrive.com/[^']+?)'",html)
        if dialog.iscanceled(): return None
        if embed:
            dialog.update(100)
            return embed[0]
        else:
            #logerror('Phoenix: Resolve Firedrive - File Not Found')
            #xbmc.executebuiltin("XBMC.Notification(File Not Found,Firedrive,2000)")
            return False
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,FireDrive,2000)")





def resolve_yify(url):
    try:
        referer = url
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Yify - Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        url = re.compile('showPkPlayer[(]"(.+?)"[)]').findall(html)[0]
        key=url
        url = 'http://yify.tv/reproductor2/pk/pk/plugins/player_p2.php?url=' + url
        print url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
        req.add_header('Referer', referer)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        print link
        
        if 'captcha' in link:
            print link
            captcha=re.search('{"captcha":(.+?),"k":"([^"]+)"}',link)
            curl='http://www.google.com/recaptcha/api/challenge?k='+captcha.group(2)+'&ajax=1&cachestop=0.7698786298278719'
            html = net().http_GET(curl).content
            print html
            image_id=re.findall("challenge : '([^']+)'",html)
            img_id=image_id[0]
            image_url='http://www.google.com/recaptcha/api/image?c='+img_id
            img = xbmcgui.ControlImage(450,15,400,130, image_url)
            wdlg = xbmcgui.WindowDialog()
            wdlg.addControl(img)
            wdlg.show()
        
            kb = xbmc.Keyboard('', 'Type the letters in the image', False)
            kb.doModal()
            capcode = kb.getText()
   
            if (kb.isConfirmed()):
                userInput = kb.getText()
                if userInput != '':
                    solution = kb.getText()
                elif userInput == '':
                    xbmc.executebuiltin('big', 'No text entered', 'You must enter text in the image to access video', '')
                    return False
            else:
                return False
               
            wdlg.close()
            url = 'http://yify.tv/reproductor2/pk/pk/plugins/player_p2.php'
            user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
            values = {'url' : key,'chall' : img_id,'type' :  captcha.group(1),'res':solution,'':'','':''}
            headers = { 'User-Agent' : user_agent,'Referer':'referer'}

            data = urllib.urlencode(values)
            req = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(req)
            link = response.read()
        if '.pdf' in link:
            html = re.findall('{"url":"([^"]+.pdf)",',link)[0]
        else:
            html = re.compile('{"url":"([^"]+)"').findall(link)[1]
        stream_url = html
        return stream_url
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,YiFi,2000)")


def resolve_VK(url):
    try:
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix Link...')       
        dialog.update(0)
        print 'Phoenix VK - Requesting GET URL: %s' % url
        useragent='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'
        link2 = net(user_agent=useragent).http_GET(url).content
        if re.search('This video has been removed', link2, re.I):
            logerror('***** Phoenix VK - This video has been removed')
            xbmc.executebuiltin("XBMC.Notification(This video has been removed,VK,2000)")
            return Fals
        urllist=[]
        quaList=[]
        match=re.findall('(?sim)<source src="([^"]+)"',link2)
        for url in match:
            print url
            urllist.append(url)
            qua=re.findall('(?sim).(\d+).mp4',url)
            quaList.append(str(qua[0]))
        dialog2 = xbmcgui.Dialog()
        ret = dialog2.select('[COLOR=FF67cc33][B]Select Quality[/COLOR][/B]',quaList)
        if ret == -1:
            return False
        stream_url = urllist[ret]
        if match: 
            return stream_url.replace("\/",'/')
    except Exception:
        #logerror('**** VK Error occured: %s' % e)
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,VK,2000)")

def resolve_youwatch(url):
    try:
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Youwatch - Requesting GET URL: %s' % url
        if 'embed' not in url:
            mediaID = re.findall('http://youwatch.org/([^<]+)', url)[0]
            url='http://youwatch.org/embed-'+mediaID+'.html'
        else:url=url
        html = net().http_GET(url).content
        try:
                html=html.replace('|','/')
                stream=re.compile('/mp4/video/(.+?)/(.+?)/(.+?)/setup').findall(html)
                for id,socket,server in stream:
                    continue
        except:
                raise ResolverError('This file is not available on',"Youwatch")
        stream_url='http://'+server+'.youwatch.org:'+socket+'/'+id+'/video.mp4?start=0'
        return stream_url
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,YouWatch,2000)")

def resolve_projectfreeupload(url):
    try:
        import jsunpack
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Project Free - Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        r = re.findall(r'\"hidden\"\sname=\"?(.+?)\"\svalue=\"?(.+?)\"\>', html, re.I)
        post_data = {}
        for name, value in r:
            post_data[name] = value
        post_data['referer'] = url
        post_data['method_premium']=''
        post_data['method_free']=''
        html = net().http_POST(url, post_data).content
        embed=re.findall('<IFRAME SRC="(.+?)"',html)
        html = net().http_GET(embed[0]).content
        r = re.findall(r'(eval\(function\(p,a,c,k,e,d\)\{while.+?)</script>',html,re.M|re.DOTALL)
        try:unpack=jsunpack.unpack(r[1])
        except:unpack=jsunpack.unpack(r[0])
        stream_url=re.findall('<param name="src"value="(.+?)"/>',unpack)[0]
        return stream_url
        if dialog.iscanceled(): return None
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Project Free,2000)")

def resolve_videomega(url):
    try:
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Videomega - Requesting GET URL: %s' % url
        try:
            mediaID = re.findall('http://videomega.tv/.?ref=([^<]+)', url)[0]
            url='http://videomega.tv/iframe.php?ref='+mediaID
        except:url=url
        html = net().http_GET(url).content
        try:
                encodedurl=re.compile('unescape.+?"(.+?)"').findall(html)
        except:
                raise ResolverError('This file is not available on',"VideoMega")
        url2=urllib.unquote(encodedurl[0])
        stream_url=re.compile('file: "(.+?)"').findall(url2)[0]
        return stream_url
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Video Mega,2000)")
    
def resolve_vidspot(url):
    try:
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        print 'Phoenix Vidspot - Requesting GET URL: %s' % url
        mediaID=re.findall('http://vidspot.net/([^<]+)',url)[0]
        url='http://vidspot.net/embed-'+mediaID+'.html'
        print url
        html = net().http_GET(url).content
        r = re.search('"file" : "(.+?)",', html)
        if r:
            stream_url = urllib.unquote(r.group(1))

        return stream_url

    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,VidSpot,2000)")
        


def resolve_megarelease(url):
    try:
        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')
        dialog.update(0)
        
        print 'MegaRelease Phoenix - Requesting GET URL: %s' % url
        html = net().http_GET(url).content

        dialog.update(50)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            logerror('***** MegaRelease - Site reported maintenance mode')
            xbmc.executebuiltin("XBMC.Notification(File is currently unavailable,MegaRelease in maintenance,2000)")                                
            return False
        if re.search('<b>File Not Found</b>', html):
            logerror('Phoenix: Resolve MegaRelease - File Not Found')
            xbmc.executebuiltin("XBMC.Notification(File Not Found,MegaRelease,2000)")
            return False

        filename = re.search('You have requested <font color="red">(.+?)</font>', html).group(1)
        filename = filename.split('/')[-1]
        extension = re.search('(\.[^\.]*$)', filename).group(1)
        guid = re.search('http://megarelease.org/(.+)$', url).group(1)
        
        vid_embed_url = 'http://megarelease.org/vidembed-%s%s' % (guid, extension)
        UserAgent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
        ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        request = urllib2.Request(vid_embed_url)
        request.add_header('User-Agent', UserAgent)
        request.add_header('Accept', ACCEPT)
        request.add_header('Referer', url)
        response = urllib2.urlopen(request)
        redirect_url = re.search('(http://.+?)video', response.geturl()).group(1)
        download_link = redirect_url + filename
        
        dialog.update(100)

        return download_link
        
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,MegaRelease,2000)")
    finally:
        dialog.close()
        
def setCookie(url):

        
    username = settings.getSetting('vhd_user')
    password = settings.getSetting('vhd_pass')
    cookieExpired = False
    name = "veeHD"
    userName = username
    ref = 'http://veehd.com'
    submit = 'Login'
    terms = 'on'
    remember_me = 'on'
    net().http_GET(url)
    net().http_POST('http://veehd.com/login',{'ref': ref, 'uname': userName, 'pword': password, 'submit': submit, 'terms': terms,'remember_me':remember_me})

        
def resolve_veehd(url):
    if settings.getSetting('vhd_account') == 'false':
                dialog = xbmcgui.Dialog()
                ok = dialog.ok('VEE HD Account Login Not Enabled', '            Please Choose Vee HD Account Tab and Enable')
                if ok:
                        LogNotify('Vee HD Account Tab ', 'Please Enable Account', '5000', '')        
                        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
                        addon.show_settings()
    
    try:
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        if dialog.iscanceled(): return False
        dialog.update(33)
        headers = {}
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7','Referer':url}
        print 'Phoenix VeeHD - Requesting GET URL: %s' % url
        setCookie('http://veehd.com')
        html = net().http_GET(url, headers).content
        if dialog.iscanceled(): return False
        dialog.update(66)
        fragment = re.findall('playeriframe".+?attr.+?src : "(.+?)"', html)
        for frags in fragment:
            pass
        frag = 'http://%s%s'%('veehd.com',frags)
        setCookie('http://veehd.com')
        html = net().http_GET(frag, headers).content
        va=re.search('iframe" src="([^"]+?)"',html)
        if va:
            poop='http://veehd.com'+va.group(1)
            headers = {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7','Referer':frag,'Cache-Control':'max-age=0'}
            setCookie(poop)
            html = net().http_GET(frag, headers).content
        r = re.search('"video/divx" src="(.+?)"', html)
        if r:
            stream_url = r.group(1)
        if not r:
            a = re.search('"url":"(.+?)"', html)
            if a:
                r=urllib.unquote(a.group(1))
                if r:
                    stream_url = r
                else:
                    logerror('***** VeeHD - File Not Found')
                    xbmc.executebuiltin("XBMC.Notification(File Not Found,VeeHD,2000)")
                    return False
            if not a:
                a = re.findall('href="(.+?)">', html)
                stream_url = a[1]
        if dialog.iscanceled(): return False
        dialog.update(100)
        return stream_url
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,VeeHD,2000)")


                


def resolve_epicshare(url):
    try:
        puzzle_img = os.path.join(datapath, "epicshare_puzzle.png")
        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')
        dialog.update(0)
        
        print 'EpicShare - Phoenix Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        if dialog.iscanceled(): return False
        dialog.update(50)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            logerror('***** EpicShare - Site reported maintenance mode')
            xbmc.executebuiltin("XBMC.Notification(File is currently unavailable,EpicShare in maintenance,2000)")  
            return False
        if re.search('<b>File Not Found</b>', html):
            logerror('***** EpicShare - File not found')
            xbmc.executebuiltin("XBMC.Notification(File Not Found,EpicShare,2000)")
            return False

        data = {}
        r = re.findall(r'type="hidden" name="(.+?)" value="(.+?)">', html)

        if r:
            for name, value in r:
                data[name] = value
        else:
            logerror('***** EpicShare - Cannot find data values')
            raise Exception('Unable to resolve EpicShare Link')
        
        #Check for SolveMedia Captcha image
        solvemedia = re.search('<iframe src="(http://api.solvemedia.com.+?)"', html)

        if solvemedia:
           dialog.close()
           html = net().http_GET(solvemedia.group(1)).content
           hugekey=re.search('id="adcopy_challenge" value="(.+?)">', html).group(1)
           open(puzzle_img, 'wb').write(net().http_GET("http://api.solvemedia.com%s" % re.search('<img src="(.+?)"', html).group(1)).content)
           img = xbmcgui.ControlImage(450,15,400,130, puzzle_img)
           wdlg = xbmcgui.WindowDialog()
           wdlg.addControl(img)
           wdlg.show()
        
           kb = xbmc.Keyboard('', 'Type the letters in the image', False)
           kb.doModal()
           capcode = kb.getText()
   
           if (kb.isConfirmed()):
               userInput = kb.getText()
               if userInput != '':
                   solution = kb.getText()
               elif userInput == '':
                   Notify('big', 'No text entered', 'You must enter text in the image to access video', '')
                   return False
           else:
               return False
               
           wdlg.close()
           dialog.create('Resolving', 'Resolving Phoenix  Link...') 
           dialog.update(50)
           if solution:
               data.update({'adcopy_challenge': hugekey,'adcopy_response': solution})

        print 'EpicShare - Phoenix Requesting POST URL: %s' % url
        html = net().http_POST(url, data).content
        if dialog.iscanceled(): return False
        dialog.update(100)
        
        link = re.search('<a id="lnk_download"  href=".+?product_download_url=(.+?)">', html)
        if link:
            print 'Phoenix EpicShare Link Found: %s' % link.group(1)
            return link.group(1)
        else:
            xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Epic Share,2000)")
        
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Epic Share,2000)")
    finally:
        dialog.close()

def resolve_lemupload(url):
    try:
        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
#         
        print 'LemUpload - Phoenix Requesting GET URL: %s' % url
        html = net().http_GET(url).content
        if dialog.iscanceled(): return False
        dialog.update(50)
        
        #Check page for any error msgs
        if re.search('<b>File Not Found</b>', html):
            print '***** LemUpload - File Not Found'
            xbmc.executebuiltin("XBMC.Notification(File Not Found,LemUpload,2000)")
            return False
        
        if re.search('This server is in maintenance mode', html):
            print '***** LemUpload - Server is in maintenance mode'
            xbmc.executebuiltin("XBMC.Notification(Site In Maintenance,LemUpload,2000)")
            return False

        filename = re.search('<h2>(.+?)</h2>', html).group(1)
        extension = re.search('(\.[^\.]*$)', filename).group(1)
        guid = re.search('http://lemuploads.com/(.+)$', url).group(1)
        vid_embed_url = 'http://lemuploads.com/vidembed-%s%s' % (guid, extension)
        request = urllib2.Request(vid_embed_url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')
        request.add_header('Referer', url)
        response = urllib2.urlopen(request)
        if dialog.iscanceled(): return False
        dialog.update(100)
        link = response.geturl()
        if link:
            redirect_url = re.search('(http://.+?)video', link)
            if redirect_url:
                link = redirect_url.group(1) + filename
            print 'Phoenix LemUpload Link Found: %s' % link
            return  link
        else:
            
            raise Exception('Unable to resolve LemUpload Link')

    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Lem Upload,2000)")
    finally:
        dialog.close()
        
def resolve_hugefiles(url):
    import jsunpack
    try:
        import time
        puzzle_img = os.path.join(datapath, "hugefiles_puzzle.png")
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Phoenix  Link...')       
        dialog.update(0)
        html = net().http_GET(url).content
        r = re.findall('File Not Found',html)
        if r:
            xbmc.log('Phoenix: Resolve HugeFiles - File Not Found or Removed', xbmc.LOGERROR)
            xbmc.executebuiltin("XBMC.Notification(File Not Found or Removed,HugeFiles,2000)")
            return False
        data = {}
        r = re.findall(r'type="hidden" name="(.+?)"\s* value="?(.+?)">', html)
        for name, value in r:
            data[name] = value
            data.update({'method_free':'Free Download'})
        if data['fname'] and re.search('\.(rar|zip)$', data['fname'], re.I):
            dialog.update(100)
            logerror('Phoenix: Resolve HugeFiles - No Video File Found')
            xbmc.executebuiltin("XBMC.Notification(No Video File Found,HugeFiles,2000)")
            return False
        if dialog.iscanceled(): return False
        dialog.update(33)
        #Check for SolveMedia Captcha image
        solvemedia = re.search('<iframe src="(http://api.solvemedia.com.+?)"', html)
        recaptcha = re.search('<script type="text/javascript" src="(http://www.google.com.+?)">', html)
    
        if solvemedia:
            html = net().http_GET(solvemedia.group(1)).content
            hugekey=re.search('id="adcopy_challenge" value="(.+?)">', html).group(1)
            open(puzzle_img, 'wb').write(net().http_GET("http://api.solvemedia.com%s" % re.search('img src="(.+?)"', html).group(1)).content)
            img = xbmcgui.ControlImage(450,15,400,130, puzzle_img)
            wdlg = xbmcgui.WindowDialog()
            wdlg.addControl(img)
            wdlg.show()
            
            xbmc.sleep(3000)
    
            kb = xbmc.Keyboard('', 'Type the letters in the image', False)
            kb.doModal()
            capcode = kb.getText()
       
            if (kb.isConfirmed()):
                userInput = kb.getText()
                if userInput != '':
                    solution = kb.getText()
                elif userInput == '':
                    xbmc.executebuiltin("XBMC.Notification(No text entered, You must enter text in the image to access video,2000)")
                    return False
            else:
                return False
                   
            wdlg.close()
            dialog.update(66)
            if solution:
                data.update({'adcopy_challenge': hugekey,'adcopy_response': solution})

        elif recaptcha:
            html = net().http_GET(recaptcha.group(1)).content
            part = re.search("challenge \: \\'(.+?)\\'", html)
            captchaimg = 'http://www.google.com/recaptcha/api/image?c='+part.group(1)
            img = xbmcgui.ControlImage(450,15,400,130,captchaimg)
            wdlg = xbmcgui.WindowDialog()
            wdlg.addControl(img)
            wdlg.show()
        
            time.sleep(3)
        
            kb = xbmc.Keyboard('', 'Type the letters in the image', False)
            kb.doModal()
            capcode = kb.getText()
        
            if (kb.isConfirmed()):
                userInput = kb.getText()
                if userInput != '':
                    solution = kb.getText()
                elif userInput == '':
                    raise Exception ('You must enter text in the image to access video')
            else:
                raise Exception ('Captcha Error')
            wdlg.close()
            dialog.update(66)
            data.update({'recaptcha_challenge_field':part.group(1),'recaptcha_response_field':solution})

        else:
            captcha = re.compile("left:(\d+)px;padding-top:\d+px;'>&#(.+?);<").findall(html)
            result = sorted(captcha, key=lambda ltr: int(ltr[0]))
            solution = ''.join(str(int(num[1])-48) for num in result)
            dialog.update(66)
            data.update({'code':solution})
        html = net().http_POST(url, data).content
        if dialog.iscanceled(): return False
        if 'reached the download-limit' in html:
            
            xbmc.executebuiltin("XBMC.Notification(Daily Limit Reached,HugeFiles,2000)")
            return False
        r = re.findall('var fileUrl = "([^"]+)"', html, re.DOTALL + re.IGNORECASE)
        if r:
            dialog.update(100)
            return r[0]
        if not r:
            sPattern = '''<div id="player_code">.*?<script type='text/javascript'>(eval.+?)</script>'''
            jpack = re.findall(sPattern, html, re.DOTALL|re.I)
            if jpack:
                dialog.update(100)
                sUnpacked = jsunpack.unpack(jpack[0])
                sUnpacked = sUnpacked.replace("\\'","")
                r = re.findall('file,(.+?)\)\;s1',sUnpacked)
                if not r:
                  r = re.findall('"src"value="(.+?)"/><embed',sUnpacked)
                return r[0]
            else:
                logerror('***** HugeFiles - Cannot find final link')
                raise Exception('Unable to resolve HugeFiles Link')
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Huge Files,2000)")        


def resolve_billionuploads(url):
    try:
        import cookielib
        cj = cookielib.CookieJar()

        agent = 'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0'
        base = 'http://billionuploads.com'

        class NoRedirection(urllib2.HTTPErrorProcessor):
            def http_response(self, request, response):
                return response

        opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent', agent)]
        response = opener.open(base)
        response = opener.open(base)
        result = response.read()

        z = []
        decoded = re.compile('(?i)var z="";var b="([^"]+?)"').findall(result)[0]
        for i in range(len(decoded)/2): z.append(int(decoded[i*2:i*2+2],16))
        decoded = ''.join(map(unichr, z))

        incapurl = re.compile('(?i)"GET","(/_Incapsula_Resource[^"]+?)"').findall(decoded)[0]
        incapurl = base + incapurl

        response = opener.open(incapurl)
        response = opener.open(url)
        result = response.read()

        post = {}
        f = common.parseDOM(result, "form", attrs = { "method": "post" })[-1]
        k = common.parseDOM(f, "input", ret="name", attrs = { "type": "hidden" })
        for i in k: post.update({i: common.parseDOM(f, "input", ret="value", attrs = { "name": i })[0]})
        post.update({'method_free': 'Download or watch'})
        post = urllib.urlencode(post)

        response = opener.open(url, post)
        result = response.read()
        response.close()

        url = common.parseDOM(result, "a", ret="href", attrs = { "class": "download" })[0]
        return url
    except:
        return

###Original Mail.ru#######################################################
def resolve_mailru(url):
    try:
        url = url.replace('.html','.json?ver=0.2.60').replace('embed/','')
        max=0
        link = requests.get(url).content
        cookielink = requests.get(url)
        setcookie = cookielink.headers['Set-Cookie']
        match=re.compile('"key":"(.+?)","url":"(.+?)"').findall(link)
        for q,url in match:
            quality=int(q.replace('p',''))
            if quality > max:
                max=quality
                playlink="%s|Cookie=%s" % (url,urllib.quote(setcookie))
        return playlink
    except Exception:
        
        xbmc.executebuiltin("XBMC.Notification(Resolver Failed,Internal Resolver,2000)")

#########END ORIGINAL MAIL>RU################################
def LIVERESOLVE(name,url,thumb):
         print "THUMBNAIL IS " +thumb
         params = {'url':url, 'name':name, 'thumb':thumb}
         addon.add_video_item(params, {'title':name}, img=thumb)
         liz=xbmcgui.ListItem(name, iconImage=thumb, thumbnailImage=thumb)
         xbmc.Player ().play(str(url), liz, False)
         return   

               
#########################Blazetamer's VeeHD  Module########################################




def VHDLOGIN():
    username = settings.getSetting('vhd_user')
    password = settings.getSetting('vhd_pass')    
    header_dict = {}
    header_dict['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    header_dict['Connection'] = 'keep-alive'
    header_dict['Content-Type'] = 'application/x-www-form-urlencoded'
    header_dict['Host'] = 'veehd.com'
    header_dict['Referer'] = 'http://veehd/'
    header_dict['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36'    
    form_data = {'ref':'http://veehd.com/login','uname':username, 'pword':password,'submit':'Login', 'terms':'on','remember_me':'on'}
    net.set_cookies(cookiejar)
    login = net.http_POST('http://veehd/', form_data=form_data, headers=header_dict)
    net.save_cookies(cookiejar)
    link = net.http_GET('http://veehd.com').content
    logincheck=re.compile('<h3><a href="/dashboard">My (.+?)</a></h3>').findall(link)
    for nolog in logincheck:
                    print 'Login Check Return is ' + nolog
                    if 'Dashboard' in nolog :
                        LogNotify('Login Failed at VeeHD', 'Check settings', '5000', '')
                        return True
    else:
                        LogNotify('Welcome Back ' + username, 'Enjoy your stay!', '5000', '')
                        net.save_cookies(cookiejar)
                        return False
  

        
def VHDSTARTUP():
        username = settings.getSetting('vhd_user')
        password = settings.getSetting('vhd_pass')
        cookiejar = addon.get_profile()
        cookiejar = os.path.join(cookiejar,'cookies.lwp')
        if username is '' or password is '':
                dialog = xbmcgui.Dialog()
                ok = dialog.ok('Username or Password Not Set', '            Please Choose VeeHD Account Tab and Set')
                if ok:
                        LogNotify('VeeHD Account Tab ', 'Please set Username & Password!', '5000', '')        
                        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
                        addon.show_settings()
        


        VHDLOGIN()      
                       
        
#************************End Login**************************************
