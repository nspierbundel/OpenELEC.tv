import utils
utils.CheckVersion()

import xbmc
import os


class MyMonitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)
        self.hotkey  = utils.ADDON.getSetting('HOTKEY')
        self.context = utils.ADDON.getSetting('CONTEXT')  == 'true'


    def onSettingsChanged(self):
        hotkey  = utils.ADDON.getSetting('HOTKEY')
        context = utils.ADDON.getSetting('CONTEXT')  == 'true'

        if self.hotkey == hotkey and self.context == context:
            return

        self.hotkey  = hotkey
        self.context = context

        utils.UpdateKeymaps()


monitor = MyMonitor()

while (not xbmc.abortRequested):
    xbmc.sleep(1000)

del monitor