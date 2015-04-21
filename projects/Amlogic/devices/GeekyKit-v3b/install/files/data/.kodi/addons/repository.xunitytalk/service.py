import urllib , urllib2 , sys , re , xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
oo000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , '' ) )
ii = os . path . join ( oo000 , 'plugin.video.aaastream' , 'addon.xml' )
oOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
def IIi1IiiiI1Ii ( directory , name ) :
 import glob
 I11i11Ii = xbmc . translatePath ( os . path . join ( directory , name ) )
 for oO00oOo in glob . glob ( I11i11Ii ) :
  OOOo0 = oO00oOo
  os . remove ( oO00oOo )
def Oooo000o ( name ) :
 if os . path . exists ( name ) == True :
  for IiIi11iIIi1Ii , Oo0O , IiI in os . walk ( name ) :
   for ooOo in IiI :
    try :
     os . unlink ( os . path . join ( IiIi11iIIi1Ii , ooOo ) )
    except :
     pass
   for Oo in Oo0O :
    try :
     os . unlink ( os . path . join ( IiIi11iIIi1Ii , Oo ) )
    except :
     pass
  try :
   os . rmdir ( name )
  except :
   pass
   if 67 - 67: O00ooOO . I1iII1iiII
iI1Ii11111iIi = 'plugin.video.aaastream'
IIi1IiiiI1Ii ( oOOo , iI1Ii11111iIi + '*' )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons' , iI1Ii11111iIi ) )
Oooo000o ( i1i1II )
import time
time . sleep ( 2 )
xbmc . executebuiltin ( 'UpdateLocalAddons' )
xbmc . executebuiltin ( 'UpdateAddonRepos' )
if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
if 56 - 56: ooO00oOoo - O0OOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
