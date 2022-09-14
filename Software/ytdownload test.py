from pynput.keyboard import Key, Controller as KeyboardController
from pytube import YouTube
import youtube_dl
import time
url = 'https://www.youtube.com/watch?v=fq6QhM3InTE'
query=input("Type:")
try:
    if '1080p' ==query:
        YouTube(url).streams.get_by_itag(137).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")    
    elif '720p' ==query or '720'==query:
        YouTube(url).streams.get_by_itag(22).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
    elif '480p'==query:
        YouTube(url).streams.get_by_itag(397).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
    elif '360p'==query:
        YouTube(url).streams.get_by_itag(18).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
    elif '240p'==query:
        YouTube(url).streams.get_by_itag(133).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
    elif '144p'==query:        
        YouTube(url).streams.get_by_itag(17).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
    elif '4k'==query:
        YouTube(url).streams.get_by_itag(248).download(f"E:\\desktop files\\Hey Buddy project\\Hey Buddy project\\Software\\download file")
except:
    import clipboard
    print("Sorry couldnt download...")
    keyboard = KeyboardController()
    keyboard.press(Key.ctrl)
    keyboard.tap('l')
    keyboard.release(Key.ctrl)
    time.sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.tap('c')
    keyboard.release(Key.ctrl)
    link = clipboard.paste()

    video_url = str(link)
    print("\n\ncopied youtube video link :\t"+video_url)
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    print("download started....")
    print("dowload started.")
    filename = f"{video_info['title']}.mp3"
    filename = filename.replace("|", '')
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': fr'E:\desktop files\Hey Buddy project\Hey Buddy project\Software\download file/{filename}'
    }
    print("converting this video to audio")
    

