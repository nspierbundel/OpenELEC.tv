import xbmc
import utils

#xbmc.executebuiltin('ActivateWindow(Programs)')
#xbmc.executebuiltin('Container.Refresh')
xbmc.executebuiltin('RunAddon(%s)' % utils.ADDONID)