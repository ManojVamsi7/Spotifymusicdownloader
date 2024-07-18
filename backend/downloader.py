from pytube import YouTube
from moviepy.editor import *
import os
import logging

def download_video_as_mp3(youtube_url, output_path):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        download_path = video.download(output_path=output_path)
        
        # Convert to MP3
        base, ext = os.path.splitext(download_path)
        mp3_path = base + '.mp3'
        
        video_clip = AudioFileClip(download_path)
        video_clip.write_audiofile(mp3_path)
        video_clip.close()
        
        # Remove the video file
        os.remove(download_path)
        
        return mp3_path
    except Exception as e:
        logging.error(f"Error downloading or converting video: {e}")
        raise e
