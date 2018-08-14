# -*- coding: utf-8 -*-
"""
@author: lekarsenten
@contact: lekarsenten@gmail.com
@license Apache License, Version 2.0

Copyright (C) 2017
"""

import collections
import urllib
from vk_api import audio
import string
import os.path
import unicodedata as ud
from vk_api.audio import VkAudio
from VKGrabber import audiosPath

all_unicode = ''.join(unichr(i) for i in xrange(65536))
unicode_letters = ''.join(c for c in all_unicode if ud.category(c)=='Lu' or ud.category(c)=='Ll')
valid_chars = "-_.() %s%s" % (unicode_letters, string.digits)
valid_chars = valid_chars.replace(u'\u0142', '')

def format_filename(s):
    
    filename = ''.join(x if x in valid_chars else ' ' for x in s)
   
    return filename

class AudioGrabber(object):
    def __init__(self, vkSession):
        """
        :param vkSession: authorized session object from vk_api
        """
        self.vk_session = vkSession

    def grab(self, userID):
        vkaudio = VkAudio(self.vk_session)

        artists = collections.Counter()

        offset = 0

        if not os.path.exists(audiosPath):
            os.makedirs(audiosPath)

        while True:
            audios = vkaudio.get(owner_id=userID)

            if not audios:
                break

            for audio in audios:
                audioFile = urllib.URLopener()
                fname = (audio['artist']+ "-" + audio['title'])
                fname = format_filename(fname)
                try:
                    print("Processing " + fname) #there might be some unicode symbols which
                                                 #cannot be printed, but are ok in filename
                except:
                    print("Whoops!!!")
                fname = audiosPath + fname + ".mp3"
                if not os.path.isfile(fname):
                    audioFile.retrieve(audio['url'], fname)

            offset += len(audios)

