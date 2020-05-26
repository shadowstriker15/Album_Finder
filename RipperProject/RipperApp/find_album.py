from .spotify_info import spotify


def get_album(artist_name, title):
    sp = spotify()

    results = sp.search(q='artist:' + artist_name + ' track:' + title, type='track')

    # Check if found in Spotify's database
    if len(results['tracks']['items']) == 0:
        # Try title without apostrophes
        results = sp.search(q='artist:' + artist_name + ' track:' + title.replace("'", ""), type='track')
        if len(results['tracks']['items']) == 0:
            return "Invalid", "Invalid"

    cover = results['tracks']['items'][0]['album']['images'][0]['url']
    album_name = results['tracks']['items'][0]['album']['name']

    return album_name, cover
