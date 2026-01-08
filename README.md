# YouTube Playlist Downloader

A simple Python CLI tool to download YouTube playlists and videos in MP3 or MP4 format.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure `ffmpeg` is installed on your system (required for MP3 conversion).

## Usage

```bash
python3 youtubedownloader.py <URL> [--format {mp3,mp4}]
```

- **URL**: The link to the YouTube video or playlist.
- **--format**: Choose between `mp3` or `mp4` (default is `mp4`).

Files will be saved in the `downloads/` folder.