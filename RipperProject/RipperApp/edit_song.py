import os
import eyed3


# Used to edit the metadata for mp3 files

def editor(artist, title, album, genre, path_list, album_path):
    audio_file = eyed3.load(path_list[0])
    audio_file.tag.artist = artist
    audio_file.tag.title = title
    if album:
        audio_file.tag.album = album
    audio_file.tag.genre = genre

    if album_path:
        audio_file.tag.images.set(3, open(album_path, 'rb').read(), 'image/jpeg')
        os.remove(album_path)

    audio_file.tag.save()
