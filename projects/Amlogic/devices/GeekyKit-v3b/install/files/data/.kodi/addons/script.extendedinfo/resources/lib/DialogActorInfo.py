import xbmc
import xbmcaddon
import xbmcgui
from Utils import *
try:
    from ImageTools import *
except:
    log("Exception when importing ImageTools")
from TheMovieDB import *
from YouTube import *
import DialogVideoInfo
import DialogTVShowInfo
homewindow = xbmcgui.Window(10000)

addon = xbmcaddon.Addon()
addon_id = addon.getAddonInfo('id')
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_strings = addon.getLocalizedString
addon_path = addon.getAddonInfo('path').decode("utf-8")


class DialogActorInfo(xbmcgui.WindowXMLDialog):
    ACTION_PREVIOUS_MENU = [92, 9]
    ACTION_EXIT_SCRIPT = [13, 10]

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self)
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        self.movieplayer = VideoPlayer(popstack=True)
        self.id = kwargs.get('id', False)
        self.person = False
        if not self.id:
            name = kwargs.get('name').decode("utf-8").split(" " + xbmc.getLocalizedString(20347) + " ")
            name = name[0].strip()
            names = name.split(" / ")
            if len(names) > 1:
                ret = xbmcgui.Dialog().select("Actor Info", names)
                if ret == -1:
                    return None
                name = names[ret]
            self.id = GetPersonID(name)
            if self.id:
                self.id = self.id["id"]
            else:
                return None
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        if self.id:
            self.person = GetExtendedActorInfo(self.id)
            youtube_thread = Get_Youtube_Vids_Thread(self.person["general"]["name"], "", "relevance", 15)
            youtube_thread.start()
            filter_thread = Filter_Image_Thread(self.person["general"]["thumb"], 25)
            filter_thread.start()
            db_movies = 0
            for item in self.person["movie_roles"]:
                if "DBID" in item:
                    db_movies += 1
            self.person["general"]["DBMovies"] = str(db_movies)
            filter_thread.join()
            self.person["general"]['ImageFilter'], self.person["general"]['ImageColor'] = filter_thread.image, filter_thread.imagecolor
            youtube_thread.join()
            self.youtube_vids = youtube_thread.listitems
        else:
            Notify(addon.getLocalizedString(32143))
        xbmc.executebuiltin("Dialog.Close(busydialog)")

    def onInit(self):
        if not self.person:
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            self.close()
            return
        homewindow.setProperty("actor.ImageColor", self.person["general"]["ImageColor"])
        windowid = xbmcgui.getCurrentWindowDialogId()
        passDictToSkin(self.person["general"], "actor.", False, False, windowid)
        self.getControl(150).addItems(create_listitems(self.person["movie_roles"], 0))
        self.getControl(250).addItems(create_listitems(self.person["tvshow_roles"], 0))
        self.getControl(350).addItems(create_listitems(self.youtube_vids, 0))
        self.getControl(450).addItems(create_listitems(self.person["images"], 0))
        self.getControl(550).addItems(create_listitems(self.person["movie_crew_roles"], 0))
        self.getControl(650).addItems(create_listitems(self.person["tvshow_crew_roles"], 0))
        self.getControl(750).addItems(create_listitems(self.person["tagged_images"], 0))
    #    self.getControl(150).addItems(tvshow_listitems)

    def setControls(self):
        pass

    def onAction(self, action):
        if action in self.ACTION_PREVIOUS_MENU:
            self.close()
            PopWindowStack()
        elif action in self.ACTION_EXIT_SCRIPT:
            self.close()

    def onClick(self, controlID):
        homewindow.setProperty("WindowColor", xbmc.getInfoLabel("Window(home).Property(ActorInfo.ImageColor)"))
        if controlID in [150, 550]:
            listitem = self.getControl(controlID).getSelectedItem()
            AddToWindowStack(self)
            self.close()
            dialog = DialogVideoInfo.DialogVideoInfo(u'script-%s-DialogVideoInfo.xml' % addon_name, addon_path, id=listitem.getProperty("id"), dbid=listitem.getProperty("dbid"))
            dialog.doModal()
        elif controlID in [250, 650]:
            listitem = self.getControl(controlID).getSelectedItem()
            # options = [addon.getLocalizedString(32147), addon.getLocalizedString(32148)]
            # selection = xbmcgui.Dialog().select(addon.getLocalizedString(32151), options)
            # if selection == 0:
            #     GetCreditInfo(listitem.getProperty("credit_id"))
            # if selection == 1:
            AddToWindowStack(self)
            self.close()
            dialog = DialogTVShowInfo.DialogTVShowInfo(u'script-%s-DialogVideoInfo.xml' % addon_name, addon_path, id=listitem.getProperty("id"), dbid=listitem.getProperty("dbid"))
            dialog.doModal()
        elif controlID in [450, 750]:
            image = self.getControl(controlID).getSelectedItem().getProperty("original")
            dialog = SlideShow(u'script-%s-SlideShow.xml' % addon_name, addon_path, image=image)
            dialog.doModal()
        elif controlID == 350:
            listitem = self.getControl(controlID).getSelectedItem()
            AddToWindowStack(self)
            self.close()
            self.movieplayer.playYoutubeVideo(listitem.getProperty("youtube_id"), listitem, True)
            self.movieplayer.wait_for_video_end()
            PopWindowStack()
        elif controlID == 132:
            text = self.person["general"]["description"] + "[CR]" + self.person["general"]["biography"]
            w = TextViewer_Dialog('DialogTextViewer.xml', addon_path, header=addon.getLocalizedString(32037), text=text, color=self.person["general"]['ImageColor'])
            w.doModal()

    def onFocus(self, controlID):
        pass
