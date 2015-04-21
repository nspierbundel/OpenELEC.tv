import urllib,re,sys,os
import xbmc,xbmcgui,xbmcaddon,xbmcplugin,threading,time
from resources.modules import main



addon_id = 'plugin.video.phstreams'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = 'http://artpathg'
cachedir = xbmc.translatePath('special://temp/')

def SEARCHistory():
    dialog = xbmcgui.Dialog()
    
    searchType = 'Movies'
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'PhoenixSearchHistory')
    if not os.path.exists(SeaFile):
        SEARCH('',searchType)
    else:
        main.addDir('Search',searchType,'simsearch',art+'/search.png','','','','')
        main.addDir('Clear History',SeaFile,'clearsearch',art+'/cleahis.png','','','','')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            seahis=urllib.unquote(seahis)    
            main.addDir(seahis,searchType,'simsearch',thumb,'','','','')

def sortSearchList(searchList,query):
    import locale
    loc = locale.getlocale()
    try:
        locale.setlocale(locale.LC_ALL, "")
    except:
        locale.setlocale(locale.LC_ALL, "C")
    searchList.sort(key=lambda tup: tup[0].decode('utf-8').encode('utf-8'),cmp=locale.strcoll)
    locale.setlocale(locale.LC_ALL, loc)
    temp = []
    itemstoremove = []
    i = 0
    if re.search('(?i)s(\d+)e(\d+)',query) or re.search('(?i)Season(.+?)Episode',query) or re.search('(?i)(\d+)x(\d+)',query):
        for item in searchList:
            if re.search('(?i)\ss(\d+)e(\d+)',item[0]) or re.search('(?i)Season(.+?)Episode',item[0]) or re.search('(?i)(\d+)x(\d+)',item[0]):
                temp.append(item)
                itemstoremove.append(i)
            i += 1
    i = 0
    for remove in itemstoremove:
        searchList.pop(remove - i)
        i += 1
    return temp + searchList

def SEARCH(mname,type,libID=''):
    if libID=='':
        print 'NO libID'
        
    else:
        libName=mname
        if re.search('(?i).\s\([12][90]\d{2}\)',mname):
            mname = re.sub('(?i)^(.+?)\s\([12][90]\d{2}\).*','\\1',mname)
        elif re.search('(?i).\s[12][90]\d{2}',mname):
            mname = re.sub('(?i)^(.+?)\s[12][90]\d{2}.*','\\1',mname)
        mname = re.sub('(?i)\s\s+',' ',mname).strip()
    try:import Queue as queue
    except ImportError:import queue
    results = []
    searchList=[]
    #mname=main.unescapes(mname)
    mname=main.removeColoredText(mname)
    if mname=='Search': mname=''
    encode = main.updateSearchFile(mname,type)
    if not encode: return False
    else:
        sources = []
        encodeunquoted = urllib.unquote(encode)
        encode = re.sub('(?i)[^a-zA-Z0-9]',' ',encodeunquoted)
        encode = re.sub('(?i)\s\s+',' ',encode).strip()
        encode = urllib.quote(encode)
        if type=='Movies':
            #sources.append('VIP')
            q = queue.Queue()
            threading.Thread(target=vip,args=(encode,type,q)).start()
            results.append(q)
        else:
            encodetv = urllib.quote(re.sub('(?i)^(.*?((\ss(\d+)e(\d+))|(Season(.+?)Episode \d+)|(\d+)x(\d+))).*','\\1',urllib.unquote(encode)))    
        encode = urllib.unquote(encode)    
        if libID=='':
            dialogWait = xbmcgui.DialogProgress()
            ret = dialogWait.create('Please wait. Phoenix is searching...')
            loadedLinks = 0
            remaining_display = 'Sources searched :: [B]'+str(loadedLinks)+' / '+str(len(results))+'[/B].'
            dialogWait.update(0,'[B]'+type+' Phoenix Search - ' + encodeunquoted + '[/B]',remaining_display)
            totalLinks = len(results)
            whileloopps = 0
            xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
            while totalLinks > loadedLinks:
                for n in range(len(results)):
                    try:
                        searchList.extend(results[n].get_nowait())
                        loadedLinks += 1
                        percent = (loadedLinks * 100)/len(results)
                        remaining_display = 'Sources searched :: [B]'+str(loadedLinks)+' / '+str(len(results))+'[/B].'
                        dialogWait.update(percent,'[B]'+type+' Phoenix - ' + encodeunquoted + '[/B]',remaining_display,sources[n] + ' finished searching')
                        if dialogWait.iscanceled(): break;
                    except: pass
                if dialogWait.iscanceled(): break;
                time.sleep(.1)
            ret = dialogWait.create('Please wait until Video list is cached.')
            totalLinks = len(searchList)
            loadedLinks = 0
            remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display,' ')
            searchList = sortSearchList(searchList,mname)
        
        if not libID=='':
            for n in range(len(results)):
                searchList.extend(results[n].get())
            searchList = sortSearchList(searchList,mname)
            import library
            t=threading.Thread(target=library.buildHostDB,args=(searchList,libID,libName))
            t.start()
            t.join()
            
        else:
            if type == 'TV':
                wordsalt = set(encodewithoutepi.lower().split())
                encode = urllib.unquote(encodetv)
            wordsorg = set(encode.lower().split())
            for name,section,url,thumb,mode,dir in searchList:
                name = name.replace('&rsquo;',"'").replace('&quot;','"').strip()
                cname = re.sub('(?i)[^a-zA-Z0-9]',' ',name)
                name = name+' [COLOR=orange]'+section+'[/COLOR]'
                if type == 'TV' and (section == 'MBox' or section == 'WatchSeries' or section == 'iWatchOnline' or section == 'IceFilms' or section == 'TubePlus'):
                    words = wordsalt
                else: words = wordsorg
                if words.issubset(cname.lower().split()):
                    if dir:
                        if type=='Movies':
                            if 'sublink' in url:
                                  main.addDir(name,url,'sublinks',thumb,'','','','')
                            else: 
                                  main.addDLDir(name,url,'linkmode',thumb,'','','','',isFolder=False, isPlayable=True)
                        else:
                            if re.search('(?i)\ss(\d+)e(\d+)',name) or re.search('(?i)Season(.+?)Episode',name) or re.search('(?i)(\d+)x(\d+)',name):
                                print 'THIS IS AREA 2'
                                main.addDir(name,url,int(mode),thumb,'','','','')
                            else:
                                print 'THIS IS AREA 3'
                                main.addDir(name,url,int(mode),thumb,'','','','')
                    else:
                        if type=='Movies':
                            if 'sublink' in url:
                                  main.addDir(name,url,'sublinks',thumb,'','','','')
                            else: 
                                  main.addDLDir(name,url,'linkmode',thumb,'','','','',isFolder=False, isPlayable=True)
                        else:
                            if re.search('(?i)\ss(\d+)e(\d+)',name) or re.search('(?i)Season(.+?)Episode',name) or re.search('(?i)(\d+)x(\d+)',name):
                                print 'THIS IS AREA 5'
                                main.addDir(name,url,int(mode),thumb,'','','','')
                            else:
                                print 'THIS IS AREA 6'
                                main.addDir(name,url,int(mode),thumb,'','','','')
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                    dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                    if dialogWait.iscanceled(): return False    
            dialogWait.close()
            del dialogWait
            if type=='Movies':
                xbmcgui.Window(10000).setProperty('MASH_SSR_TYPE', '2')
            else: xbmcgui.Window(10000).setProperty('MASH_SSR_TYPE', '1')
            try:
                filelist = [ f for f in os.listdir(cachedir) if f.endswith(".fi") ]
                for f in filelist: os.remove(os.path.join(cachedir,f))
            except:pass
            if not loadedLinks:
                xbmc.executebuiltin("XBMC.Notification(Super Search - "+encode.replace("%20"," ")+",No Results Found,3000)")
                xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False) 
                return False



def vip(encode,type,q):
    #from resources.modules import filestube
    returnList = vipSuperSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def vipSuperSearch(encode,type):
    try:
        returnList=[]
        encode = encode.replace('%20',' ')
        urls = []
        urls.append("http://tuzla.watchkodi.com/2015%20HD.xml")
        urls.append("http://tuzla.watchkodi.com/2014%20HD.xml")
        urls.append("http://tuzla.watchkodi.com/new%20screener.xml")
        urls.append("http://tuzla.watchkodi.com/2013%20HD.xml")
        urls.append("http://tuzla.watchkodi.com/1080p%20movies.xml")
        urls.append("http://tuzla.watchkodi.com/3D.xml")
        urls.append("http://tuzla.watchkodi.com/Boxset.xml")
        urls.append("http://tuzla.watchkodi.com/NEW%20HD.xml")
        urls.append("http://tuzla.watchkodi.com/GrandDane/mains.xml")
        urls.append("http://tuzla.watchkodi.com/kids_animation.xml")
        urls.append("http://tuzla.watchkodi.com/Halloween.xml")
        urls.append("http://tuzla.watchkodi.com/Special%20selection.xml")
        urls.append("http://tuzla.watchkodi.com/TVshows/tvshows.xml")
        urls.append("http://tuzla.watchkodi.com/LIVE%20TV/Live%20tv%20directory.xml")
        urls.append("http://tuzla.watchkodi.com/Western%20collection.xml")
        urls.append("http://tuzla.watchkodi.com/Documentary.xml")
        urls.append("http://tuzla.watchkodi.com/music/Music-Directory.xml")
        urls.append("http://tuzla.watchkodi.com/RADIO/1.RadioDIR.xml")
        urls.append("http://tuzla.watchkodi.com/veehdCollection.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/one242415.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/disclaimer.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/LatestRelease.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/featured.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/requests.xml")
        urls.append("http://gibraltar.watchkodi.com/retrotv/retrotv_directory2.xml")
        urls.append("http://gibraltar.watchkodi.com/topten/TopTen_Directory.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/sixties.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/hallmark.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/lifetimebest.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/funny.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/stooges.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/hardy.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/budandlou.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/cheech.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/carson.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/walkingdead.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/westerns.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/psycothriller.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/erotic.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/cia.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/test.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/hitch.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/monster.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/stippers.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/grindhouse.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/blax.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/batman.xml")
        urls.append("http://gibraltar.watchkodi.com/Sports/Sports_Directory.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/standupUK.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/monroe.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/elvis.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/clinteastwood.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/melbrookscollection.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/jackN.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/jasonstatham.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/stephanking.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/war.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/disaster.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/kungfu.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/zombies.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/007.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/bikers.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/startrek.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/animated.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/ScaryMovies.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/oscars.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/abcmovie.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/discofever.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/blackentertainment.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/janeausten.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/mafiamovies.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/superhero.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/standupcomedy.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/roasts.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/fastcars.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/liveconcert.xml")
        urls.append("http://gibraltar.watchkodi.com/CinemaItaliano/cinemaitaliano_directory.xml")
        urls.append("http://gibraltar.watchkodi.com/ForeignCinema/ForeignCinemaDirectory.xml")
        urls.append("http://gibraltar.watchkodi.com/Foriegn/italyTV1.xml")
        urls.append("http://gibraltar.watchkodi.com/Foriegn/italianseries.xml")
        urls.append("http://gibraltar.watchkodi.com/TwilightZone/twilightzone_directory.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/videogames.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/SciFi.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/Vampires.xml")
        urls.append("http://gibraltar.watchkodi.com/Collections/UFOs.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/softporn.xml")
        urls.append("http://gibraltar.watchkodi.com/Movies/Lfilms.xml")
        urls.append("http://gibraltar.watchkodi.com/Misc/twitter.xml")
        urls.append("http://zenica.watchkodi.com/Genre/Latest%20Releases.xml")
        urls.append("http://zenica.watchkodi.com/Genre/top30.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Genre%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Decades%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/Movies/1080p%20Movies.xml")
        #urls.append("http://zenica.watchkodi.com/Movies/3D%20Movies.xml")
        urls.append("http://zenica.watchkodi.com/Genre/kidszone.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Kidz%20Collectionz.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Kids%20TV%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Cartoonland%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/Genre/MartialArts.xml")
        urls.append("http://zenica.watchkodi.com/Directories/720p%20Boxsets%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/Genre/Superheroes.xml")
        urls.append("http://zenica.watchkodi.com/Genre/Organized%20Crime.xml")
        urls.append("http://zenica.watchkodi.com/Directories/BoB%20Directory.xml")
        urls.append("http://zenica.watchkodi.com/TV/BoB%20TV/British%20Stand%20Up.xml")
        urls.append("http://zenica.watchkodi.com/Directories/Docs%20Directory.xml")
        urls.append("http://alaska.watchkodi.com/maindir/main2.xml")
        urls.append("http://alaska.watchkodi.com/Playlist/playmain.xml")

        
        
        xml = main.batchOPENURL(urls)
        match=re.compile('(?sim)(<poster>.*?(?=<poster>|\Z))').findall(xml)
        for posterXML in match:
            poster = re.compile('(?sim)<poster>(.*?)</poster>').findall(posterXML)[0]
            posterXML=posterXML.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
            match2 = re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>').findall(posterXML)
            for title,url,thumb in match2:
                if re.search('(?i)'+encode,title):
                    if 'sublink' in url:
                        returnList.append((title.strip(),poster,url,thumb,'linkmode',True))
                    else:
                        returnList.append((title.strip(),poster,url,thumb,'linkmode',False))
                    
        return returnList
    except: return []
