export const downloadPlaylist = async (playlistId) => {
    const response = await fetch('http://localhost:5000/api/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ playlistId })
    });
    if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Network response was not ok: ${errorText}`);
    }
    return response.json();
};
