#!/usr/bin/env python

"""
Embeds web videos using URLs.  For instance, if a URL to an youtube video is
found in the text submitted to markdown and it isn't enclosed in parenthesis
like a normal link in markdown, then the URL will be swapped with a embedded
youtube video.

All resulting HTML is XHTML Strict compatible.

>>> import markdown

Test Metacafe

>>> s = "http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/"
>>> markdown.markdown(s, ['video'])
u'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="423" src="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf" width="498"></iframe>\\n</p>'

Test Metacafe with arguments

>>> markdown.markdown(s, ['video(metacafe_width=500,metacafe_height=425)'])
u'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="425" src="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf" width="500"></iframe>\\n</p>'

Test Link To Metacafe

>>> s = "[Metacafe link](http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/)"
>>> markdown.markdown(s, ['video'])
u'<p><a href="http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/">Metacafe link</a></p>'


Test Markdown Escaping

>>> s = "\\http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/"
>>> markdown.markdown(s, ['video'])
u'<p>http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</p>'
>>> s = "`http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/`"
>>> markdown.markdown(s, ['video'])
u'<p><code>http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</code></p>'


Test Youtube

>>> s = "http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"
>>> markdown.markdown(s, ['video'])
u'<p>\\n<div class="embed-responsive embed-responsive-16by9">\\n<iframe allowfullscreen="true" class="embed-responsive-item" frameborder="0" height="480" src="http://www.youtube.com/embed/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" width="853"></iframe>\\n</div>\\n</p>'


Test Youtube with argument

>>> markdown.markdown(s, ['video(youtube_width=200,youtube_height=100)'])
u'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="100" src="http://www.youtube.com/embed/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" width="200"></iframe>\\n</p>'


Test Youtube Link

>>> s = "[Youtube link](http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1)"
>>> markdown.markdown(s, ['video'])
u'<p><a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1">Youtube link</a></p>'


Test Dailymotion

>>> s = "http://www.dailymotion.com/relevance/search/ut2004/video/x3kv65_ut2004-ownage_videogames"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.dailymotion.com/swf/x3kv65_ut2004-ownage_videogames" height="405" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.dailymotion.com/swf/x3kv65_ut2004-ownage_videogames"></param><param name="allowFullScreen" value="true"></param></object></p>'


Test Dailymotion again (Dailymotion and their crazy URLs)

>>> s = "http://www.dailymotion.com/us/video/x8qak3_iron-man-vs-bruce-lee_fun"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.dailymotion.com/swf/x8qak3_iron-man-vs-bruce-lee_fun" height="405" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.dailymotion.com/swf/x8qak3_iron-man-vs-bruce-lee_fun"></param><param name="allowFullScreen" value="true"></param></object></p>'


Test Yahoo! Video

>>> s = "http://video.yahoo.com/watch/1981791/4769603"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40" height="322" type="application/x-shockwave-flash" width="512"><param name="movie" value="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40"></param><param name="allowFullScreen" value="true"></param><param name="flashVars" value="id=4769603&amp;vid=1981791"></param></object></p>'


Test Veoh Video

>>> s = "http://www.veoh.com/search/videos/q/mario#watch%3De129555XxCZanYD"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=e129555XxCZanYD" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=e129555XxCZanYD"></param><param name="allowFullScreen" value="true"></param></object></p>'


Test Veoh Video Again (More fun URLs)

>>> s = "http://www.veoh.com/group/BigCatRescuers#watch%3Dv16771056hFtSBYEr"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=v16771056hFtSBYEr" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=v16771056hFtSBYEr"></param><param name="allowFullScreen" value="true"></param></object></p>'


Test Veoh Video Yet Again (Even more fun URLs)

>>> s = "http://www.veoh.com/browse/videos/category/anime/watch/v181645607JyXPWcQ"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=v181645607JyXPWcQ" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=v181645607JyXPWcQ"></param><param name="allowFullScreen" value="true"></param></object></p>'


Test Vimeo Video

>>> s = "http://www.vimeo.com/1496152"
>>> markdown.markdown(s, ['video'])
u'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="480" src="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" width="850"></iframe>\\n</p>'


Test Vimeo Video with some GET values

>>> s = "http://vimeo.com/1496152?test=test"
>>> markdown.markdown(s, ['video'])
u'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="480" src="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" width="850"></iframe>\\n</p>'

Test Blip.tv

>>> s = "http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv" height="300" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv"></param><param name="allowFullScreen" value="true"></param></object></p>'

Test Gametrailers

>>> s = "http://www.gametrailers.com/video/console-comparison-borderlands/58079"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.gametrailers.com/remote_wrap.php?mid=58079" height="392" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.gametrailers.com/remote_wrap.php?mid=58079"></param><param name="allowFullScreen" value="true"></param></object></p>'
"""

import markdown

version = "0.1.6"

class VideoExtension(markdown.Extension):
    def __init__(self, configs):
        self.config = {
            'bliptv_width': ['480', 'Width for Blip.tv videos'],
            'bliptv_height': ['300', 'Height for Blip.tv videos'],
            'dailymotion_width': ['480', 'Width for Dailymotion videos'],
            'dailymotion_height': ['405', 'Height for Dailymotion videos'],
            'gametrailers_width': ['480', 'Width for Gametrailers videos'],
            'gametrailers_height': ['392', 'Height for Gametrailers videos'],
            'metacafe_width': ['498', 'Width for Metacafe videos'],
            'metacafe_height': ['423', 'Height for Metacafe videos'],
            'veoh_width': ['410', 'Width for Veoh videos'],
            'veoh_height': ['341', 'Height for Veoh videos'],
            'vimeo_width': ['850', 'Width for Vimeo videos'],
            'vimeo_height': ['480', 'Height for Vimeo videos'],
            'yahoo_width': ['512', 'Width for Yahoo! videos'],
            'yahoo_height': ['322', 'Height for Yahoo! videos'],
            #'youtube_width': ['853', 'Width for Youtube videos'],
            'youtube_width': ['', 'Width for Youtube videos'],
            #'youtube_height': ['480', 'Height for Youtube videos'],
            'youtube_height': ['', 'Height for Youtube videos'],
        }

        # Override defaults with user settings
        for key, value in configs:
            self.setConfig(key, value)

    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'bliptv', Bliptv,
            r'([^(]|^)http://(\w+\.|)blip.tv/file/get/(?P<bliptvfile>\S+.flv)')
        self.add_inline(md, 'dailymotion', Dailymotion,
            r'([^(]|^)http://www\.dailymotion\.com/(?P<dailymotionid>\S+)')
        self.add_inline(md, 'gametrailers', Gametrailers,
            r'([^(]|^)http://www.gametrailers.com/video/[a-z0-9-]+/(?P<gametrailersid>\d+)')
        self.add_inline(md, 'metacafe', Metacafe,
            r'([^(]|^)http://www\.metacafe\.com/watch/(?P<metacafeid>\S+)/')
        self.add_inline(md, 'veoh', Veoh,
            r'([^(]|^)http://www\.veoh\.com/\S*(#watch%3D|watch/)(?P<veohid>\w+)')
        self.add_inline(md, 'vimeo', Vimeo,
            r'([^(]|^)http(s?)://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(md, 'yahoo', Yahoo,
            r'([^(]|^)http(s?)://video\.yahoo\.com/watch/(?P<yahoovid>\d+)/(?P<yahooid>\d+)')
        self.add_inline(md, 'youtube', Youtube,
            r'([^(]|^)http(s?)://(www\.youtube\.com/watch\?\S*v=|youtu\.be/)(?P<youtubeargs>[A-Za-z0-9_&=-]+)\S*')

class Bliptv(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/%s' % m.group('bliptvfile')
        width = self.ext.config['bliptv_width'][0]
        height = self.ext.config['bliptv_height'][0]
        return flash_object(url, width, height)

class Dailymotion(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//www.dailymotion.com/swf/%s' % m.group('dailymotionid').split('/')[-1]
        width = self.ext.config['dailymotion_width'][0]
        height = self.ext.config['dailymotion_height'][0]
        return flash_object(url, width, height)

class Gametrailers(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//www.gametrailers.com/remote_wrap.php?mid=%s' % \
            m.group('gametrailersid').split('/')[-1]
        width = self.ext.config['gametrailers_width'][0]
        height = self.ext.config['gametrailers_height'][0]
        return flash_object(url, width, height)

class Metacafe(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//www.metacafe.com/fplayer/%s.swf' % m.group('metacafeid')
        width = self.ext.config['metacafe_width'][0]
        height = self.ext.config['metacafe_height'][0]
        return iframe_object(url, width, height)

class Veoh(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//www.veoh.com/videodetails2.swf?permalinkId=%s' % m.group('veohid')
        width = self.ext.config['veoh_width'][0]
        height = self.ext.config['veoh_height'][0]
        return flash_object(url, width, height)

class Vimeo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com' % m.group('vimeoid')
        width = self.ext.config['vimeo_width'][0]
        height = self.ext.config['vimeo_height'][0]
        return iframe_object(url, width, height)

class Yahoo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = "//d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40"
        width = self.ext.config['yahoo_width'][0]
        height = self.ext.config['yahoo_height'][0]
        obj = flash_object(url, width, height)
        param = markdown.util.etree.Element('param')
        param.set('name', 'flashVars')
        param.set('value', "id=%s&vid=%s" % (m.group('yahooid'),
                m.group('yahoovid')))
        obj.append(param)
        return obj

class Youtube(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = '//www.youtube.com/v/%s' % m.group('youtubeargs')
        url = '//www.youtube.com/embed/%s' % m.group('youtubeargs')
        width = self.ext.config['youtube_width'][0]
        height = self.ext.config['youtube_height'][0]
        #return flash_object(url, width, height)
        return iframe_object(url, width, height)

def flash_object(url, width, height):
        obj = markdown.util.etree.Element('object')
        obj.set('type', 'application/x-shockwave-flash')
        obj.set('width', width)
        obj.set('height', height)
        obj.set('data', url)
        param = markdown.util.etree.Element('param')
        param.set('name', 'movie')
        param.set('value', url)
        obj.append(param)
        param = markdown.util.etree.Element('param')
        param.set('name', 'allowFullScreen')
        param.set('value', 'true')
        obj.append(param)
        #param = markdown.util.etree.Element('param')
        #param.set('name', 'allowScriptAccess')
        #param.set('value', 'sameDomain')
        #obj.append(param)
        return obj

def iframe_object(url, width=None, height=None, frameborder='0', allowfullscreen='true', div_class='16by9'):
    """
    Must return something like
    <iframe width="853" height="480" src="https://www.youtube.com/embed/i5oJxea-BAo" frameborder="0" allowfullscreen></iframe>
    instead of
    <object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="344" type="application/x-shockwave-flash" width="425"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1"></param><param name="allowFullScreen" value="true"></param></object>
    """
    div = markdown.util.etree.Element('div')
    div.set('class', 'embed-responsive embed-responsive-%s' % div_class)
    iframe = markdown.util.etree.Element('iframe')
    iframe.set('width', width)
    iframe.set('height', height)
    iframe.set('src', url)
    iframe.set('allowfullscreen', allowfullscreen)
    iframe.set('frameborder', frameborder)
    iframe.set('class', 'embed-responsive-item')
    div.insert(0, iframe)
    return div

def makeExtension(configs=None) :
    return VideoExtension(configs=configs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
