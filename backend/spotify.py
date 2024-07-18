import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging

def get_playlist_tracks(playlist_id, client_id, client_secret):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        results = sp.playlist_tracks(playlist_id)
        tracks = []
        
        for item in results['items']:
            track = item['track']
            tracks.append({
                'name': track['name'],
                'artist': track['artists'][0]['name']
            })
        
        logging.info(f"Tracks: {tracks}")
        return tracks
    except Exception as e:
        logging.error(f"Error fetching playlist tracks: {e}")
        raise e
