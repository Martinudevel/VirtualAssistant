import os
import yt_dlp
video_url = "" # Your youtube link here

audio_file = 'test' 
ydl_opts = {
    'format': 'bestaudio',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': audio_file,  
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        t =  ydl.download([video_url])
    print(t)
except Exception as e:
    print(f"An error occurred: {e}")
# finally: # This removes the files after being processed
#     if os.path.exists(audio_file + ".mp3"):
#         os.remove(audio_file + ".mp3")
