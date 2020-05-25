import urllib.request
from pathlib import Path
import os


# Used to find and download an album cover

def find_cover(link, user):
    home = str(Path.home())
    user_folder = 'user_' + str(user.id)
    path = os.path.join(home, 'media', 'Users', user_folder, "album.jpg")

    urllib.request.urlretrieve(link, path)
    return path
