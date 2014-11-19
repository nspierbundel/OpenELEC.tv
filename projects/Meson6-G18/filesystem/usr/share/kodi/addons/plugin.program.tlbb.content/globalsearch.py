import os, sys
import xbmc, xbmcaddon

__addon__        = xbmcaddon.Addon('script.globalsearch')
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__language__     = __addon__.getLocalizedString
__cwd__          = __addon__.getAddonInfo('path').decode("utf-8")
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ).encode("utf-8") ).decode("utf-8")

sys.path.append(__resource__)

def doSearch():
    searchstring = None
    if len(sys.argv) > 1:
        try:
            param = sys.argv[1]
            if param.startswith('searchstring:'):
                import urllib
                searchstring = param.split(':', 1)[-1]
                searchstring = urllib.unquote_plus(searchstring)
                searchstring = searchstring.replace('\'', '')
                searchstring = searchstring.replace('"',  '')
        except:
            searchstring = None
            
    if not searchstring:     
        keyboard = xbmc.Keyboard( '', __language__(32101), False )
        keyboard.doModal()
        if ( keyboard.isConfirmed() ):
            searchstring = keyboard.getText()

    if searchstring:
        import gui
        ui = gui.GUI( "script-globalsearch-main.xml", __cwd__, "Default", searchstring=searchstring )
        ui.doModal()
        del ui
        sys.modules.clear()

doSearch()