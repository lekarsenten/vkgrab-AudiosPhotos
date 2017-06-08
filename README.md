# vkgrab-AudiosPhotos
PY script : using vk_api : grab all audios from current user and all photos from current user including starred photos.

What this will do?
1) Grab all audios for specified owner id, save them to specified folder. Skips already existed files. Filename pattern will be artist - title.mp3. Supports unicode names.
2) Grab all photos for specified owner id, including wall photos, saved photos and avatars, save them to specified folder. Trying to get largest photo (up to 5MP). Skips already existed files.
3) Grab all starred(fave) photos for current user, save them to folder, skip existing files.

To get started:
1) Edit VKGrabber.py -> enter config data (top block)
2) Run script

P.S. you may comment out either audiograbber.grab or photograbber.grab if you don't need this functionality
