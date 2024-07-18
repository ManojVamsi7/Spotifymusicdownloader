from flask import Flask, request, jsonify
from flask_cors import CORS
from spotify import get_playlist_tracks
from youtube import search_youtube
from downloader import download_video_as_mp3
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

logging.basicConfig(level=logging.INFO)

@app.route('/api/download', methods=['POST'])
def download_playlist():
    try:
        data = request.get_json()
        logging.info(f"Received data: {data}")
        playlist_id = data['playlistId']
        client_id = '73d7c0449a504a058d619ff6c85870b1'
        client_secret = '596db487d40343c9a40bf6da01f44d2d'
        youtube_api_key = 'AIzaSyA7aWcMf_AjXaWE_6twcd7I5SpAHey0HzU'
        output_path = '/Downloads'

        tracks = get_playlist_tracks(playlist_id, client_id, client_secret)
        logging.info(f"Retrieved tracks: {tracks}")

        for track in tracks:
            song_name = f"{track['name']} {track['artist']}"
            youtube_url = search_youtube(song_name, youtube_api_key)
            logging.info(f"Downloading from URL: {youtube_url}")
            download_video_as_mp3(youtube_url, output_path)
        
        return jsonify({"message": "Download complete!"})
    except Exception as e:
        logging.error(f"Error during download: {e}")
        return jsonify({"message": "Error downloading playlist"}), 500

if __name__ == '__main__':
    app.run(debug=True)
