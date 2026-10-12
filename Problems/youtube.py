'''import yt_dlp

url = "https://www.youtube.com/watch?v=yE6tIle64tU&t=4297s"
yt_dlp.YoutubeDL().download([url])'''

import yt_dlp

# Clean URL without tracking or timestamp parameters
url = "https://www.youtube.com/watch?v=yE6tIle64tU"

# Configuration options for stable extraction
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])