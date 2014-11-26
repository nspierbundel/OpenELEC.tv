import xbmc,time

for i in 1,2,3,4,5:
    print "in loop"
    xbmc.executebuiltin('UpdateAddonRepos')
    time.sleep(2)
