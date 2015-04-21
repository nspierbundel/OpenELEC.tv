import urllib2,xbmc,xbmcaddon,os

PLUGIN='plugin.video.mikeytv'
ADDON = xbmcaddon.Addon(id=PLUGIN)
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
world=os.path.join(datapath, "world")
if os.path.exists(datapath) == False:
        os.makedirs(datapath)
try:
    req = urllib2.Request('http://worldtvpro.zapto.org/cms/cms/jklmnop.php')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    f = open(world, mode='w')
    f.write(link)
    f.close()
except:pass
