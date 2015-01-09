#
#       Copyright (C) 2014
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#


import xbmc
import xbmcgui
import xbmcaddon
import sys
import os


if sys.version_info < (2, 7):
    import simplejson
else:
    import json as simplejson 


ADDONID = 'script.tlbb.systemsettings'
ADDON   =  xbmcaddon.Addon(ADDONID)

def main():
    if len(sys.argv) < 2:
        return

    param = sys.argv[1].lower()

    if param == 'setlanguage':
        return doSetLanguage()

    if param == 'refresh':
        return refresh()

    if param == 'zoomup':
        return zoom(True)

    if param == 'zoomdown':
        return zoom(False)

    if param == 'setsubtitledownload':
        return doSetSubtitleDownload()

    if param == 'setsubtitlepreferred':
        return doSetSubtitlePreferred()

    if param == 'setsubtitlecharset':
        return doSetSubtitleCharset()

    if param == 'setregion':
        doSetRegion()

    if param == 'settimezonecountry':
        doSetTZCountry()

    if param == 'settimezone':
        doSetTZ()


def execute(cmd):
    log(cmd)
    xbmc.executebuiltin(cmd)


def log(text):
    try:
        output = '%s : %s' % (ADDONID, str(text))
        #print output
        xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def setSetting(setting, value):
    setting = '"%s"' % setting

    if isinstance(value, list):
        text = ''
        for item in value:
            text += '"%s",' % str(item)

        text  = text[:-1]
        text  = '[%s]' % text
        value = text

    elif not isinstance(value, int):
        value = '"%s"' % value

    query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % (setting, value)
    log(query)
    response = xbmc.executeJSONRPC(query)
    log(response)


def getSetting(setting):
    try:
        setting = '"%s"' % setting
 
        query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (setting)
        log(query)
        response = xbmc.executeJSONRPC(query)
        log(response)

        response = simplejson.loads(response)                

        if response.has_key('result'):
            if response['result'].has_key('value'):
                return response ['result']['value'] 
    except:
        pass

    return None


def getLanguage(language):
    file = xbmc.translatePath(os.path.join('special://xbmc/', 'language', language, 'langinfo.xml'))

    try:        
        f    = open(file, 'r')
        text = f.read()
        f.close()
    except:
        return None

    text = text.replace(' =',  '=')
    text = text.replace('= ',  '=')
    text = text.replace(' = ', '=')

    return text

def getTZCountries():
    file = '/usr/share/zoneinfo/iso3166.tab'

    countries = []

    try:        
        f    = open(file, 'r')
        lines = f.readlines()
        f.close()
    except:
        return countries

    for line in lines:
        if line.startswith('#'):
            continue
        items = line.split('\t')
        if len(items) < 2:
            continue

        code    = items[0]
        country = items[1].replace('\n', '')
        countries.append([country, code])

    countries = sorted(countries)
    return countries


def getTZ(theCode):
    file = '/usr/share/zoneinfo/zone.tab'

    zones = []

    try:        
        f    = open(file, 'r')
        lines = f.readlines()
        f.close()
    except:
        return zones

    for line in lines:
        if line.startswith('#'):
            continue
        items = line.split('\t')
        if len(items) < 3:
            continue

        code     = items[0]
        location = items[1]
        zone     = items[2].replace('\n', '')

        if code != theCode:
            if len(zones) > 0:
                #this logic assumes same codes are sequential in file
                break
        else:
            zones.append(zone)

    zones = sorted(zones)
    return zones


def getCharsets():
    file = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'charset.txt'))

    default  = xbmc.getLocalizedString(13278)

    charsets = []
    try:        
        f      = open(file, 'r')
        lines = f.readlines()
        f.close()
    except:
        return charsets

    for line in lines:
        line = line.replace('"',  '')
        line = line.replace('\r', '')
        line = line.replace('\n', '')
        line = line.split(',')
        if len(line) < 2:
            continue

        charsets.append([line[1].strip(), line[0].strip()])

    charsets = sorted(charsets)
    charsets.insert(0, [default, 'DEFAULT'])
    return charsets


def doSetSubtitleCharset():
    import select
    menu = []

    setting = 'subtitles.charset'
    default = xbmc.getLocalizedString(13278)

    charsets = getCharsets()

    if len(charsets) == 0:
        return

    for idx, charset in enumerate(charsets):
        menu.append([charset[0], idx])

    current = getSetting(setting)    

    for charset in charsets:
        if current == charset[1]:
            current = charset[0]
            break

    option = select.select(xbmc.getLocalizedString(31380), menu, current)

    if option < 0:
        return

    label = charsets[option][0]

    if label == current:
        return

    charset = charsets[option][1]

    if charset == current:
        return

    setSetting(setting, charset)
    execute('Skin.SetBool(SubtitleCharsetSet)')
    xbmc.executebuiltin('Skin.SetString(%s,%s)' % (setting, label))

def doSetTZ():
    import select
    menu = []

    setting = 'locale.timezone'
    
    code      = '??'
    countries = getTZCountries()
    country   = getSetting('locale.timezonecountry')

    for item in countries:
        if country.lower() == item[0].lower():
            code = item[1]
            break

    timezones = getTZ(code)

    if len(timezones) == 0:
        return
        
    for idx, zone in enumerate(timezones):
        menu.append([zone, idx])

    current = getSetting(setting)
     
    option = select.select(xbmc.getLocalizedString(14080), menu, current)

    if option < 0:
        return

    tz = menu[option][0]

    if tz == current:
        return

    setSetting(setting, tz)
    execute('Skin.SetBool(TimezoneSet)')
    refreshSkinString(setting)


def doSetTZCountry():
    import select
    menu = []

    setting = 'locale.timezonecountry'
    
    countries = getTZCountries()
        
    for idx, country in enumerate(countries):
        menu.append([country[0], idx])

    current = getSetting(setting)
     
    option = select.select(xbmc.getLocalizedString(14080), menu, current) #14079 = 'Timezone country'

    if option < 0:
        return

    tz = menu[option][0]

    if tz == current:
        return

    setSetting(setting, tz)
    execute('Skin.SetBool(TimezoneCountrySet)')
    refreshSkinString(setting)


def doSetLanguage():
    import select
    menu = []

    setting = 'locale.language'

    skin = xbmc.getSkinDir().lower()
    path = xbmc.translatePath(os.path.join('special://home/addons/', skin, 'language'))

    try:    current, dirs, files = os.walk(path).next()
    except: dirs = []

    if len (dirs) == 0:
        path = xbmc.translatePath(os.path.join('special://xbmc/addons/', skin, 'language'))

        try:    current, dirs, files = os.walk(path).next()
        except: return

    if len (dirs) == 0:
        return
   
    dirs = sorted(dirs, key=str.lower)

    flagDir = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'flags'))

    import re
    for idx, dir in enumerate(dirs):
        valid = False
        code  = ''
        try:
            text  = getLanguage(dir) 
            code  = re.compile('<language locale="(.+?)">').search(text).group(1)
            flag  = os.path.join(flagDir, '%s.png' % code.lower())
            valid = os.path.exists(flag)
        except:
            pass

        if not valid:
            flag = getUnknownFlag(dir)
            flag = os.path.join(flagDir, '%s.png' % flag)

        menu.append([dir, idx, flag])

    current = getSetting(setting)
     
    option = select.select(xbmc.getLocalizedString(309), menu, current) #248 - Language

    if option < 0:
        return

    language = menu[option][0]

    if language == current:
        return

    setSetting(setting, language)
    setSetting('locale.charset', 'DEFAULT')
    execute('Skin.SetBool(LanguageSet)')
    refreshSkinString(setting)


def getUnknownFlag(country):
    country = country.lower()

    if country == 'basque':                   return 'bq'
    if country == 'filipino':                 return 'ph'
    if country == 'haitian (haitian creole)': return 'ht'
    if country == 'georgian':                 return 'un'
    if country == 'lithuanian':               return 'lt'
    if country == 'mongolian (mongolia)':     return 'un'
    if country == 'romansh':                  return 'rm'
    if country == 'sinhala':                  return 'un'
    if country == 'spanish (venezuela)':      return 'un'
    if country == 'vietnamese (viet nam)':    return 'vi'

    return 'un'


def doSetSubtitleDownload():
    import select
    menu = []

    setting = 'subtitles.languages'

    skin = xbmc.getSkinDir().lower()
    path = xbmc.translatePath(os.path.join('special://home/addons/', skin, 'language'))

    try:    current, dirs, files = os.walk(path).next()
    except: dirs = []

    if len (dirs) == 0:
        path = xbmc.translatePath(os.path.join('special://xbmc/addons/', skin, 'language'))

        try:    current, dirs, files = os.walk(path).next()
        except: return

    if len (dirs) == 0:
        return
   
    dirs = sorted(dirs, key=str.lower)

    flagDir = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'flags'))

    import re
    for idx, dir in enumerate(dirs):
        valid = False
        code  = ''
        try:
            text  = getLanguage(dir) 
            code  = re.compile('<language locale="(.+?)">').search(text).group(1)
            flag  = os.path.join(flagDir, '%s.png' % code.lower())
            valid = os.path.exists(flag)
        except:
            pass

        if not valid:
            flag = getUnknownFlag(dir)
            flag = os.path.join(flagDir, '%s.png' % flag)

        menu.append([dir, idx, flag])
        
    list    = getSetting(setting)
    current = None

    if len(list) > 0:
        current = list[0]
     
    option = select.select(xbmc.getLocalizedString(21448), menu, current)

    if option < 0:
        return

    language = menu[option][0]

    if (language == current) and (len(list) == 1):
        return

    setSetting(setting, [language])
    execute('Skin.SetBool(SubtitleDownloadSet)')
    refreshSkinString(setting)


def doSetSubtitlePreferred():
    import select
    menu = []

    original = xbmc.getLocalizedString(308)
    default  = xbmc.getLocalizedString(309)

    setting = 'locale.subtitlelanguage'

    file = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'subtitle.txt'))

    options = []
    try:        
        f       = open(file, 'r')
        options = f.readlines()
        f.close()
    except:
        return
   
    options = sorted(options, key=str.lower)

    menu.append([original, 0])
    menu.append([default,  1])

    idx = 2

    for option in options:
        exec(option)
        menu.append([option, idx])
        idx += 1

    current = getSetting(setting)

    if current == 'original':
        current = original
    elif current == 'default':
        current = default

    option = select.select(xbmc.getLocalizedString(286), menu, current)

    if option < 0:
        return

    if option == 0:
        language = 'original'
    elif option == 1:
        language = 'default'
    else:
        language = menu[option][0]

    if language == current:
        return

    setSetting(setting, language)
    execute('Skin.SetBool(SubtitlePreferredSet)')
    refreshSkinString(setting)


def doSetRegion():
    import select
    menu = []

    setting  = 'locale.country' #region

    language = getSetting('locale.language')
    text     = getLanguage(language)

    if not text:
        return

    import re

    theRegions = []

    regions = re.compile('<region name="(.+?)"').findall(text)
    for region in regions:
        theRegions.append(region)

    regions = re.compile('<region locale="(.+?)">').findall(text)
    for region in regions:
        theRegions.append(region)

    theRegions.sort()

    for idx, region in enumerate(theRegions):
        menu.append([region, idx])

    if len(menu) < 1:
        return

    current = getSetting(setting)

    option = select.select(xbmc.getLocalizedString(20026), menu, current)

    if option < 0:
        return

    region = menu[option][0]

    if region == current:
        return

    setSetting(setting, region)
    execute('Skin.SetBool(RegionSet)')
    refreshSkinString(setting)


def zoom(up):
    setting = 'lookandfeel.skinzoom'
    value   = getSetting(setting)

    if (up):
        value += 2
    else:
        value -= 2

    if value > 20:
        value = -20

    if value < -20:
        value = 20    

    setSetting(setting, value)
    refreshSkinString(setting)

def refresh():
    refreshSkinString('locale.language')
    refreshSkinString('locale.subtitlelanguage')
    refreshSkinString('locale.country')
    refreshSkinString('locale.timezonecountry')
    refreshSkinString('locale.timezone')
    refreshSkinString('lookandfeel.skinzoom')
    refreshSkinString('subtitles.languages')
    refreshSkinString('subtitles.charset')

    firmware = xbmcaddon.Addon('script.tlbb').getSetting('cVersion').replace('\r', '').replace('\n', '')
    xbmc.executebuiltin('Skin.SetString(%s,%s)' % ('firmware', firmware))

    setting = 'lookandfeel.skin'
    skin    = getSetting(setting)
    if skin:
        if skin.startswith('skin.'):
            skin = skin[5:]
        xbmc.executebuiltin('Skin.SetString(%s,%s)' % (setting, skin))


def refreshSkinString(setting):
    value = getSetting(setting)

    if isinstance(value, list):
        value = str(value[0])
    else:
        value = str(value)

    if setting == 'subtitles.charset':
        charsets = getCharsets()
        for charset in charsets:
            if value == charset[1]:
                xbmc.executebuiltin('Skin.SetString(%s,%s)' % (setting, charset[0]))
                break
        return

    if setting == 'locale.timezonecountry' and len(value) == 0:
        value = 'Default'

    if value:
        xbmc.executebuiltin('Skin.SetString(%s,%s)' % (setting, value))
    else:
        xbmc.executebuiltin('Skin.Reset(%s)' % setting)


if __name__ == '__main__':
    try: main()
    except Exception, e:
        log('ERROR IN SCRIPT - %s' % str(e))