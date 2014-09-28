python-markdown-video
=====================

Fork of https://code.google.com/p/python-markdown-video/


[Python Markdown Extension for Video](http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/)
===================================

I'm a big fan of markdown, especially the fact that it can be extended so easily. I wanted to give the users of DeathCat Inc. the ability to embed video from popular services in their posts with only an URL, so I wrote up a new extension. To see it in action, go [here](http://deathcat.org/314/). This code is licensed under LGPL.

You can get it here.

It is installable as many other python modules...

    python setup.py install

..., but **mdx_video.py** only has to be in your **PYTHON_PATH**. With Django, for instance, you can place it in the same directory as **settings.py**.

Using my extension is like using any other extension for markdown.

    >>> import markdown
    >>> s = "http://www.youtube.com/watch?v=F8qwxzQar2g"
    >>> markdown.markdown(s, ['video'], safe_mode='escape')

Remember to set **safe_mode** to **escape** if you are passing untrusted users' input through markdown, extension or not. This extension supports arguments for setting the dimension of the video. By default, the dimensions are what the specific service gives for their example embed. If you don't like this size, then you can change it like so:

    >>> markdown.markdown(s, ['video(youtube_width=720, youtube_height=400)'], safe_mode='escape')

If you want to integrate markdown and this extension with Django, then I recommend looking at this [post](http://tylerlesmann.com/2008/jul/25/smart-way-implementing-markdown-django/).

This extension supports the following services:

- Blip.tv
- Dailymotion
- Metacafe
- Veoh
- Vimeo
- Yahoo! video
- Youtube

NOTE: Blip.tv works a little differently than the others because there is no way to construct a working object with the player URL. Instead of the URL to the Blip.tv page, you will use the URL to the flv file, like #http://blip.tv/file/get/Pycon-DjangoOnJython531.flv for example. This is located in **Files and Links** section of Blip.tv.

Adding extra services is easy. Note: This portion is relevant to the extension for python-markdown 1.7. The first part is defining what URL for the video service should look like. You do this in the **extendMarkdown** method of **VideoExtension**.

    # This regular expression looks for a youtube URL that do not start with parenthesis.
    # It does this to avoid eating regular markdown links.
    YOUTUBE_RE = r'([^(]|^)http://www\.youtube\.com/watch\?\S*v=(?P<youtubeid>[A-Za-z0-9_-]+)\S*'
    # Here we plug our expression into the bit that builds the video embed html.
    # We define this shortly.
    YOUTUBE_PATTERN = Youtube(YOUTUBE_RE)
    # The next two lines allow control of markdown through instances of this class.
    YOUTUBE_PATTERN.md = md
    YOUTUBE_PATTERN.ext = self
    # This registers everything with markdown, so the code will be executed.
    md.inlinePatterns.append(YOUTUBE_PATTERN)

Next, we get to build the HTML. We need to add a new subclass of **markdown.BasePattern** to the module.

    class Youtube(markdown.BasePattern):
        def handleMatch(self, m, doc):
            url = 'http://www.youtube.com/v/%s' % m.group('youtubeid')
            width = self.ext.getConfig('youtube_width')
            height = self.ext.getConfig('youtube_height')
            return FlashObject(doc, url, width, height)

For the most part, building the HTML is easy. I have defined a **flash_object** function that builds an object element that work in most cases. You only need to feed it your [minidom](http://docs.python.org/library/xml.dom.minidom.html) instance, **doc**, an **url**, and **width/height**, both as strings. You will notice that I am using **self.ext.getConfig** to assign my width and height. These are the extension arguments. You will want to use these too. To do so, add a new key to the **self.config** dictionary of __init__ in **VideoExtension**.

    'youtube_width': ['640', 'Width for Youtube videos'],
    'youtube_height': ['385', 'Height for Youtube videos'],

The first part is the default value and the second bit is a description of the argument. If you need to define more HTML, then I suggest taking look at the **Yahoo** class.

Posted by Tyler Lesmann on April 2, 2009 at 8:16 at http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/
