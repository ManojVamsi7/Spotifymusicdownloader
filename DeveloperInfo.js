import React from 'react';

function DeveloperInfo({ isVisible, onClose }) {
    return (
        <div className={`developer-info ${isVisible ? 'visible' : ''}`}>
            <div className="content">
                <h2>Developer Information</h2>
                <p>Name: John Doe</p>
                <p>Email: john.doe@example.com</p>
                <p>GitHub: <a href="https://github.com/johndoe">johndoe</a></p>
                <button onClick={onClose}>Close</button>
            </div>
        </div>
    );
}

export default DeveloperInfo;
