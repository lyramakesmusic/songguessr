import os
import random
import json
from flask import Flask, jsonify, render_template, send_file
from pathlib import Path

app = Flask(__name__)

# songs = [(filename, filepath), ...] loaded on startup
songs = []

def load_songs():
    """Load all audio files from songs folder on startup"""
    global songs
    songs.clear()
    
    songs_dir = Path("songs")
    if not songs_dir.exists():
        print("Songs directory not found, creating empty one")
        songs_dir.mkdir()
        return
    
    # audio_files = [.mp3, .wav, .m4a, .ogg files]
    audio_extensions = {'.mp3', '.wav', '.m4a', '.ogg', '.flac'}
    
    for file_path in songs_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in audio_extensions:
            # song_name = filename without extension for answer matching
            song_name = file_path.stem
            # filename = just the filename without songs/ prefix for audio serving
            filename = file_path.name
            songs.append((song_name, filename))
    
    print(f"Loaded {len(songs)} songs from songs folder")

@app.route('/')
def index():
    """Serve main game page"""
    return render_template('index.html')

@app.route('/getsong')
def get_song():
    """Return random song info as JSON"""
    if not songs:
        return jsonify({"error": "No songs loaded"}), 404
    
    # random_song = (song_name, filename)
    song_name, filename = random.choice(songs)
    
    return jsonify({
        "song_name": song_name,
        "file_path": filename
    })

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    """Serve audio files from songs directory"""
    file_path = Path("songs") / filename
    if file_path.exists():
        return send_file(file_path)
    return "File not found", 404

@app.route('/songlist')
def get_song_list():
    """Return list of all song names for autocomplete"""
    # song_names = [name1, name2, ...] for answer matching  
    song_names = [name for name, _ in songs]
    return jsonify(song_names)

if __name__ == '__main__':
    load_songs()
    app.run(debug=True, host='0.0.0.0', port=5000) 