#Python modules
import os
import re
import sys
import urllib
import urllib2
import time
import subprocess
import threading

#XBMC modules
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

#Plugin modules
import downloader
import utils 
import backup
import requests

ADDON = xbmcaddon.Addon(id='plugin.program.tlbbbackup')
flagWarning = 0
BASE_URL = utils.BASE_URL

def option():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a option', ['Restore', 'Backup'])
    return ret
            
def searchKeywordBox(msg,hidden=False):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, msg)
        keyboard.setHiddenInput(hidden)
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered =  keyboard.getText() .replace(' ','%20')
            if search_entered == None:
                return False          
        return search_entered    
        
def main(user, validateString):
        retVal = option()
        #Upload
        if retVal == 1:
            dialog = xbmcgui.Dialog()
            dp = xbmcgui.DialogProgress()
            dp.create("TLBB Backup","Archiving backup ...",'', 'Please Wait')

            backup_name      =  searchKeywordBox('Please Enter Keyword')
            if backup_name == "":
                backup_name      =  searchKeywordBox('Please Enter Keyword')
                if backup_name == "":
                    return
            backup_password  =  searchKeywordBox('Please Enter password')
            if backup_password == "":
                backup_password  =  searchKeywordBox('Please Enter password')
                if backup_password == "":
                        return

            folder  =  xbmc.translatePath(os.path.join('special://home',''))
            if backup.is_exist(user, validateString, backup_name):
	        ans = dialog.yesno("TLBB Backup","Backup with same name already exist Want to overwrite?")
                if ans:
                    #Ask only two times for wrong password
                    for count in 1, 2:
               	        ret_val = backup.upload_wrapper(dp, user, validateString, backup_name,backup_password,1)
			utils.DBG(ret_val)
                        if ret_val == utils.WRONG_PASSWORD:
                            dialog.ok("Wrong password","Please re enter password...")
                            backup_password  =  searchKeywordBox('Please Enter password')
                        if backup_password == "":
                            dialog.ok("LBB Backup","Blank password","Please retry")
                            break
                        if ret_val in [utils.UPLOAD_PROGRESS_FAILED, utils.UPLOAD_FILE_WRITE_FAILED, utils.UPLOAD_INVALID_FILE, utils.UPLOAD_FAILED]:
                            dialog.ok("LBB Backup","Keyword: " + backup_name ,"Upload Failed")
                            break
                        if ret_val == "ok" :
                            dialog.ok("TLBB Backup","Keyword: " + backup_name ,"Backup uploaded successfully")
                            break
                else:
                    dialog.ok("TLBB Backup","Keyword: " + backup_name ,"Failed")
            else :
                try:
                    ret_val = backup.upload_wrapper(dp, user, validateString, backup_name,backup_password,0)
                    utils.DBG(ret_val)
                    errorList = [utils.UPLOAD_PROGRESS_FAILED, utils.UPLOAD_FILE_WRITE_FAILED, utils.UPLOAD_INVALID_FILE, utils.UPLOAD_FAILED]
                    if ret_val in errorList:
                        dialog.ok("LBB Backup","Keyword: " + backup_name ,"Upload Failed")
                    else if ret_val == "ok":
                        dialog.ok("TLBB Backup","Keyword: " + backup_name ,"Backup uploaded successfully")
                    else:
                        dialog.ok("LBB Backup","Keyword: " + backup_name ,"Upload Failed...")
                except Exception as e:
                    print e

        #Download
        if retVal == 0:
            dialog = xbmcgui.Dialog()      
            dp = xbmcgui.DialogProgress()
            dp.create("TLBB Restore","Downloading ",'', 'Please Wait')
            keyword      =  searchKeywordBox("Please Enter Keyword")
            if backup.is_exist(user, validateString, backup_name):
	            url ='http://backups.thelittleblackbox.com/'+keyword + '.tar.gz'
	            path         =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
	            lib          =  os.path.join(path, keyword+'.tar.gz')
	            addonfolder  =  xbmc.translatePath(os.path.join('special://home',''))
	            
	            downloader.download(url,lib)
	            
	            dp.update(0,"", "Extracting Zip Please Wait")
	            
		    utils.all(lib,addonfolder,dp)
		    print "######################Jadav: Copying guisettings.xml ##############################"
	            guisetting_path = xbmc.translatePath(os.path.join('special://profile','guisettings.xml'))
	            guisetting_tlbb_path = xbmc.translatePath(os.path.join('special://profile','guisettings_tlbb.xml'))
		    shutil.copyfile(guisetting_path, guisetting_tlbb_path)
	            xbmc.executebuiltin('UpdateLocalAddons')
	            xbmc.executebuiltin( 'UpdateAddonRepos' )
		    os.remove(lib)
	            ret = dialog.yesno("All Done", "[COLOR yellow]Please be patient to complete installation we will restart XBMC. Brought To You By TLBB[/COLOR]")
                    if ret:
                        subprocess.call(["reboot"])
            else:
                dialog.ok("TLBB Restore","Invalid Keyword: No backup with given name exist")

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

def login():
    log = searchKeywordBox('Please Enter TLBB User ID')
    pwd = searchKeywordBox('Please Enter TLBB password',True)

    if log == "" or "pwd" == "":
        return "","",""

    URL = BASE_URL + "/verifyUser/?log=" + log + "&pwd=" + pwd
    ret = requests.get(URL).text
    utils.DBG(ret,"testLogin")
    try:
        if ret.split(':')[0] == "success":
            return log,ret.split(':')[0],ret.split(':')[1]
        return log,"failed",""
    except:
        return log,"failed",""

#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        
        log, ret, key = login()
        if ret == 'success':
            main(log, key)
        else:
            dialog = xbmcgui.Dialog()
            dialog.ok("TLBB Restore","Invalid userID or Password ")

xbmcplugin.endOfDirectory(int(sys.argv[1]))
