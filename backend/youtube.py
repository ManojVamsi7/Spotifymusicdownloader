from googleapiclient.discovery import build
import logging

def search_youtube(song_name, api_key):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            q=song_name,
            part='snippet',
            maxResults=1
        )
        response = request.execute()
        
        video_id = response['items'][0]['id']['videoId']
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        logging.info(f"Found YouTube URL: {youtube_url}")
        return youtube_url
    except Exception as e:
        logging.error(f"Error searching YouTube: {e}")
        raise e
