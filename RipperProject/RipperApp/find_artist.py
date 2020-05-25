from .spotify_info import spotify


def get_artist(title):
    sp = spotify()

    results = sp.search(q='track:' + title, type='track')

    # Check if found in Spotify's database
    if len(results['tracks']['items']) == 0:
        return "Invalid"

    else:
        artist_name = results['tracks']['items'][0]['album']['artists'][0]['name']

    return artist_name
