import xbmc
import xbmcaddon
import xbmcgui
import os
import re
import ConfigParser

def GetXBMCVersion():
    #xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')
    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor


ADDONID         = 'plugin.program.tlbb.content'
ADDON           =  xbmcaddon.Addon(ADDONID)
HOME            =  ADDON.getAddonInfo('path')
ROOT            =  ADDON.getSetting('FOLDER')
PROFILE         =  os.path.join(ROOT, 'TLBB Content')
VERSION         = '1.0.14'
ICON            =  os.path.join(HOME, 'icon.png')
FANART          =  os.path.join(HOME, 'fanart.jpg')
SEARCH          =  os.path.join(HOME, 'resources', 'media', 'search.png')
GETTEXT         =  ADDON.getLocalizedString
TITLE           =  GETTEXT(30000)
addContentIcon  =  os.path.join(HOME, 'resources', 'media', 'addContentIcon.png')
addGroupIcon    =  os.path.join(HOME, 'resources', 'media', 'addGroupIcon.png')

KEYMAP_HOT      = 'tlbb_content_hot.xml'
KEYMAP_MENU     = 'tlbb_content_menu.xml'

MAJOR, MINOR    = GetXBMCVersion()
FRODO           = (MAJOR == 12) and (MINOR < 9)
GOTHAM          = (MAJOR == 13) or (MAJOR == 12 and MINOR == 9)

FILENAME        = 'favourites.xml'
FOLDERCFG       = 'folder.cfg'
CONFIG_PATH     = os.path.join(xbmc.translatePath(ROOT), 'folder_path.cfg')
InitialFilePath = os.path.join(xbmc.translatePath(ROOT), '.initialized')

if not os.path.exists(InitialFilePath):

    #Default Home Menu folders
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"Movies")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"Movies"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"Movies",FILENAME),'w')
        f.close()
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"TV Shows")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"TV Shows"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"TV Shows",FILENAME),'w')
        f.close()
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"Music")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"Music"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"Music",FILENAME),'w')
        f.close()
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"Family")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"Family"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"Family",FILENAME),'w')
        f.close()
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"Sports")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"Sports"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"Sports",FILENAME),'w')
        f.close()
    if not os.path.exists(os.path.join(xbmc.translatePath(PROFILE),"Live TV")):
        os.makedirs(os.path.join(xbmc.translatePath(PROFILE),"Live TV"))
        f = open(os.path.join(xbmc.translatePath(PROFILE),"Live TV",FILENAME),'w')
        f.close()

    #TLBB plugin's content    
    if not os.path.exists(os.path.join(xbmc.translatePath(ROOT), '.TLBB Plugins',FILENAME)):
        os.makedirs(os.path.join(xbmc.translatePath(ROOT), '.TLBB Plugins'))
        file = os.path.join(xbmc.translatePath(ROOT), '.TLBB Plugins',FILENAME)
        f    = open(file,'w')

        f.write("<favourites>\n")
        f.write("<favourite name='TLBB Installer' thumb='special://home/addons/plugin.video.tlbbinstaller/icon.png'>ActivateWindow(10025,plugin://plugin.video.tlbbinstaller/)</favourite>\n")
        f.write("<favourite name='TLBB Backup' thumb='special://home/addons/plugin.program.tlbbbackup/icon.png'>ActivateWindow(10025,plugin://plugin.program.tlbbbackup/)</favourite>\n")
        f.write("<favourite name='TLBB Updater' thumb='special://home/addons/script.tlbb.m6/icon.png'>RunScript(special://home/addons/skin.tlbb/extras/scripts/update.py)</favourite>\n")
        f.write("<favourite name='VPNicity' thumb='special://home/addons/plugin.program.vpnicity/icon.png'>ActivateWindow(10025,plugin://plugin.program.vpnicity/)</favourite>\n")
        f.write("<favourite name='OpenVPN' thumb='special://home/addons/script.openvpn/icon.png'>RunScript(script.openvpn)</favourite>\n")
        #f.write("<favourite name='Regional Installer' thumb='special://home/addons/plugin.video.tlbbwizard/icon.png'>ActivateWindow(10025,plugin://plugin.video.tlbbwizard/)</favourite>\n")
        f.write("<favourite name='Network Manager' thumb='special://home/addons/script.linux.nm/icon.png'>RunScript(script.linux.nm)</favourite>\n")
        f.write("</favourites>")
        f.close()

    f = open(InitialFilePath,'w')
    f.close()
    
def getCurrentPath():
    config = ConfigParser.ConfigParser()

    if not os.path.exists(CONFIG_PATH):
        return None
    else:
       config.read(CONFIG_PATH)
       return config.get('FOLDER', 'path')

    
def setCurrentPath(path):
    config = ConfigParser.ConfigParser()
    f = open(CONFIG_PATH, 'w')
   
    if config.has_section('FOLDER'):
        remove_section('FOLDER')

    config.add_section('FOLDER')
    config.set('FOLDER', 'path', path)
    config.write(f)
    f.close()


def getUrl():
    config = ConfigParser.ConfigParser()

    if not os.path.exists(CONFIG_PATH):
        return None
    else:
       config.read(CONFIG_PATH)
       return config.get('URL', 'url')


def setUrl(url):
    config = ConfigParser.ConfigParser()

    if os.path.exists(CONFIG_PATH):
        f = open(CONFIG_PATH, 'a')
    else:
        f = open(CONFIG_PATH, 'w')

    if config.has_section('URL'):
        remove_section('URL')

    config.add_section('URL')
    config.set('URL', 'url', url)
    config.write(f)
    f.close()


def getType():
    config = ConfigParser.ConfigParser()

    if not os.path.exists(CONFIG_PATH):
        return None
    else:
       config.read(CONFIG_PATH)
       return config.get('addonType', 'type')


def setType(type):
    config = ConfigParser.ConfigParser()

    if os.path.exists(CONFIG_PATH):
        f = open(CONFIG_PATH, 'a')
    else:
        f = open(CONFIG_PATH, 'w')

    if config.has_section('addonType'):
        remove_section('addonType')

    config.add_section('addonType')
    config.set('addonType', 'type', type)
    config.write(f)
    f.close()


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def generateMD5(text):
    if not text:
        return ''

    try:
        import hashlib        
        return hashlib.md5(text).hexdigest()
    except:
        pass

    try:
        import md5
        return md5.new(text).hexdigest()
    except:
        pass
        
    return '0'


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING') != 'True':
        VerifyKeymaps()

    if prev == curr:        
        return

    verifySuperSearch(replace=True)

    ADDON.setSetting('VERSION', curr)

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING') != 'True':
        verifySuperSearch(replace=False)

    if prev == '0.0.0' or prev== '1.0.0':
        folder  = xbmc.translatePath(PROFILE)
        if not os.path.isdir(folder):
            try:    os.makedirs(folder) 
            except: pass


def verifySuperSearch(replace=False):
    dst = os.path.join(xbmc.translatePath(ROOT), 'Search', FILENAME)

    if os.path.exists(dst):
        if not replace:
            return

    src = os.path.join(HOME, 'resources', 'Search', FILENAME)

    try:    os.makedirs(os.path.join(xbmc.translatePath(ROOT), 'Search'))
    except: pass

    import shutil
    shutil.copyfile(src, dst)


def UpdateKeymaps():
    DeleteKeymap(KEYMAP_HOT)
    DeleteKeymap(KEYMAP_MENU)
    VerifyKeymaps()

        
def DeleteKeymap(map):
    path = os.path.join(xbmc.translatePath('special://profile/keymaps'), map)

    tries = 5
    while os.path.exists(path) and tries > 0:
        tries -= 1 
        try: 
            os.remove(path) 
            break 
        except: 
            xbmc.sleep(500)


def VerifyKeymaps():
    reload = False

    if VerifyKeymapHot():  reload = True
    if VerifyKeymapMenu(): reload = True

    if not reload:
        return

    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')  


def VerifyKeymapHot():
    dest = os.path.join(xbmc.translatePath('special://profile/keymaps'), KEYMAP_HOT)

    if os.path.exists(dest):
        return False

    key = ADDON.getSetting('HOTKEY').lower()

    includeKey = key in ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'g']

    if not includeKey:
        DeleteKeymap(KEYMAP_HOT)
        return True

    cmd = '<keymap><Global><keyboard><%s>XBMC.RunScript(special://home/addons/plugin.program.tlbb.content/hot.py)</%s></keyboard></Global></keymap>'  % (key, key)
    
    f = open(dest, mode='w')
    f.write(cmd)
    f.close()
    xbmc.sleep(1000)

    tries = 4
    while not os.path.exists(dest) and tries > 0:
        tries -= 1
        f = open(dest, mode='w')
        f.write(t)
        f.close()
        xbmc.sleep(1000)

    return True


def VerifyKeymapMenu():
    context = ADDON.getSetting('CONTEXT')  == 'true'

    if not context:
        DeleteKeymap(KEYMAP_MENU)
        return True

    keymap = xbmc.translatePath('special://profile/keymaps')
    src    = os.path.join(HOME, 'resources', 'keymaps', KEYMAP_MENU)
    dst    = os.path.join(keymap, KEYMAP_MENU)

    try:
        if not os.path.isdir(keymap):
            os.makedirs(keymap)
    except Exception, e:
        print 'Making folders : %s' % str(e)

    try:
        import shutil
        shutil.copy(src, dst)
    except Exception, e:
        print 'Copying file : %s' % str(e)

    return True


def verifyPlugin(cmd):
    try:
        plugin = re.compile('plugin://(.+?)/').search(cmd).group(1)
        xbmcaddon.Addon(plugin)
        return True
    except:
        pass

    return False


def verifyScript(cmd):
    try:
        script = cmd.split('(', 1)[1].split(',', 1)[0].replace(')', '').replace('"', '')
        if script != "special://home/addons/skin.tlbb/extras/scripts/update.py":
            xbmcaddon.Addon(script)
            return True
        return True
    except:
        pass

    return False


def GetFolder(title):
    default = ROOT
    folder  = xbmc.translatePath(PROFILE)

    if not os.path.isdir(folder):
        os.makedirs(folder) 

    folder = xbmcgui.Dialog().browse(3, title, 'files', '', False, False, default)
    if folder == default:
        return None

    return xbmc.translatePath(folder)


def showBusy():
    busy = None
    try:
        import xbmcgui
        busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        busy.show()

        try:    busy.getControl(10).setVisible(False)
        except: pass
    except:
        busy = None

    return busy


if __name__ == '__main__':
    pass
