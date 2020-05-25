import glob
from pathlib import Path
import os

# Used to delete mp3 songs and jpg album cover files uploaded and downloaded on server

home = str(Path.home())
user_path = os.path.join(home, 'media', 'Users')

users_path = []
p = Path(user_path)

# Get paths for users
for user in p.iterdir():
    users_path.append(user)

user_songs = []
user_covers = []

# Get paths for mp3 and jpg files
for path in users_path:
    songs = os.path.join(path, '*mp3')
    covers = os.path.join(path, '*jpg')

    songs = glob.glob(songs)
    covers = glob.glob(covers)
    user_songs.append(songs)
    user_covers.append(covers)

# Loop through song paths
for user in user_songs:
    for song in user:
        os.remove(song)

# Loop through cover paths
for user in user_covers:
    for cover in user:
        os.remove(cover)
