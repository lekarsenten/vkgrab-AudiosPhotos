# -*- coding: utf-8 -*-
"""
@author: lekarsenten
@contact: lekarsenten@gmail.com
@license Apache License, Version 2.0

Copyright (C) 2017
"""

import vk_api
import urllib
import urlparse
import os.path
import collections

class PhotoGrabber(object):
    def __init__(self, vksession):
        """
        :param vkSession: authorized session object from vk_api
        """
        self.vk_session = vksession
    def getLargestPhotoUrl(self, photo):
        sizesdict = collections.Counter()
        for ssize in photo['sizes']:
            sizesdict[ssize['type']] = ssize['src']
        photosource = sizesdict['w'] or sizesdict['z'] or sizesdict['y'] or sizesdict['x'] or sizesdict['m']
        return photosource

    def downloadIfNotExists(self, url, filepath):
        if not os.path.isfile(filepath):
            photoFile = urllib.URLopener()
            photoFile.retrieve(url, filepath)

    def grab(self, userID):
        tools = vk_api.VkTools(self.vk_session)
        photos = tools.get_all_iter('photos.getAll', 200, {'owner_id': userID,
                                                           'extended' : 0,
                                                           'photo_sizes' : 1,
                                                           'no_service_albums' : 0})
        #create directories for storing
        for dir in VKGrabber.subfolders:
            folderPath = VKGrabber.photosRoot + VKGrabber.subfolders[dir]
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)

        #download photos via getAll
        for photo in photos:
            photosource = self.getLargestPhotoUrl(photo)
            fname = photosource.rsplit('/', 1)[-1]
            fpath = VKGrabber.photosRoot + VKGrabber.subfolders.get(photo['album_id'], "") + fname;
            print("Processing " + fpath)
            self.downloadIfNotExists(photosource, fpath)

        #download saved photos. Saved photos won't return via getAll (but should)
        savedPhotos = tools.get_all_iter('photos.get', 1000, {'owner_id' : userID,
                                                              'album_id' : -15,
                                                           'extended' : 0,
                                                           'photo_sizes' : 1,
                                                           'no_service_albums' : 0})
        for saved in savedPhotos:
            photosource = self.getLargestPhotoUrl(saved)
            fname = photosource.rsplit('/', 1)[-1]
            fpath = VKGrabber.photosRoot + VKGrabber.subfolders.get(saved['album_id'], "") + fname;
            print("Processing " + fpath)
            self.downloadIfNotExists(photosource, fpath)
        
        #download Fave photos
        favephotos = tools.get_all_iter('fave.getPhotos', 200, {'extended' : 0,
                                                                'photo_sizes' : 1})
        faveFolderPath = VKGrabber.photosRoot + VKGrabber.favePhotosFolder
        if not os.path.exists(faveFolderPath):
            os.makedirs(faveFolderPath)
    
        for fave in favephotos:
            photosource = self.getLargestPhotoUrl(fave)
            fname = photosource.rsplit('/', 1)[-1]
            fpath = faveFolderPath + fname;
            print("Processing " + fpath)
            self.downloadIfNotExists(photosource, fpath)
