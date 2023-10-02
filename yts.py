from youtube_dl import YoutubeDL

def download_video(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'verbose': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

download_video('https://youtu.be/EXvTIeUz2fI?si=Q4i9LAoCk_xRmTjT')
