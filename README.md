## Prerequisites

- **Python 3.11**
- **ffmpeg** (required for MP3 conversion)

## Installation

1. Create and activate a virtual environment using Python 3.11:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `ffmpeg` is installed on your system (required for MP3 conversion).

## Usage

Once the virtual environment is activated:
```bash
python youtubedownloader.py <URL> [--format {mp3,mp4}]
```

- **URL**: The link to the YouTube video or playlist.
- **--format**: Choose between `mp3` or `mp4` (default is `mp4`).

Files will be saved in the `downloads/` folder.