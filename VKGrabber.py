# -*- coding: utf-8 -*-
"""
@author: lekarsenten
@contact: lekarsenten@gmail.com
@license Apache License, Version 2.0

This script will grab all audios from user profile and then all photos from user profile.
Copyright (C) 2017
"""

#VK login
login = "tempmail@gmail.com"
#VK password
password = "secret"
#VK user id. 
#I.E. last part of audios URL.
userID = 12345678

#audios folder path
audiosPath = "vkAudio"
#photos root path
photosRoot = "vkPhotos/"
subfolders = {-7: "wall/", #subfolder for photos from wall album
              -6: "profile/", #subfolder for photos from profile album
              -15: "saved/" #subfolder for photos from saved album
             }
#subfolder for photos from favorites (starred) album
favePhotosFolder = "fave/"

























import vk_api
import grab_audio
import grab_photo

def main():
    
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    audiograbber = grab_audio.AudioGrabber(vk_session)
    audiograbber.grab()
    photograbber = grab_photo.PhotoGrabber(vk_session)
    photograbber.grab()

if __name__ == '__main__':
    main()
