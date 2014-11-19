import utils
import favourite
import os
import xbmc

ROOT     = utils.ROOT
FILENAME = utils.FILENAME

def getDefaultSearch():
    file  = os.path.join(xbmc.translatePath(ROOT), 'Search', FILENAME)
    faves = favourite.getFavourites(file)

    for fave in faves:
        label = fave[0]
        thumb = fave[1]
        cmd   = fave[2]

        if 'plugin' in cmd:
            if utils.verifyPlugin(cmd):
                return fave

        if 'RunScript' in cmd:
            if utils.verifyScript(cmd):
                return fave
    
    return None

