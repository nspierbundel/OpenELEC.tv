import urllib, urllib2, requests
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import os, sys, re, time
import extract, utils, favourite
import xml.etree.ElementTree as ET



BASEURL             = 'http://addons.totalxbmc.tv/'
ADDON_ID            = 'plugin.program.tlbb.content'
ADDON               = xbmcaddon.Addon(id=ADDON_ID)
HOME                = ADDON.getAddonInfo('path')
FILENAME            = utils.FILENAME
FANART              = os.path.join(xbmc.translatePath('special://home/'), 'addons/tlbb-master/extras/bg/default.jpg')
FANART              = utils.FANART
XML_EXPRESSION_ITEM = '<item><id>(.+?)</id><title>(.+?)</title><icon>(.+?)</icon><repoLink>(.+?)</repoLink><pluginLink>(.+?)</pluginLink><cmd>(.+?)</cmd><thumbnail>(.+?)</thumbnail><rating>(.+?)</rating><type>(.+?)</type><description>(.+?)/|^$</description></item>'
XML_EXPRESSION_DIR  = '<dir><title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></dir>'

def download(url, dest, dp = None):

    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Status...", "Checking Installation", ' ', ' ')

    dp.update(0)
    urllib.urlretrieve(url, dest, lambda nb, bs, fs, url=url: _pbhook(nb, bs, fs, url, dp))

def _pbhook(numblocks, blocksize, filesize, url, dp):

    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)

    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()

def addDir(name, url, mode, iconimage=''): 
    if len(iconimage) > 0:
        iconimage = FANART

    else:
        iconimage = 'DefaultFolder.png'

    if url.lower() != 'none':
        if not url.startswith(BASEURL):
            url = BASEURL + url
            
    u   = "plugin://plugin.program.tlbb.content/"
    u  += "?url="  + urllib.quote_plus(url)
    u  += "&name=" + urllib.quote_plus(name)
    u  += "&mode=" + str(mode)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setProperty("Fanart_Image", FANART)
    addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

def AUTO_VIEW(content = ''):
    if not content:
        return

    xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view') != 'true':
        return

    if content == 'addons':
        xbmc.executebuiltin("Container.SetViewMode(58)")
    else:
        xbmc.executebuiltin("Container.SetViewMode(58)")

def addDirectoryItem(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder)
    

def addHELPDir(name, url, mode, iconimage, fanart, description, filetype, repourl='', version='', author=''):
        u  = "plugin://plugin.program.tlbb.content/"
        u += "?url="         + urllib.quote_plus(url)
        u += "&name="        + urllib.quote_plus(name)
        u += "&filetype="    + urllib.quote_plus(filetype)
        u += "&repourl="     + urllib.quote_plus(repourl)
        u += "&mode="        + str(mode)
                        
        liz = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ 'title': name, 'plot': description })
        liz.setProperty('Fanart_Image', fanart)
        liz.setProperty('Addon.Description', description)

        addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

def add2HELPItem(id, name, url, cmd, mode, iconimage, fanart, description, filetype, rating, isFolder=True):
        u = "plugin://plugin.program.tlbb.content/"
        u += "?url=" + urllib.quote_plus(url)
        u += "&id=" + urllib.quote_plus(id)
        u += "&name=" + urllib.quote_plus(name)
        u += "&filetype=" + urllib.quote_plus(filetype)
        u += "&mode=" + str(mode)
        u += "&description=" + urllib.quote_plus(description)
        u += "&rating="      + str(rating)
        
        liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

        liz.setInfo(type="Video", infoLabels={ "label": name, "title": name, "Plot": description, "cmd": cmd , 'rating': rating})
        liz.setProperty("Fanart_Image", fanart)

        addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def add2HELPDir(name, url, mode, iconimage, fanart, filetype, isFolder=True):
        u  = "plugin://plugin.program.tlbb.content/"
        u += "?url="         + urllib.quote_plus(url)
        u += "&name="        + urllib.quote_plus(name)
        u += "&filetype="    + urllib.quote_plus(filetype)
        u += "&mode="        + str(mode)
        
        liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

        liz.setInfo(type="Video", infoLabels={ "label": name, "title": name})
        liz.setProperty("Fanart_Image", fanart)

        addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def OPEN_URL(url):
    link = requests.get(url).text
    return link.replace('\r', '').replace('\n', '').replace('\t', '')

def checkRepo(url,dp):
    newfile   = url.rsplit('/',1)[1]
    newfile   = newfile.rsplit('?',1)[0]
    reponame  = newfile.rsplit('.',1)[0]
    try:
        reponame = str(reponame).split('-')[0]
    except:
        reponame = str(reponame)
    current, dirs, files = os.walk(xbmc.translatePath('special://home/addons')).next()

    for dir in dirs:
        #zipfile already exist
        if dir == reponame:
            #Repo already exist
            return
        
    #Repo installation
    path = xbmc.translatePath(os.path.join('special://home/addons', 'packages'))
    lib  = os.path.join(path, newfile)

    download(url, lib, dp)
    
    addonfolder = xbmc.translatePath(os.path.join('special://', 'home/addons'))
    time.sleep(2)
    extract.all(lib, addonfolder, dp)
    return

def ADDONINSTALL(name, url, cmd, filetype, repourl, fav_path):
    try:
        confirm = xbmcgui.Dialog().yesno('Please Confirm', '                Do you wish to install the chosen add-on and', '                        its respective repository if needed?', '                    ', 'Cancel', 'Install')  

        #On cancel
        if confirm == 0:
            url  = utils.getUrl()
            tags = utils.getTag()
            type = utils.getType()

            if type == "Official":
                mode = "official"
                ADDONLIST(url, mode,tags)
            elif type == "UnOfficial":
                mode = "unofficial"
                ADDONLIST(url, mode,tags)

        #On install
        elif confirm == 1:
            
            dp = xbmcgui.DialogProgress()
            dp.create('Download Progress:', 'Downloading repo...', '', 'Please Wait')
            
            if url != 'XBMC':
                checkRepo(url,dp)
    
            #Addon installation
            xml_url = utils.getUrl()
            link    = OPEN_URL(xml_url)
            match   = re.compile(XML_EXPRESSION_ITEM).findall(link)

            for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in match:
                if title == name:
                    addon_url = pluginlink

            newfile   = addon_url.rsplit('/',1)[1]
            newfile   = newfile.rsplit('?',1)[0]
            try:
                version   = newfile.rsplit('-',1)[1].rsplit('.',1)[0]
            except:
                #version is not available
                pass
            addonname = newfile.rsplit('-', 1)[0]
            addonname = str(addonname)
            addonname = addonname.replace('[', '')
            addonname = addonname.replace(']', '')
            addonname = addonname.replace('"', '')
            addonname = addonname.replace('[', '')
            addonname = addonname.replace("'", '')

            path = xbmc.translatePath(os.path.join('special://home/addons', 'packages'))
            current, dirs, files = os.walk(xbmc.translatePath('special://home/addons')).next()

            for dir in dirs:
                #zipfile already exist
                if dir == addonname:
                    addon_path      = os.path.join(xbmc.translatePath('special://home/addons'),addonname)
                    addon_xml       = os.path.join(addon_path,'addon.xml')
                    tree            = ET.parse(addon_xml)
                    root            = tree.getroot()
                    existingVersion = root.attrib.get('version')

                    if existingVersion == version:
                        addon_cmd = ''
                        xml_url   = utils.getUrl()
                        link      = OPEN_URL(xml_url)
                        match     = re.compile(XML_EXPRESSION_ITEM).findall(link)

                        for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in match:
                            if title == name:
                                addon_cmd = cmd

                        icon_path   = os.path.join(xbmc.translatePath('special://home/addons'),os.path.join(addonname,'icon.png'))
                        fanart_path = os.path.join(xbmc.translatePath('special://home/addons'),os.path.join(addonname,'fanart.jpg'))
                        if not os.path.exists(fanart_path):
                            fanart_path = FANART 
                        copy = []
                        copy.append(name)
                        copy.append(icon_path)
                        copy.append(fanart_path)
                        copy.append(addon_cmd)
                        fav_file = os.path.join(fav_path, FILENAME)
                        favourite.copyFave(fav_file, copy)
        
                        #xbmcgui.Dialog().ok('Installed','Now you can use it directly from current folder')
                        return 1
                
            #zipfile not found
            lib = os.path.join(path, newfile)
            dp.update(0, 'Downloading plugin...')

            download(addon_url, lib, dp)

            if filetype == 'addon':
                addonfolder = xbmc.translatePath(os.path.join('special://', 'home/addons'))
            elif filetype == 'media':
                addonfolder = xbmc.translatePath(os.path.join('special://', 'home'))    
            elif filetype == 'main':
                addonfolder = xbmc.translatePath(os.path.join('special://', 'home'))
            time.sleep(2)

            addonname = extract.all(lib, addonfolder, dp)
            
            addon_cmd = ''                
            xml_url   = utils.getUrl()
            link      = OPEN_URL(xml_url)
            match     = re.compile(XML_EXPRESSION_ITEM).findall(link)

            for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in match:
                if title == name:
                    addon_cmd = cmd                    

            icon_path = os.path.join(addonfolder, os.path.join(addonname, 'icon.png'))
            fanart_path = os.path.join(xbmc.translatePath('special://home/addons'), os.path.join(addonname, 'fanart.jpg'))
            if not os.path.exists(fanart_path):
                fanart_path = FANART 
            copy = []
            copy.append(name)
            copy.append(icon_path)
            copy.append(fanart_path)
            copy.append(addon_cmd)
            fav_file = os.path.join(fav_path, FILENAME)
            favourite.copyFave(fav_file, copy)
            
            #Updated plugin
            addon_path = os.path.join(xbmc.translatePath('special://home/addons'),addonname)
            addon_xml  = os.path.join(addon_path,'addon.xml')            
            tree       = ET.parse(addon_xml)
            root       = tree.getroot()
            exVersion  = root.attrib.get('version')
            digits     = exVersion.rsplit('.')
            newVersion = ''

            #if int(digits[2]) != 0:
            #    newVersion = exVersion.rsplit('.',1)[0] + '.0'
            #elif int(digits[1]) != 0:
            #    newVersion = exVersion.split('.',1)[0] + '.0.0'
            #else:
            #    newVersion = '0.0.0'

            newVersion = '0.0.0'
            root.set('version', newVersion)
            tree.write(addon_xml)
    
            #xbmc.executebuiltin( 'UpdateLocalAddons' )
            #xbmc.executebuiltin( 'UpdateAddonRepos' )            
            #xbmcgui.Dialog().ok('Installed','Now you can use it directly from current folder')

            #updatePath = xbmc.translatePath('special://home/addons/plugin.program.tlbb.content/addonUpdate.py')
            #xbmc.executebuiltin( "RunScript(" + updatePath + ")")            
            
            return 1
    
    except Exception as e:
        xbmcgui.Dialog().ok('Error','Installation failed')

        path      = utils.getCurrentPath()
        thepath   = xbmc.translatePath(path)
        label     = os.path.basename(thepath)
        link      = "ReplaceWindow(10001,%s?label=%s&mode=%d&path=%s)" % (sys.argv[0] , label, 400, urllib.quote_plus(thepath)) 

        xbmc.executebuiltin(link)

def ADDONLIST(url, mode, tag):
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    utils.setTag(tag)
    link = OPEN_URL(url)
    
    matchDir = re.compile(XML_EXPRESSION_DIR).findall(link)

    if matchDir:
        for title, link, thumbnail in matchDir:
            add2HELPDir(title, link, 553, thumbnail, thumbnail, mode,)

        AUTO_VIEW('')
        return
    
    else:
        tags = utils.getTag()
        url  = "http://portal.thelittleblackbox.com/getItem/?type=1&tags="
        utils.setUrl(url)
        url  = url + tags
        link = OPEN_URL(url)
        matchItem = re.compile(XML_EXPRESSION_ITEM).findall(link)
    
        if mode == "official":
            utils.setType("Official")
    
            for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in matchItem:
                if type == "Official":
                    add2HELPItem(id, title, repolink, cmd, 552, icon, thumbnail, description[0:-1], 'addon', rating,)                     
    
            AUTO_VIEW('movies')
            
        elif mode == "unofficial":
            utils.setType("UnOfficial")
    
            for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in matchItem:
                print id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description
                if type == "UnOfficial":
                    add2HELPItem(id, title, repolink, cmd, 552, icon, thumbnail, description[0:-1], 'addon', rating)                    
    
            AUTO_VIEW('movies')
    
        elif mode == "mostpopular":
            utils.setType("mostpopular")
    
            for id, title, icon, repolink, pluginlink, cmd, thumbnail, rating, type, description in matchItem:
                add2HELPItem(id, title, repolink, cmd, 552, icon, thumbnail, description[0:-1], 'addon', rating,)                     
    
            AUTO_VIEW('movies')
    
