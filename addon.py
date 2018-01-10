import xbmcaddon
import xbmcplugin
import xbmcgui
import sys
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello World! 11"
line2 = "We can write anything we want here"
line3 = ", ".join(sys.argv)

handle = int(sys.argv[1])
 
# xbmcgui.Dialog().ok(addonname, line1, line2, line3)

xbmcplugin.addDirectoryItems(handle, [
    (sys.argv[0] + "?a", xbmcgui.ListItem(label="a"), False),
    (sys.argv[0] + "?b", xbmcgui.ListItem(label="b"), False),
])
xbmcplugin.endOfDirectory(handle)
