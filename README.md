# songguessr
song guesser on local files

### setup

Clone to a folder, install flask, `python app.py`, and go to `localhost:5000`

It selects from audio files in `/songs` subfolder

file structure:
```
songguessr/
├── app.py
├── songs/          (put your .mp3, .wav, .m4a, .ogg, .flac files here)
└── templates/
    └── index.html
```

### how to play

- Listen to audio snippet (starts at 0.2s)
- Type your guess or select from dropdown
- Wrong guess = longer snippet (0.5s → 1s → 2s → 5s)
- 5 points max per song
- Select "I don't know" to skip to next snippet length

It does not work on mobile yet 
