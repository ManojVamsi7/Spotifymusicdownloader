Spotify Playlist to MP3 Downloader
This application allows you to download Spotify playlists by searching for the songs on YouTube and downloading them as MP3 files. The backend is built with Flask, and the frontend is built with React.

Features
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
java
Copy code
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
Backend
Navigate to the backend directory.

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file and add your Spotify API credentials and YouTube API key:

makefile
Copy code
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
YOUTUBE_API_KEY=your_youtube_api_key
Run the Flask server:

bash
Copy code
python app.py
Frontend
Navigate to the frontend directory.
Install dependencies:
bash
Copy code
npm install
Start the React development server:
bash
Copy code
npm start
Usage
Open your web browser and navigate to http://localhost:3000.
Enter the Spotify Playlist URL and click "Fetch Playlist Details".
View the playlist tracks and click "Download Playlist" to start the download.
