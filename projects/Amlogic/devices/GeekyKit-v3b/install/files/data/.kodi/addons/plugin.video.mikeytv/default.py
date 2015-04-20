import urllib , urllib2 , sys , re , xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import net
if 73 - 73: II111iiii
net = net . Net ( )
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = xbmcaddon . Addon ( id = 'plugin.video.mikeytv' )
o0OOO = xbmc . translatePath ( I1IiI . getAddonInfo ( 'profile' ) )
iIiiiI = os . path . join ( o0OOO , "world" )
if os . path . exists ( o0OOO ) == False :
 os . makedirs ( o0OOO )
 if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
 if 68 - 68: o00ooo0 / Oo00O0
 if 66 - 66: oO0o0ooO0
 if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - iii1II11ii
def ooO00oOoo ( ) :
 #O0OOo ( '[COLOR orange]New World Tv[/COLOR]' , 'url' , 500 , '' , '' )
 O0OOo ( '[COLOR red]Iptv Blogs[/COLOR]' , 'url' , 300 , '' , '' )
 O0OOo ( '[COLOR gold]Vdubt25[/COLOR]' , 'url' , 400 , '' , '' )
 O0OOo ( '[COLOR cyan]I-PTV[/COLOR]' , 'url' , 300 , '' , '' )
 O0OOo ( '[COLOR green]HasBahCa IPTV[/COLOR]' , 'url' , 300 , '' , '' )
 O0OOo ( '[COLOR purple]Wois IPTV[/COLOR]' , 'http://whois.india.dj/source/sobhytv.com/sp.html' , 1 , '' , '' )
 O0OOo ( '[COLOR blue]Pac 12[/COLOR]' , 'pac12' , 2 , '' , '' )
 O0OOo ( '[COLOR limegreen]Nile Sat[/COLOR]' , 'nilesattv' , 2 , '' , '' )
 if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . iiIIIII1i1iI / iiIIIII1i1iI % iiIIIII1i1iI
 if 22 - 22: ii1II11I1ii1I . iiIIIII1i1iI
 if 41 - 41: o00ooo0 . Oo00O0 * iiIIIII1i1iI % i11iIiiIii
def o000o0o00o0Oo ( name ) :
 if 80 - 80: OoooooooOO . I1IiiI
 if 'Iptv Blogs' in name :
  if 87 - 87: iii1II11ii / Oo00O0 + o00ooo0 - Oo00O0 . Oo00O0 / II111iiii
  iiIIIIi1i1 = [ 'iptv-xbmc' , 'iptv-tv' , 'i-ptv' ]
  for O0OoOoo00o in iiIIIIi1i1 :
   O0OOo ( O0OoOoo00o . upper ( ) , O0OoOoo00o , 4 , '' , '' )
  try :
   iiiI11 = OOooO ( 'http://tvonlinestreams.com' ) . replace ( '\t' , '' ) . replace ( '\n' , '' ) . replace ( '#EXTM3U' , '' )
   OOoO00o = re . compile ( '<div class="entry-summary clearfix">(.+?)<a' , re . DOTALL ) . findall ( iiiI11 )
   if 9 - 9: I1IiiI - ii1II11I1ii1I % i1IIi % OoooooooOO
   for i1iIIi1 in OOoO00o :
    if 50 - 50: i11iIiiIii - ii1II11I1ii1I
    oo0Ooo0 = i1iIIi1 . strip ( ) . split ( '#EXTINF:' )
    for I1I11I1I1I in oo0Ooo0 :
     if 90 - 90: II111iiii + iii1II11ii / o0oOOo0O0Ooo % II111iiii - O0
     if 'raw=' in I1I11I1I1I :
      name = I1I11I1I1I . split ( 'rtmp://' ) [ 0 ]
      name = name . replace ( '0,' , '' ) . replace ( '-1,' , '' ) . replace ( '-2,' , '' )
      iIii1 = I1I11I1I1I . split ( 'raw=' ) [ 1 ]
      O0OOo ( name . title ( ) . strip ( ) , iIii1 , 200 , '' , '' )
     elif 'http:' in I1I11I1I1I :
      name = I1I11I1I1I . split ( 'http://' ) [ 0 ]
      name = name . replace ( '0,' , '' ) . replace ( '-1,' , '' ) . replace ( '-2,' , '' )
      iIii1 = 'http://' + I1I11I1I1I . split ( 'http://' ) [ 1 ]
      O0OOo ( name . title ( ) . strip ( ) , iIii1 , 200 , '' , '' )
      if 71 - 71: OoO0O00
      if 55 - 55: OoO0O00 / I1ii11iIi11i * i11iII1iiI
      if 86 - 86: i11iIiiIii + ii1II11I1ii1I + Oo00O0 * iI1Ii11111iIi + o0oOOo0O0Ooo
      if 61 - 61: OoO0O00 / i11iIiiIii
  except : pass
  #addDir('Sky','skypackage',2,'','')  
  #addDir('Canal +','upplusliga',2,'','')
  if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
  if 65 - 65: OoOoOO00
 if 'I-PTV' in name :
  ii1I = 'http://i-ptv.blogspot.co.uk/2014/04/iptv-m3u-list.html'
  iiiI11 = OOooO ( ii1I )
  if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * ii1II11I1ii1I - i11iII1iiI
  OOoO00o = re . compile ( '<a href="(.+?)">.+?/a>(.+?)<' ) . findall ( iiiI11 )
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % i11iII1iiI / OoooooooOO % iii1II11ii
  for iIii1 , name in OOoO00o :
   name = name . strip ( )
   O0OOo ( name . title ( ) + '[COLOR cyan] I-PTV[/COLOR]' , iIii1 , 1 , '' , '' )
   if 75 - 75: oO0o0ooO0
 if 'HasBahCa' in name :
  ii1I = 'http://01.gen.tr/iptv/'
  iiiI11 = OOooO ( ii1I )
  if 97 - 97: i11iIiiIii
  OOoO00o = re . compile ( '<h3 onclick="GetCntry\(\'(.+?)\'\)">(.+?)</h3>' ) . findall ( iiiI11 )
  if 32 - 32: Oo0Ooo * O0 % iii1II11ii % ii1II11I1ii1I . iiIIIII1i1iI
  for iIii1 , name in OOoO00o :
   iIii1 = ii1I + 'server.php?what=cntrychanns&cat=' + iIii1
   O0OOo ( name . title ( ) + '[COLOR green] HasBahCa IPTV[/COLOR]' , iIii1 , 3 , '' , '' )
   if 61 - 61: Oo00O0
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 79 - 79: Oo0Ooo + I1IiiI - oO0o0ooO0
 if 83 - 83: Oo00O0
def OO00o0OOO0 ( ) :
 if 27 - 27: O0 % i1IIi * iii1II11ii + i11iIiiIii + OoooooooOO * i1IIi
 import json
 iiiI11 = open ( iIiiiI ) . read ( )
 o0oo0o0O00OO = json . loads ( iiiI11 )
 o0oO = [ ]
 for I1i1iii in o0oo0o0O00OO :
  i1iiI11I = I1i1iii [ 'categoryName' ]
  iiii = I1i1iii [ 'categoryImageLink' ]
  if i1iiI11I not in o0oO :
   o0oO . append ( i1iiI11I )
   if 54 - 54: I1ii11iIi11i * i11iII1iiI
   O0OOo ( i1iiI11I , 'url' , 501 , iiii , '' )
   if 13 - 13: iiIIIII1i1iI + OoOoOO00 - OoooooooOO + o00ooo0 . oO0o0ooO0 + OoO0O00
   if 8 - 8: iIii1I11I1II1 . I1IiiI - iIii1I11I1II1 * ii1II11I1ii1I
   if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + Oo00O0 * iii1II11ii / iii1II11ii
def OoOo ( name ) :
 iI = name
 import json
 iiiI11 = open ( iIiiiI ) . read ( )
 o0oo0o0O00OO = json . loads ( iiiI11 )
 for I1i1iii in o0oo0o0O00OO :
  iiii = I1i1iii [ 'channelImageLink' ]
  name = I1i1iii [ 'channelName' ]
  iIii1 = I1i1iii [ 'channelLink' ]
  if iI in I1i1iii [ 'categoryName' ] :
   o00O ( name , iIii1 , iiii )
   if 69 - 69: iii1II11ii % o00ooo0 - o0oOOo0O0Ooo + o00ooo0 - O0 % OoooooooOO
   if 31 - 31: II111iiii - i11iII1iiI . o00ooo0 % OoOoOO00 - O0
def iii11 ( url ) :
 print url
 O0oo0OO0oOOOo = url
 if 35 - 35: iiIIIII1i1iI % I1IiiI
 iiiI11 = OOooO ( url )
 if 70 - 70: oO0o0ooO0 * I1ii11iIi11i
 iiiI11 = iiiI11 . replace ( '\r' , '\n' ) . replace ( '\n\n' , '\n' ) . replace ( '<br />' , '\n' ) . replace ( '\n\n' , '\n' )
 if 46 - 46: Oo00O0 / OoO0O00
 if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + ii1II11I1ii1I + ii1II11I1ii1I - o0oOOo0O0Ooo / o00ooo0
 OOoO00o = re . compile ( '#EXTINF:(.+?)\n(.+?)\n' ) . findall ( iiiI11 )
 if 44 - 44: Oo00O0 . i1IIi - I1ii11iIi11i . O0 - Oo00O0
 for i1iiI11I , url in OOoO00o :
  if 92 - 92: oO0o0ooO0 . iI1Ii11111iIi + o0oOOo0O0Ooo
  if 'http-user-agent=' in url :
   return IiII1I11i1I1I ( O0oo0OO0oOOOo )
  else :
   i1iiI11I = i1iiI11I . replace ( '0,' , '' ) . replace ( '-1,' , '' ) . replace ( '-2,' , '' )
   if '</pre>' in url :
    url = url . split ( '</pre>' ) [ 0 ]
   if not 'HasBahCa IPTV' in i1iiI11I :
    if 'group-title' in i1iiI11I :
     i1iiI11I = i1iiI11I . split ( ',' ) [ 1 ]
    if not '[COLOR' in i1iiI11I :
     i1iiI11I = i1iiI11I . title ( ) . strip ( ) . replace ( '-1:' , '' )
     if 83 - 83: I1ii11iIi11i / Oo00O0
    O0OOo ( i1iiI11I , url , 200 , '' , '' )
    if 49 - 49: o0oOOo0O0Ooo
    if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
    if 78 - 78: iI1Ii11111iIi
def IiII1I11i1I1I ( url ) :
 print '#####################'
 iiiI11 = OOooO ( url )
 if 71 - 71: i11iII1iiI + Oo00O0 % i11iIiiIii + I1ii11iIi11i - iiIIIII1i1iI
 iiiI11 = iiiI11 . replace ( '\r' , '\n' ) . replace ( '\n\n' , '\n' ) . replace ( '<br />' , '\n' ) . replace ( '\n\n' , '\n' )
 if 88 - 88: OoOoOO00 - OoO0O00 % i11iII1iiI
 OOoO00o = re . compile ( '#EXTINF:(.+?)\n.+?EXTVLCOPT:http-user-agent="(.+?)"\n(.+?)\n' ) . findall ( iiiI11 )
 if 16 - 16: I1IiiI * iii1II11ii % iiIIIII1i1iI
 for i1iiI11I , Oo000o , url in OOoO00o :
  i1iiI11I = i1iiI11I . replace ( '0,' , '' ) . replace ( '-1,' , '' ) . replace ( '-2,' , '' )
  if '</pre>' in url :
   url = url . split ( '</pre>' ) [ 0 ]
  url = url + '?|User-Agent=' + Oo000o
  O0OOo ( i1iiI11I . title ( ) , url , 200 , '' , '' )
  if 7 - 7: Oo00O0 * OoO0O00 % iii1II11ii . iiIIIII1i1iI
  if 45 - 45: i11iIiiIii * II111iiii % iIii1I11I1II1 + I1ii11iIi11i - ii1II11I1ii1I
  if 17 - 17: iiIIIII1i1iI
def ooOooo000oOO ( url ) :
 ii1I = 'http://01.gen.tr/iptv/'
 iiiI11 = OOooO ( url )
 if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 if 58 - 58: II111iiii * i11iII1iiI * I1ii11iIi11i / i11iII1iiI
 if 75 - 75: iii1II11ii
 if 50 - 50: ii1II11I1ii1I / Oo0Ooo - iii1II11ii - iI1Ii11111iIi % oO0o0ooO0 - iii1II11ii
 OOoO00o = re . compile ( 'onclick="Play\(\'(.+?)\'\)".+?>(.+?)<' ) . findall ( iiiI11 )
 for url , i1iiI11I in OOoO00o :
  url = ii1I + 'server.php?what=play&cat=' + url
  if 91 - 91: OoO0O00 / iI1Ii11111iIi - II111iiii . iI1Ii11111iIi
  O0OOo ( i1iiI11I . title ( ) , url , 200 , '' , '' )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 18 - 18: o0oOOo0O0Ooo
 if 98 - 98: oO0o0ooO0 * oO0o0ooO0 / oO0o0ooO0 + iI1Ii11111iIi
def ii111111I1iII ( url ) :
 O0oo0OO0oOOOo = 'http://%s.blogspot.com/feeds/posts/default' % url
 if 68 - 68: oO0o0ooO0 - iIii1I11I1II1 * i11iIiiIii / I1ii11iIi11i * o00ooo0
 iiiI11 = OOooO ( O0oo0OO0oOOOo )
 if 23 - 23: oO0o0ooO0
 if 91 - 91: iIii1I11I1II1 + o00ooo0
 if 31 - 31: iiIIIII1i1iI . OoOoOO00 . i11iII1iiI
 if 75 - 75: iI1Ii11111iIi + OoO0O00 . OoOoOO00 . Oo00O0 + Oo0Ooo . OoO0O00
 OOoO00o = re . compile ( '<category term="(.+?)"' ) . findall ( iiiI11 )
 for i1iiI11I in OOoO00o :
  if 96 - 96: i11iII1iiI . Oo00O0 - Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * i11iII1iiI
  O0OOo ( i1iiI11I , url , 5 , '' , '' )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 65 - 65: ii1II11I1ii1I . iIii1I11I1II1 / O0 - ii1II11I1ii1I
 if 21 - 21: I1IiiI * iIii1I11I1II1
def oooooOoo0ooo ( name , url ) :
 url = 'http://%s.blogspot.co.uk/search/label/%s' % ( url , name . replace ( ' ' , '%20' ) )
 print url
 iiiI11 = OOooO ( url )
 if 6 - 6: iI1Ii11111iIi - ii1II11I1ii1I + iIii1I11I1II1 - o00ooo0 - i11iIiiIii
 if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
 if 61 - 61: II111iiii
 if 64 - 64: Oo00O0 / OoOoOO00 - O0 - iI1Ii11111iIi
 if 86 - 86: iI1Ii11111iIi % OoOoOO00 / I1IiiI / OoOoOO00
 OOoO00o = re . compile ( "<h3 class='post-title entry-title'.+?href='(.+?)'>(.+?)</a>" , re . DOTALL ) . findall ( iiiI11 )
 for url , name in OOoO00o :
  url = url . replace ( '</div>' , '' )
  O0OOo ( name , url . strip ( ) , 1 , '' , '' )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 42 - 42: OoO0O00
 if 67 - 67: o00ooo0 . oO0o0ooO0 . O0
 if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / i11iII1iiI + ii1II11I1ii1I
 if 87 - 87: iii1II11ii * I1ii11iIi11i + i11iII1iiI / iIii1I11I1II1 / oO0o0ooO0
def I1111IIi ( url ) :
 if 'tvonlinestreams' in url :
  print url
  iiiI11 = OOooO ( url )
  OOoO00o = re . compile ( '<div class="entry-summary clearfix">(.+?) <a' ) . findall ( iiiI11 )
  for i1iIIi1 in OOoO00o :
   if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
   oo0Ooo0 = i1iIIi1 . split ( '#EXTINF:-1,' )
   for I1I11I1I1I in oo0Ooo0 :
    if 'http:' in I1I11I1I1I :
     i1iiI11I = I1I11I1I1I . split ( 'http://' ) [ 0 ]
     url = 'http://' + I1I11I1I1I . split ( 'http://' ) [ 1 ]
    else :
     i1iiI11I = I1I11I1I1I . split ( 'rtmp://$OPT:rtmp-raw=' ) [ 0 ]
     url = I1I11I1I1I . split ( 'rtmp://$OPT:rtmp-raw=' ) [ 1 ]
     if 15 - 15: iI1Ii11111iIi . OoO0O00 / Oo0Ooo + iI1Ii11111iIi
    for i1iiI11I , url in OOoO00o :
     O0OOo ( i1iiI11I . title ( ) , url , 200 , '' , '' )
     if 78 - 78: O0 . iii1II11ii . II111iiii % i11iII1iiI
     if 49 - 49: ii1II11I1ii1I / OoO0O00 . II111iiii
 ooOOoooooo = OOooO ( 'http://skylive.k30.us/' + url + '.php' )
 if 'document.write' in ooOOoooooo :
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % oO0o0ooO0 * iiIIIII1i1iI . i11iIiiIii
  iiiI11 = urllib . unquote_plus ( re . compile ( "document.write\(unescape\('(.+?)'\)" ) . findall ( ooOOoooooo ) [ 0 ] )
 else :
  iiiI11 = ooOOoooooo
 if 'playlist: ' in iiiI11 :
  if 2 - 2: I1ii11iIi11i * iI1Ii11111iIi - iIii1I11I1II1 + I1IiiI . iii1II11ii % oO0o0ooO0
  OOoO00o = re . compile ( 'file: "(.+?)".+?image: "(.+?)".+?title: "(.+?)"' , re . DOTALL ) . findall ( iiiI11 )
  for url , iiii , i1iiI11I in OOoO00o :
   if not 'Main Page' in i1iiI11I . title ( ) :
    O0OOo ( i1iiI11I . title ( ) , url , 201 , iiii , '' )
 else :
  OOoO00o = re . compile ( 'img src="(.+?)" border="0" height="40" width="40">.+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iiiI11 )
  for iiii , url , i1iiI11I in OOoO00o :
   if not 'Main Page' in i1iiI11I . title ( ) :
    O0OOo ( i1iiI11I . title ( ) , url , 201 , iiii , '' )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 92 - 92: oO0o0ooO0
 if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
def OOooO ( url ) :
 II111iiiI1Ii = urllib2 . Request ( url )
 II111iiiI1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O0OOO0Ooo = urllib2 . urlopen ( II111iiiI1Ii )
 iiiI11 = o0O0OOO0Ooo . read ( )
 o0O0OOO0Ooo . close ( )
 return iiiI11
 if 45 - 45: O0 / o0oOOo0O0Ooo
def i1 ( ) :
 IIIII11I1IiI = xbmcgui . Dialog ( )
 IIIII11I1IiI . ok ( 'World Tv' , 'Sorry Channel is Down' , "" , "Try Another Channel" )
 if 16 - 16: iIii1I11I1II1
 if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
 if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + ii1II11I1ii1I
def o0o ( name ) :
 xbmc . executebuiltin ( 'ActivateWindow(videos,plugin://plugin.video.vdubt)' )
 if 73 - 73: iiIIIII1i1iI * I1ii11iIi11i + I1IiiI . Oo00O0
def o0oO00000 ( name , url , iconimage ) :
 OOOOoo0Oo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 OOOOoo0Oo . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
 OOOOoo0Oo . setProperty ( "IsPlayable" , "true" )
 if 14 - 14: oO0o0ooO0
 if '/up' in url :
  if 11 - 11: iiIIIII1i1iI * I1IiiI . iIii1I11I1II1 % OoooooooOO + oO0o0ooO0
  OOO = OOooO ( url . replace ( '/up' , '/' ) )
  if 68 - 68: II111iiii + iI1Ii11111iIi
  if 45 - 45: oO0o0ooO0 / oO0o0ooO0 + o00ooo0 + Oo00O0
  if 'http://www.videolan.org' in OOO :
   OOoO00o = re . compile ( 'target="(.+?)"' ) . findall ( OOO ) [ 0 ]
   OOoO00o = OOoO00o . replace ( 'http://luxtivi.k18.us' , 'http://skylive.k30.us/' )
   OOO = OOooO ( OOoO00o )
   O0oo0OO0oOOOo = 'http://' + OOO . split ( 'http://' ) [ 1 ] + '?|User-Agent=Lavf53.32.100'
 else :
  if 47 - 47: o0oOOo0O0Ooo + Oo00O0
  O0oo0OO0oOOOo = url
  if 82 - 82: II111iiii . iiIIIII1i1iI - iIii1I11I1II1 - iiIIIII1i1iI * II111iiii
  if 77 - 77: iIii1I11I1II1 * OoO0O00
 OOOOoo0Oo . setPath ( O0oo0OO0oOOOo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoo0Oo )
 if 95 - 95: I1IiiI + i11iIiiIii
 if 6 - 6: Oo00O0 / i11iIiiIii + oO0o0ooO0 * iii1II11ii
 if 80 - 80: II111iiii
def O0O ( name , url , iconimage ) :
 OOOOoo0Oo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 OOOOoo0Oo . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
 OOOOoo0Oo . setProperty ( "IsPlayable" , "true" )
 if 1 - 1: II111iiii
 if 'rtmp' in url :
  if not 'timeout=' in url :
   url = url + ' timeout=10'
   if 84 - 84: o0oOOo0O0Ooo % II111iiii . i11iIiiIii / OoO0O00
 if '/up' in url :
  OOO = OOooO ( url . replace ( '/up' , '/' ) )
  if 80 - 80: o00ooo0 . i11iIiiIii - o0oOOo0O0Ooo
  if 25 - 25: OoO0O00
  if 'http://www.videolan.org' in OOO :
   OOoO00o = re . compile ( 'target="(.+?)"' ) . findall ( OOO ) [ 0 ]
   OOO = OOooO ( OOoO00o )
   O0oo0OO0oOOOo = 'http://' + OOO . split ( 'http://' ) [ 1 ] + '?|User-Agent=Lavf53.32.100'
 else :
  if 62 - 62: i11iII1iiI + O0
  O0oo0OO0oOOOo = url
  if 98 - 98: o0oOOo0O0Ooo
 if 'server.php?' in url :
  print 'opening'
  OOO = OOooO ( url )
  if 'value="' in OOO :
   OOOO0oo0 = 'value="(.+?)"'
  else :
   OOOO0oo0 = 'src="(.+?)"'
  try :
   O0oo0OO0oOOOo = re . compile ( OOOO0oo0 ) . findall ( OOO ) [ 0 ]
   print '#######################'
   print O0oo0OO0oOOOo
   if 'youtube' in O0oo0OO0oOOOo :
    return i1 ( )
  except :
   return i1 ( )
   if 35 - 35: ii1II11I1ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % ii1II11I1ii1I
 else :
  if 47 - 47: oO0o0ooO0 - ii1II11I1ii1I . II111iiii + OoooooooOO . i11iIiiIii
  O0oo0OO0oOOOo = url
 if 'raw=' in O0oo0OO0oOOOo :
  O0oo0OO0oOOOo = O0oo0OO0oOOOo . split ( 'raw=' ) [ 1 ]
 OOOOoo0Oo . setPath ( O0oo0OO0oOOOo . replace ( 'amp;' , '' ) . replace ( '/>' , '' ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoo0Oo )
 if 94 - 94: o0oOOo0O0Ooo * ii1II11I1ii1I / Oo0Ooo / ii1II11I1ii1I
 if 87 - 87: Oo0Ooo . iiIIIII1i1iI
 if 75 - 75: Oo00O0 + OoOoOO00 + o0oOOo0O0Ooo * iI1Ii11111iIi % iii1II11ii . oO0o0ooO0
 if 55 - 55: i11iII1iiI . I1IiiI
 if 61 - 61: Oo0Ooo % iiIIIII1i1iI . Oo0Ooo
 if 100 - 100: o00ooo0 * O0
def o00oO0oo0OO ( ) :
 O0O0OOOOoo = [ ]
 oOooO0 = sys . argv [ 2 ]
 if len ( oOooO0 ) >= 2 :
  Ii1I1Ii = sys . argv [ 2 ]
  OOoO0 = Ii1I1Ii . replace ( '?' , '' )
  if ( Ii1I1Ii [ len ( Ii1I1Ii ) - 1 ] == '/' ) :
   Ii1I1Ii = Ii1I1Ii [ 0 : len ( Ii1I1Ii ) - 2 ]
  OO0Oooo0oOO0O = OOoO0 . split ( '&' )
  O0O0OOOOoo = { }
  for o00O0 in range ( len ( OO0Oooo0oOO0O ) ) :
   oOO0O00Oo0O0o = { }
   oOO0O00Oo0O0o = OO0Oooo0oOO0O [ o00O0 ] . split ( '=' )
   if ( len ( oOO0O00Oo0O0o ) ) == 2 :
    O0O0OOOOoo [ oOO0O00Oo0O0o [ 0 ] ] = oOO0O00Oo0O0o [ 1 ]
    if 13 - 13: OoooooooOO
 return O0O0OOOOoo
 if 33 - 33: o00ooo0 + oO0o0ooO0 * iii1II11ii / iIii1I11I1II1 - I1IiiI
def O0OOo ( name , url , mode , iconimage , description ) :
 O0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 OO0ooOOO0OOO = True
 OOOOoo0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOoo0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oooOOoOo0 = [ ]
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 if mode == 200 or mode == 201 :
  OOOOoo0Oo . setProperty ( "IsPlayable" , "true" )
  if 62 - 62: OoooooooOO * I1IiiI
  OO0ooOOO0OOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0oO , listitem = OOOOoo0Oo , isFolder = False )
 else :
  oO00oooOOoOo0 . append ( ( 'Play All Videos' , 'XBMC.RunPlugin(%s?name=%s&mode=2001&iconimage=None&url=%s)' % ( sys . argv [ 0 ] , name , url ) ) )
  OOOOoo0Oo . addContextMenuItems ( items = oO00oooOOoOo0 , replaceItems = False )
  xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0oO , listitem = OOOOoo0Oo , isFolder = True )
 return OO0ooOOO0OOO
 if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 if 50 - 50: o00ooo0 . o0oOOo0O0Ooo
def o00O ( name , url , iconimage ) :
 OOOOoo0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OOOOoo0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOOOoo0Oo . setProperty ( "IsPlayable" , "true" )
 OO0ooOOO0OOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OOOOoo0Oo , isFolder = False )
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * iI1Ii11111iIi * ii1II11I1ii1I
 if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
def o0o0O0O00oOOo ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1IiI . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1IiI . getSetting ( viewType ) )
  if 14 - 14: OoOoOO00 + iii1II11ii
  if 52 - 52: OoooooooOO - Oo00O0
Ii1I1Ii = o00oO0oo0OO ( )
iIii1 = None
i1iiI11I = None
o0O0o0 = None
iiii = None
II111iI111I1I = None
if 18 - 18: oO0o0ooO0 - i11iII1iiI . o00ooo0 . iIii1I11I1II1
if 2 - 2: i11iII1iiI . OoO0O00
try :
 iIii1 = urllib . unquote_plus ( Ii1I1Ii [ "url" ] )
except :
 pass
try :
 i1iiI11I = urllib . unquote_plus ( Ii1I1Ii [ "name" ] )
except :
 pass
try :
 iiii = urllib . unquote_plus ( Ii1I1Ii [ "iconimage" ] )
except :
 pass
try :
 o0O0o0 = int ( Ii1I1Ii [ "mode" ] )
except :
 pass
try :
 II111iI111I1I = urllib . unquote_plus ( Ii1I1Ii [ "description" ] )
except :
 pass
 if 78 - 78: iI1Ii11111iIi * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / o00ooo0
print "Mode: " + str ( o0O0o0 )
print "URL: " + str ( iIii1 )
print "Name: " + str ( i1iiI11I )
print "IconImage: " + str ( iiii )
if 35 - 35: iI1Ii11111iIi % i11iII1iiI - iii1II11ii
if 20 - 20: i1IIi - Oo00O0
if 30 - 30: iI1Ii11111iIi / I1IiiI
if o0O0o0 == None or iIii1 == None or len ( iIii1 ) < 1 :
 print ""
 ooO00oOoo ( )
 if 35 - 35: II111iiii % i11iII1iiI . Oo00O0 + Oo00O0 % II111iiii % II111iiii
elif o0O0o0 == 1 :
 iii11 ( iIii1 )
 if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
elif o0O0o0 == 2 :
 I1111IIi ( iIii1 )
 if 94 - 94: iii1II11ii . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
elif o0O0o0 == 3 :
 ooOooo000oOO ( iIii1 )
 if 72 - 72: ii1II11I1ii1I
elif o0O0o0 == 4 :
 ii111111I1iII ( iIii1 )
 if 1 - 1: OoO0O00 * iiIIIII1i1iI * OoooooooOO + Oo00O0
elif o0O0o0 == 5 :
 oooooOoo0ooo ( i1iiI11I , iIii1 )
 if 33 - 33: O0 * o0oOOo0O0Ooo - o00ooo0 % o00ooo0
elif o0O0o0 == 300 :
 o000o0o00o0Oo ( i1iiI11I )
 if 18 - 18: o00ooo0 / Oo0Ooo * o00ooo0 + o00ooo0 * i11iIiiIii * I1ii11iIi11i
elif o0O0o0 == 400 :
 o0o ( i1iiI11I )
 if 11 - 11: Oo00O0 / OoOoOO00 - iiIIIII1i1iI * OoooooooOO + OoooooooOO . OoOoOO00
elif o0O0o0 == 500 :
 OO00o0OOO0 ( )
 if 26 - 26: ii1II11I1ii1I % I1ii11iIi11i
elif o0O0o0 == 501 :
 OoOo ( i1iiI11I )
 if 76 - 76: iiIIIII1i1iI * oO0o0ooO0
elif o0O0o0 == 200 :
 if 52 - 52: i11iII1iiI
 O0O ( i1iiI11I , iIii1 , iiii )
 if 19 - 19: I1IiiI
elif o0O0o0 == 201 :
 if 25 - 25: ii1II11I1ii1I / Oo00O0
 o0oO00000 ( i1iiI11I , iIii1 , iiii )
 if 31 - 31: i11iII1iiI . O0 % I1IiiI . o0oOOo0O0Ooo + iiIIIII1i1iI
elif o0O0o0 == 2001 :
 if 71 - 71: o00ooo0 . II111iiii
 playall ( i1iiI11I , iIii1 )
 if 62 - 62: OoooooooOO . iI1Ii11111iIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
