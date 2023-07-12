
import youtube_dl
import urllib.request as ytsearch
import re
import vlc
import webbrowser as wb
from googlesearch import search
import random

query="jeeva jeeva song from manikya movie song"

search = query.replace(' ', '+')

# -------------> getting html content of the yt video to get its ID
html = ytsearch.urlopen(
    'https://www.youtube.com/results?search_query='+search)
# -------------------------> extratying Video ID From html data

video_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())
video_url = 'https://www.youtube.com/watch?v='+video_id[0]
print(video_url)



# Extract the audio URL using youtube_dl
ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(id)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)
    audio_url = info['url']
title=info['title']
# Print the video details
print("Title:", title)
# Create a vlc instance
vlc_instance = vlc.Instance()

# Create a vlc MediaPlayer object
media_player = vlc_instance.media_player_new()

# Load the audio URL into vlc MediaPlayer
media = vlc_instance.media_new(audio_url)
media_player.set_media(media)

# Play the audio
media_player.play()

while True:
    print("0. lyrics")
    print("1. Pause")
    print("2. Resume")
    print("3. Stop")
    print("4. Forward 5 seconds")
    print("5. Rewind 5 seconds")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        
        query = query
        for i in search(query+" lyrics in english"):
            list=[i]
            break
        random_link=str(random.choices(list))
        lyrics_link = str(random_link[2:-2])
        print(lyrics_link)
        wb.open(lyrics_link)
    elif choice == 1:
        media_player.pause()
    elif choice == 2:
        media_player.play()
    elif choice == 3:
        media_player.stop()
        break
    elif choice == 4:
        # Forward 10 seconds
        current_time = media_player.get_time()
        new_time = current_time + 10000  # 10000 milliseconds = 10 seconds
        media_player.set_time(new_time)
    elif choice == 5:
        # Rewind 10 seconds
        current_time = media_player.get_time()
        new_time = current_time - 10000  # 10000 milliseconds = 10 seconds
        media_player.set_time(new_time)
    elif choice == 6:
        media_player.stop()
        media_player.release()
        break
    else:
        print("Invalid choice. Please try again.")



