import argparse
import os
import sys
import yt_dlp

def download_video(url, format_type='mp4'):
    """
    Downloads a YouTube video or playlist in the specified format.
    """
    output_dir = 'downloads'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Base options
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Allow playlist downloads
        'quiet': False,
        'no_warnings': False,
    }

    if format_type == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif format_type == 'mp4':
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        })
    else:
        print(f"Unsupported format: {format_type}")
        sys.exit(1)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download: {url}")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos or playlists in mp3 or mp4 format.")
    parser.add_argument("url", help="The YouTube video or playlist URL.")
    parser.add_argument("--format", choices=['mp3', 'mp4'], default='mp4', help="The output format (default: mp4).")

    args = parser.parse_args()

    download_video(args.url, args.format)

if __name__ == "__main__":
    main()
