import urllib2,xbmc,xbmcaddon,os

PLUGIN='plugin.video.streamtvbox'
ADDON = xbmcaddon.Addon(id=PLUGIN)
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
world=os.path.join(datapath, "world")
pak=os.path.join(datapath, "pak")
if os.path.exists(datapath) == False:
        os.makedirs(datapath)
try:
    req = urllib2.Request('http://worldtvpro.zapto.org/cms/cms/jklmnop.php')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referrer', 'http://adstreams.dynns.com/apps/service_files/live_tv_pakinida2.1.php')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    f = open(world, mode='w')
    f.write(link)
    f.close()
except:pass

try:
    req = urllib2.Request('http://www.softmagnate.com/CMS-Server-Pak-Hind-HD/getJson.php')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referrer', 'http://adstreams.dynns.com/apps/service_files/live_tv_pakinida2.1.php')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    f = open(pak, mode='w')
    f.write(link)
    f.close()
except:pass
