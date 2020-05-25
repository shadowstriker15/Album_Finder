from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


def spotify():
    client_id = ""
    client_secret = ""
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
