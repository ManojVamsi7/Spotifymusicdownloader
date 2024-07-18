Spotify Playlist to MP3 Downloader

This application allows you to download Spotify playlists by searching for the songs on YouTube and downloading them as MP3 files. The backend is built with Flask, and the frontend is built with React.

Features :

Fetch playlist details from Spotify.
Search for songs on YouTube.
Download songs as MP3 files.
Display download progress.
View developer info.
Prerequisites
Python 3.8 or higher
Node.js and npm
Spotify Developer Account (for API credentials)
YouTube Data API key

Project Structure

.
├── backend
│   ├── app.py
│   ├── requirements.txt
├── frontend
│   ├── public
│   │   ├── index.html
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── api.js
│   │   ├── DeveloperInfo.js
│   ├── package.json
│   ├── package-lock.json
├── README.md


Installation
1. Backend
2. Navigate to the backend directory.
 pip install -r requirements.txt

Create a .env file and add your Spotify API credentials:
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
YOUTUBE_API_KEY=your_youtube_api_key

Run the Flask server:
python app.py

Frontend
1. Navigate to the frontend directory.
2. Install dependencies
npm install
npm start

Usage
Open your web browser and navigate to http://localhost:3000.
Enter the Spotify Playlist ID and click "Fetch Playlist Details".
View the playlist tracks and click "Download Playlist" to start the download.
Monitor the download progress and view the status messages.
Click the "Developer Info" button to view developer information.
