TITLE = "Ask A Ninja"
RSS_FEED = 'http://askaninja.blip.tv/rss'
NS = {'blip':'http://blip.tv/dtd/blip/1.0', 'media':'http://search.yahoo.com/mrss/'}
ART = 'art-default.jpg'
ICON = 'icon-default.png'
ICON_SEARCH = 'icon-search.png'

def Start(): # Initialize the plug-in
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

# Setup the default attributes for the ObjectContainer
ObjectContainer.title1 = TITLE
ObjectContainer.view_group = 'List'
ObjectContainer.art = R(ART)

# Setup the default attributes for the other objects
DirectoryObject.thumb = R(ICON)
DirectoryObject.art = R(ART)
VideoClipObject.thumb = R(ICON)
VideoClipObject.art = R(ART)

#############################################################################################
@handler('/video/askaninja', TITLE)
def MainMenu():
    oc = ObjectContainer()
    return oc
