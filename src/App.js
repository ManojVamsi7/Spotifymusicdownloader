import React, { useState } from 'react';
import { downloadPlaylist } from './api';
import './App.css'; // Import your CSS file

function App() {
    const [playlistLink, setPlaylistLink] = useState('');
    const [status, setStatus] = useState('');
    const [loading, setLoading] = useState(false);

    const extractPlaylistId = (url) => {
        const match = url.match(/playlist\/([a-zA-Z0-9]+)/);
        return match ? match[1] : null;
    };

    const handleDownload = async () => {
        const playlistId = extractPlaylistId(playlistLink);
        if (!playlistId) {
            setStatus('Invalid playlist link');
            return;
        }

        setLoading(true);
        setStatus('Downloading...');
        try {
            const response = await downloadPlaylist(playlistId);
            setStatus(response.message);
        } catch (error) {
            console.error(error);
            setStatus('Error downloading playlist: ' + error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <h1>Spotify Playlist to MP3</h1>
            <input
                type="text"
                value={playlistLink}
                onChange={(e) => setPlaylistLink(e.target.value)}
                placeholder="Enter Spotify Playlist Link"
            />
            <button className="download-button" onClick={handleDownload} disabled={loading}>
                {loading ? 'Downloading...' : 'Download'}
            </button>
            {loading && <div className="progress-bar" />}
            <p>{status}</p>
        </div>
    );
}

export default App;
