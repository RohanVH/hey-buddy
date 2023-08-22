from plyer import notification as msg
import vlc
import youtube_dl
import urllib.request as ytsearch
import re
import vlc
import webbrowser as wb
from googlesearch import search
import random
from tqdm import tqdm
import os
from prettytable import PrettyTable
from gtts import gTTS
from audioplayer import AudioPlayer
import pyttsx3
import speech_recognition as sr
import warnings
import datetime
import wikipedia
import webbrowser as wb
import os
import random
from datetime import date
from pytube import YouTube
import clipboard
import time
import speedtest
# wheel file error
from playsound import playsound
from tkinter import *
from tkinter.ttk import *
from time import strftime
import subprocess
import winshell
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController
import pyautogui    
import numpy as np
import pyaudio
import os
import youtube_dl
import sys
import ctypes
from PyPDF2 import PdfFileReader
import englishNews as english
import kannadaNews as k
from bs4 import BeautifulSoup
import requests
warnings.filterwarnings('ignore')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# # print(voices[1].id)
# # 1 female
# # 0 male
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',172)
# engine = pyttsx3.init()
keyboard = KeyboardController()
mouse = Controller()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<3:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        speak("hey your still awake.")
        speak("its midnight")
        speak("dont spoil you health for wealth. Remember, if you are healthy, you can earn money at any time. please go to sleep buddy")
        speak("now finish up ur work soon and go to bed") 
    elif hour >= 3 and hour < 12:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        with open(r"./Software/wishes/good morning wishes.txt", "r", encoding="utf8") as file:
            allText = file.read()
            words = list(map(str, allText.splitlines()))
            morning=random.choice(words)
            print("\n\t\t\t"+"\033[95m Quote for the day:\033[00m"+f'\t{morning}'+"\n")
            speak(morning)
            if 'good morning' in morning or 'Good Morning' in morning:
                speak("have a good day buddy")
            else:
                speak("Good Morning!")
                speak("have a good day")
            
    elif hour >=20 and hour<=23:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        with open(r"./Software/wishes/night.txt", "r", encoding="utf8") as file:
            allText = file.read()
            words = list(map(str, allText.splitlines()))
            night=random.choice(words)
            print("\n\t\t\t" +"\033[95m Quote for the day:\033[00m"+f'\t{night}'+"\n")
            speak(night)
            speak("good night")

    elif hour >= 12 and hour < 18:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        with open(r"./Software/wishes/afternoon.txt", "r", encoding="utf8") as file:
            allText = file.read()
            words = list(map(str, allText.splitlines()))
            afternoon=random.choice(words)
            print("\n\t\t\t" +"\033[95m Quote for the day:\033[00m"+f'\t{afternoon}'+"\n")
            speak(afternoon)
            speak("Good Afternoon!")

    else:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        with open(r"./Software/wishes/evening.txt", "r", encoding="utf8") as file:
            allText = file.read()
            words = list(map(str, allText.splitlines()))
            evening = random.choice(words)
            print(f"\n\t\t\t"+"\033[95m Quote for the day:\033[00m"+f'\t{evening}'+"\n")
            speak(evening)
            speak("Good Evening!")

    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\033[95m\t\t\t\t[---->>\tListening...\t<<----]\t\t\t\t\n\033[00m")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(f"\033[95m\t\t\t\t[---->\tRecognizing...\t<----]\t\t\t\t\n\033[00m")
        query = r.recognize_google(audio, language='en-in')
        print(f"\t\t\t\tUser said: {query}\n")

    except Exception as e:
        print(e)
        print("\t\t\t\twaiting for your command say something...")
        return "None"
    except sr.UnknownValueError:
        print("Hey buddy could not understand the audio")
    except sr.RequestError as ex:
        print("hey buddy get an request Error from Google Speech Recognition" + ex)
    except sr.RequestError as e:
        print("Request from Google Speech Recognition failed; {0}".format(e))
    return query

def writter():
    listener = sr.Recognizer()
    with sr.Microphone() as data_taker:
        speak('writter listening')
        print(f"\033[92m\t\t\t\t---->\t Writter Listing...\t<----\t\t\t\t\n\033[00m")

        voice = listener.listen(data_taker)
        final_voice = listener.recognize_google(voice, language='en-in')
        final_voice = final_voice.lower()
        print("writter Typing.........")

        try:
            for x in final_voice:
                
                keyboard.type(x)
                if 'enter' == final_voice:
                    x = x.replace('enter', '')
                    keyboard.tap(Key.enter)
                    print('enter buttom was clicked')
                    writter()
                elif 'home' == final_voice:
                    x = x.replace('home', '')
                    keyboard.tap(Key.home)
                    print('home button was clicked')
                    writter()
                elif 'end' == final_voice:
                    x = x.replace('end', '')
                    keyboard.tap(Key.end)
                    print('end button was clicked')
                    writter()
                elif 'left' == final_voice:
                    x = x.replace('left', '')
                    keyboard.tap(Key.left)
                    print('left arrow button was clicked')
                    writter()
                elif 'right' == final_voice:
                    x = x.replace('right', '')
                    keyboard.tap(Key.right)
                    print('right arrow button was clicked')
                    writter()
                elif 'backspace' == final_voice:
                    x = x.replace('backspace', '')
                    keyboard.tap(Key.backspace)
                    print('backspace button was clicked')
                    writter()
                elif 'space' == final_voice:
                    x = x.replace('space', '')
                    keyboard.tap(Key.space)
                    print('space button was clicked')
                    writter()

                elif 'activate tab' == final_voice:
                    x = x.replace('tab', '')
                    keyboard.tap(Key.tab)
                    print('tab button was clicked')
                    writter()

                elif 'caps lock' == final_voice:
                    x = x.replace('caps lock on', '')
                    x = x.replace('caps lock off', '')
                    keyboard.tap(Key.caps_lock)
                    print('caps lock button was clicked')
                    writter()

                elif 'number lock' == final_voice:
                    x = x.replace('number lock on', '')
                    x = x.replace('number lock off', '')
                    keyboard.tap(Key.caps_lock)
                    print('caps lock button was clicked')
                    writter()

                elif 'stop typing' == final_voice:
                    x = x.replace('stop typing', '')
                    print('stoped typing')
                    speak('hold on a second please')
                    break
                # keyboard.type(x)
            writter()
        except Exception as e:
            print(e)
            print("writter is waiting say something...")
            return "None"
        return final_voice
def is_empty(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) > 0
recognizer = sr.Recognizer()
def create_note(query):
    global recognizer
    speak("what do you want to write onto your note?")
    engine.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()
                speak("Choose a filename!")
                print("Choose a filename!")
                engine.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                speak(f"I successfully created the note {filename}")
                print(f"I successfully created the note {filename}")
                break
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you please try again!")
            print("I did not understand you please try again!")
def open_note(query):
    global recognizer
    speak("lemme know the file name which you wanna open")
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                print("tell me the file name to be opened")
                engine.runAndWait()
                try:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    filename = recognizer.recognize_google(audio)
                    filename = filename.lower()
                    # filename = filename.lower()
                    inter_file = is_empty(f"{filename}.txt")
                    if inter_file == False:
                        print('there is no such file in your notes')
                        speak('there is no such file in your notes')
                        break
                    else:
                        with open(f"{filename}.txt", 'r') as f:
                            content = f.read()
                            print("please wait...")
                            speak(f"opening {filename}file")
                            print(f"opening {filename}file")
                            print(content)
                            speak(content)
                            break
                except FileNotFoundError:
                    print("File Not Found")
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            print("\t\t\t\tI did not understand you please try again!")
            speak("waiting for your response...")
            engine.runAndWait()
def delete_exisisting_note(query):
    global recognizer
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                speak("lemme know the file name which you wanna delete")
                print("tell the file name")
                engine.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                os.remove(f"{filename}.txt")
                print(f"{filename} file note has been removed")
                speak(f"{filename} file note has been removed")
                break
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you please try again!")
            print("I did not understand you please try again!")
            engine.runAndWait()
def add_internal_todo(query):
    global recognizer
    print("what todo do you want to add?")
    speak("what todo do you want to add?")
    # engine.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio)
                item = item.lower()
                add_internal_todo = [f"\n{item}"]
            with open("internal TODO list.txt", 'a') as f:
                f.writelines(f"\n{item}\n")
                done = True
                speak(f"I added {item} to the your internal to do list")
                print(f"I added {item} to the your internal to do list")
                # engine.runAndWait()
                recognizer = sr.Recognizer()
            if "that's it" in item or "i'm do with my list" in item:
                break
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you please try again!")
            engine.runAndWait()
def show_internal_todo(query):
    inter_file = is_empty("internal TODO list.txt")
    if inter_file == False:
        print('there is no items in the list (Internal ToDO)')
        speak('the internal to do list is empty')
    else:
        print("The items on your internal to do list are the following:")
        speak("The items on your internal to do list are the following")
        with open("internal TODO list.txt", 'r') as f:
            content = f.read()
            print(f'\t\t\t\t------------------------List TODO---------------------------')
            print(f'\t\t\t\t{content}')
            print(f'\t\t\t\t------------------------------------------------------------')
            speak(content)
def add_external_todo(query):
    global recognizer
    print("what todo do you want to add?")
    speak("what todo do you want to add?")
    # engine.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio)
                item = item.lower()
                add_external_todo = [f"\n{item}"]
            with open("external TODO list.txt", 'a') as f:
                f.writelines(f"\n{item}\n")
                done = True
                speak(f"\t\t\tI added {item} to the your external to do list")
                print(f"\t\t\tI added {item} to the your external to do list")
                # engine.runAndWait()
            recognizer = sr.Recognizer()
            if "that's it" in item or "i'm do with my list" in item:
                break
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you please try again!")
            engine.runAndWait()
def show_external_todo(query):
    exter_file = is_empty("external TODO list.txt")
    if exter_file == False:
        print('there is no items in the list (external ToDO)')
        speak('the external to do list is empty')
    else:
        print("The items on your external to do list are the following:")
        speak("The items on your external to do list are the following")
        with open("external TODO list.txt", 'r') as f:
            content = f.read()
            print(f'\t\t\t\t------------------------List TODO---------------------------')
            print(f'\t\t\t\t{content}')
            print(f'\t\t\t\t------------------------------------------------------------')
            speak(content)
def skip_Ads():
    print('The current pointer position is {0}'.format(mouse.position))
    mouse.position = (993, 634)
    print('Now the pointer position moved it to {0}'.format(mouse.position))
    mouse.move(5, -5)
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.click(Button.left, 2)
    mouse.scroll(0, 2)
    print("process completed successfully...")
    # speak("done")
 
def subscribe_buttonClick():
    subscribe = pyautogui.locateCenterOnScreen("./Software/subscribechannel.png")
    print(subscribe)
    if subscribe is not None:
        pyautogui.click(subscribe)
        print("Subscribed the channel!")
           
def unSubscribe_buttonClick():
    unsubscribe = pyautogui.locateCenterOnScreen("./Software/unsubscribechannel.png")
    print(unsubscribe)
    if unsubscribe is not None:
        pyautogui.click(unsubscribe)
        print("Unsubscribed the channel!")
    time.sleep(1)
    bluebutton = pyautogui.locateCenterOnScreen("./Software/unsubscribebluebutton.png")
    print(bluebutton)
    if bluebutton is not None:
        pyautogui.click(bluebutton)
        print("bluebutton clicked!")
    else:
        print("i didnt find blue button")
            
def likebutton():
    if True:
        like = pyautogui.locateCenterOnScreen("./Software/likebutton.png")
        print(like)
        if like is not None:
            pyautogui.click(like)
            print("like clicked!")
        else:
            print("i didnt find like button")
def dislikebutton():
    if True:
        dislike = pyautogui.locateCenterOnScreen("./Software/dislikebutton.png")
        print(dislike)
        if dislike is not None:
            pyautogui.click(dislike)
            print("dislike clicked!")
        else:
            print("i didnt find dislike button")
def comment():
    if True:
        comment = pyautogui.locateCenterOnScreen("./Software/comment.png")
        print(comment)
        if comment is not None:
            pyautogui.click(comment)
            print("ready to comment on this video!")
        else: 
            print("i didnt find comment section")
def postcomment():
    if True:
        postcomment = pyautogui.locateCenterOnScreen("./Software/postcomment.png")
        print(postcomment)
        if postcomment is not None:
            pyautogui.click(postcomment)
            print("ready to postcomment on this video!")
        else:
            print("i didnt find postcomment section")
def cancelcomment():
    if True:
        cancelcomment = pyautogui.locateCenterOnScreen("./Software/cancelcomment.png")
        print(cancelcomment)
        if cancelcomment is not None:
            pyautogui.click(cancelcomment)
            print("ready to cancel comment on this video!")
        else:
            print("i didnt find cancel comment section")
                
def showmore():
    if True:
        showmore = pyautogui.locateCenterOnScreen("./Software/showmore.png")
        print(showmore)
        if showmore is not None:
            pyautogui.click(showmore)
            print("ready to display video description of this video!")
        else:
            print("i didnt find showmore section")
                
def showless():
    if True:
        showless = pyautogui.locateCenterOnScreen("./Software/showless.png")
        print(showless)
        if showless is not None:
            pyautogui.click(showless)
            print("ready to close video description of this video!")
        else:
            print("i didnt find showless section")
                

def ythomepage():
    if True:
        ythomepage = pyautogui.locateCenterOnScreen("./Software/ythomepage.png")
        print(ythomepage)
        if ythomepage is None:
            print("i didnt find ythomepage section")
        if ythomepage is not None:
            pyautogui.click(ythomepage)
            print("ready to open youtubehomepage!")
                
    
def ytsearch():
    if True:
        ytsearch = pyautogui.locateCenterOnScreen("./Software/ytsearch.png")
        print(ytsearch)
        if ytsearch is None:
            print("i didnt find ytsearch section")
        if ytsearch is not None:
            pyautogui.click(ytsearch)
            print("ready to search")
                
def ytsearchbutton():
    if True:
        ytsearchbutton = pyautogui.locateCenterOnScreen(
            "ytsearchbutton.png")
        print(ytsearchbutton)
        if ytsearchbutton is not None:
            pyautogui.click(ytsearchbutton)
            print("ready to search")
        else:
            print("i didnt find ytsearchbutton section")
                

def ytvoicesearch():
    if True:
        ytvoicesearch = pyautogui.locateCenterOnScreen("./Software/ytvoicesearch.png")
        print(ytvoicesearch)
        if ytvoicesearch is None:
            print("i didnt find ytvoicesearch section")
        if ytvoicesearch is not None:
            pyautogui.click(ytvoicesearch)
            print("ready to search")
                
def removefulscreenskip_Ads():
    mouse = Controller()
    print('The current pointer position is {0}'.format(mouse.position))
    mouse.position = (1845, 929)
    print('Now the pointer position moved it to {0}'.format(mouse.position))
    mouse.move(5, -5)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # mouse.click(Button.left, 2)
    # mouse.scroll(0, 2)
    print("process completed successfully...")
def cancelvoicesearch():
    if True:
        cancelvoicesearch = pyautogui.locateCenterOnScreen(
            "cancelvoicesearch.png")
        print(cancelvoicesearch)
        if cancelvoicesearch is None:
            print("i didnt find cancelvoicesearch section")
        if cancelvoicesearch is not None:
            pyautogui.click(cancelvoicesearch)
            print("ready to search")
                
def thispc():
    if True:
        thispc = pyautogui.locateCenterOnScreen("./Software/thispc.png")
        print(thispc)
        if thispc is None:
            print("i didnt find cancelvoicesearch section")
        if thispc is not None:
            pyautogui.click(thispc)
            print("ready to search")
        
def ytmenu():
    if True:
        ytmenu = pyautogui.locateCenterOnScreen("./Software/ytmenu.png")
        print(ytmenu)
        if ytmenu is None:
            print("i didnt find youtube menu")
        if ytmenu is not None:
            pyautogui.click(ytmenu)
            print("yotube menu activated")
        
def saveplaylist():
    saveplaylist = pyautogui.locateCenterOnScreen("./Software/saveplaylist.png")
    print(saveplaylist)
    if saveplaylist is not None:
        pyautogui.click(saveplaylist)
        print("yotube menu activated")
    else:
        print("i didnt find youtube menu")
def openqrc():
    mouse = Controller()
    print('The current pointer position is {0}'.format(mouse.position))
    mouse.position = (1512, 503)
    print('Now the pointer position moved it to {0}'.format(mouse.position))
    mouse.move(5, -5)

    mouse.press(Button.right)
    mouse.release(Button.right)
    mouse.click(Button.right, 2)
    time.sleep(1)
    keyboard = KeyboardController()
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)
    keyboard.tap(Key.down)

    keyboard.tap(Key.enter)
    print("opened QR code of this page!")
    time.sleep(10)
    keyboard.tap(Key.esc)
    print("QR code closed")

        
def savetoWatchlater():
    savetoWatchlater = pyautogui.locateCenterOnScreen("./Software/savetoWatchlater.png")
    print(savetoWatchlater)
    if savetoWatchlater is not None:
        pyautogui.click(savetoWatchlater)
        print("yotube menu activated")
    else:
        print("i didnt find youtube menu")
def savetoProject():
    savetoProject = pyautogui.locateCenterOnScreen("./Software/savetoProject.png")
    print(savetoProject)
    if savetoProject is None:
        print("i didnt find youtube menu")
    if savetoProject is not None:
        pyautogui.click(savetoProject)
        print("yotube menu")
def savetoSongs():
    savetoSongs = pyautogui.locateCenterOnScreen("./Software/savetoSongs.png")
    print(savetoSongs)
    if savetoSongs is not None:
        pyautogui.click(savetoSongs)
        print("yotube menu activate")
    else:
        print("i didnt find youtube menu")
def savetoMovies():
    savetoMovies = pyautogui.locateCenterOnScreen("./Software/savetoMovies.png")
    print(savetoMovies)
    if savetoMovies is not None:
        pyautogui.click(savetoMovies)
        print("yotube menu activate")
    else:
        print("i didnt find youtube menu")
def ytnotification():
    if True:
        ytnotification = pyautogui.locateCenterOnScreen("./Software/ytnotification.png")
        if ytnotification is not None:
            pyautogui.click(ytnotification)
            print("yotube notification activated")
        else:
            print("i didnt find youtube notification")
                
def youtube_video2mp3_converter():
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
    speak("dowload started.")
    filename = f"{video_info['title']}.mp3"
    filename = filename.replace("|", '')
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': fr'./Software/downloads/{filename}'
    }
    speak("converting this video to audio")
    with youtube_dl.YoutubeDL(options) as ydl:
        speak("please wait its almost done")    
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    speak("download completed i have saved this in your downloads folder")
    time.sleep(3)
    speak("should i play this song which i have downloaded?")
    response=takeCommand().lower()
    if 'yes' in response:
        filename = f"{filename}"
        filename = filename.replace("|", '')
        mp3song = fr"./Software/downloads/{filename}"
        os.startfile(mp3song) 

    else:
        speak("hmmmmmm!, think your not interested")


def insta_story():
    a_dictionary = {}
    a_file = open(
        r"./Software/Details/instagram friends Id.txt", "r", encoding="utf8")
    myTable = PrettyTable(["\033[93mName/033[00m","\033[93mInstagram Id\033[00m"])
    for line in a_file:
        key, value = line.split()
        if "_" in key:
            key = key.replace("_", " ")
        a_dictionary[key] = value
        myTable.add_row([f'\033[96m{key}\033[00m', f'\033[96m{value}\033[00m'])
      

    try:
        speak("tell me the name of the person")
        query=takeCommand().lower()
        instaId = a_dictionary[f"{query}"]
        print(f"\033[92m\t\t\t\tInsta ID Found!\t\t\t\t\n\033[00m")
        print(f"\033[92m\n\t\t\t\t{query}'s insta id is {instaId}.\n\033[00m")
        print(f"\033[93m\n\t\t\t\tFetching{query}'s Instagram story...\033[00m\n")
        wb.open(f'https://www.instagram.com/stories/{instaId}/')
        print("video gonna play in 10 seconds")
        time.sleep(10)  # 10 sec
        vstory = pyautogui.locateCenterOnScreen("./Software/view story.png")
        print(vstory)
        if vstory is not None:
            pyautogui.click(vstory)
            print("view story button clicked!")
        print(f"\033[93m\t\t\t\tready to play the story of {query}\033[00m")
        
    except KeyError as e:
        print(f"\033[91m\t\t\t\t--->Id not Found<---\t\t\t\t\n\033[00m")
        print(f"\033[91m\t\t\t\t{query.upper()} is not in my database/t\t\t\t\n\033[00m")
        speak("do you want me to display the available insta id list")
        query=takeCommand.lower()
        if 'yes' == query or 'ok'==query:
            header = "AVAILABLE IDS"
            print(f"\033[92m\n\n\t\t{header}\033[00m")
            print(myTable)


def onlineplayer(query):
    import youtube_dl
    import urllib.request as ytsearch
    import re
    import vlc
    import webbrowser as wb
    from googlesearch import search
    import random
    print(f"searching {query} in youtube")
    speak(f"searching {query} in youtube")
    search = query.replace(' ', '+')

    # -------------> getting html content of the yt video to get its ID
    html = ytsearch.urlopen('https://www.youtube.com/results?search_query='+search)
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
        control = takeCommand().lower()
        print("\n0. lyrics")
        print("1. Pause")
        print("2. Resume")
        print("3. Stop")
        print("4. Forward")
        print("5. Rewind")
        print("6. Download Audio")
        print("7. Exit\n")

        if control == 'open lyrics' or control == 'show lyrics':
            
            query = query
            for i in search(query+" lyrics in english"):
                list=[i]
                break
            random_link=str(random.choices(list))
            lyrics_link = str(random_link[2:-2])
            print(lyrics_link)
            wb.open(lyrics_link)
        elif control == 'pause' or control == 'pause music':
            media_player.pause()
        elif control == 'play' or control == 'start' or control == 'play music':
            media_player.play()
        elif control == 'stop' or control == 'stop playing' or control == 'stop music':
            print("Turning off")
            speak("Turning off ")
            media_player.stop()
            break
        elif control == 'forward' or control == 'forward 20 seconds':
            # Forward 10 seconds
            current_time = media_player.get_time()
            new_time = current_time + 20000  # 20000 milliseconds = 20 seconds
            media_player.set_time(new_time)
        elif control == 'forward a bit' or control == 'forward 10 seconds':
            # Forward 10 seconds
            current_time = media_player.get_time()
            new_time = current_time + 10000  # 10000 milliseconds = 10 seconds
            media_player.set_time(new_time)

        elif control == 'rewind' or control == 'rewind 20 seconds':
            # Rewind 10 seconds
            current_time = media_player.get_time()
            new_time = current_time - 20000  # 20000 milliseconds = 10 seconds
            media_player.set_time(new_time)
        elif control == 'rewind a bit' or control == 'rewind 10 seconds':
            # Rewind 10 seconds
            current_time = media_player.get_time()
            new_time = current_time - 10000  # 20000 milliseconds = 10 seconds
            media_player.set_time(new_time)
        elif control == 'download this song' or control == 'download' :
            # Output directory to save the audio
            output_directory = "./Software/downloads"

            # Create a youtube_dl options object
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s')
            }
            try:
                # Create a youtube_dl instance
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    # Download the audio
                    ydl.download([video_url])
                    
                    print(f"{title} Downloaded")
            except Exception as e:
                print(e)
        elif 'close window' in query:
                    speak("wait a sec buddy closing window")
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.f4)
                    keyboard.release(Key.alt)
                    print("windows closed alt+f4 activated")
        elif control == 'exit' or control == 'close' or control == 'close the music player':
            media_player.stop()
            media_player.release()
            break
        else:
            print("Invalid choice. Please try again.")



    

def call(person):
    call_book = {'ajji':'7676062533','amma':'7483132135','akka':'7411678135','appa':'9480477169','anita Mam':'9901006412','arpitha':'9972691769','janaki Mam':'9480443972','khushi':'8088408445','komal':'6360696740','naveen':'8050039951','nayana akka':'6364414046','nishu':'8095820463','pranitha':'8296132796','pushpa aunty':'9008252604','rishi':'8861742604','sachin':'7795442095','sai bro bhalki':'6362587380','sangeetha Mam':'9035298900','santhu':'8088152109','sarika':'9108975122','shashi biradar':'9110239301','shashidhar':'8147484364','shilpa mam':'7022007065','sneha':'7026685212'}  # ------------- List of phone number
    if person in call_book:   #------------------------------ Searching the call books
        ph_no=call_book[person]     #------------------------ Phone no. of the perso
        command1='adb shell am start -a android.intent.action.CALL -d tel:+91'+ph_no  #----cmd. to make call
        print('calling.. '+person) 
        os.system(command1)  
        print("Dailing...")
        print("Connected...")
    else:
        print('no saved contact')
def dail_random(rnumber):
    command0 = 'adb shell am start -a android.intent.action.CALL -d tel:+91'+rnumber
    os.system(command0)
def on_Off_LoudSpeaker():
    command2='adb shell input tap 289 1624'  #--------------- cmd. to tap the speaker button
    os.system(command2)                                  
    print("button activated")
   

def call_End():
    command3='adb shell input tap 539 1929'  #--------------- cmd. to tap the call end button
    os.system(command3)                                  
    print("Call Ended")

def call_dailing_Keypad():
    os.system('adb shell input tap 792 1613')    
    print("Dailing Keypad activated.")
        
def OnOff_mutecall():
    os.system('adb shell input tap 536 1612')                                  
    print("Mute/unmute button activated")


def add_call():
    
    command6 = 'adb shell input tap 276 1306'        # ------------------ cmd. to tap the add call button
    os.system(command6)

    call_book = {'ajji': '7676062533', 'amma': '7483132135', 'akka': '7411678135', 'appa': '9480477169', 'anita Mam': '9901006412', 'arpitha': '9972691769', 'janaki Mam': '9480443972', 'khushi': '8088408445', 'komal': '6360696740', 'naveen': '8050039951', 'nayana akka': '6364414046', 'nishu': '8095820463', 'pranitha': '8296132796',
                'pushpa aunty': '9008252604', 'rishi': '8861742604', 'sachin': '7795442095', 'sai bro bhalki': '6362587380', 'sangeetha Mam': '9035298900', 'santhu': '8088152109', 'sarika': '9108975122', 'shashi biradar': '9110239301', 'shashidhar': '8147484364', 'shilpa mam': '7022007065', 'sneha': '7026685212'}  # ------------- List of phone number
    print("Tell me the person name or the number:\t")
    query = query = takeCommand().lower()
    if query in call_book:
        command6 = f'adb shell input text {call_book[query]}'  #--------- enter number
        os.system(command6)
        command6 = 'adb shell input tap 544 2035'  #--------------------- call button
        os.system(command6)

    else:
        command6 = f'adb shell input text {query}'  #--------------------- enter number
        os.system(command6)
        command6 = 'adb shell input tap 544 2035'  #---------------------- call button
        os.system(command6)
    
def connectBluetooth():
    command7='adb shell input tap 801 1291'  #---------------------------- cmd. to tap the bluetooth button
    os.system(command7)                                  
    print("bluetooth button activated...")
   

def callhold_onOff():
    command8='adb shell input tap 937 189'  #----------------------------- cmd. to tap the add call button
    os.system(command8)                                  
    print("Adding call")
    time.sleep(2)
    command8='adb shell input tap 795 346'  #----------------------------- cmd. to tap the call hold button
    os.system(command8)
    print("hold button activated...")
    

def resume_call():
    command9='adb shell input tap 562 767'  #----------------------------- cmd. to tap the add call resume button
    os.system(command9)                                  
    print("Resuming call")

# ------------------------------Main---------------------------------------
if __name__ == "__main__":

    msg.notify(title="Hey Buddy!", message="Application Started...",
            app_icon=r'./Software/HB-icon.ico', timeout=3)
    playsound(r"./Software/On.mp3")
    msg.notify(title="Hey Buddy!", message="Hey Buddy Activated...",
            app_icon=r'./Software/HB-icon.ico', timeout=5)
    print("Processing....")
    # speak("Processing....")
    print("Connecting to server....")
    # speak("Connecting to server....")
    print("Turning on...")
    # speak("Turning on...")
    print('\033[92m>>>>>>>>>>>>>>>>>>>>\033[00m'+'[ '+'\033[91mH\033[00m'+'\033[93mE/033[00m'+"Y "+'\033[91mB\033[00m'+'\033[93mUDD\033[00m'+"Y"+'\033[91m! \033[00m'+'\033[93mACTIVATED\033[00m'+' ]'+'\033[92m<<<<<<<<<<<<<<<<<<<<\033[00m')
    password = 'rohan'
    print("Knock! Knock! Who's there?")
    speak("Knock Knock")
    time.sleep(0.25)
    speak("Who's there?")
    query = takeCommand().lower()
    if password == query: #basic security --has to be upgraded
        ply = vlc.MediaPlayer( r"./Software/accepted.mp3")
        good_states = ["State.Playing", "State.NothingSpecial", "StateOpening"]
        while str(ply.get_state()) in good_states:
            ply.play()
        ply.stop()
        speak("Access Granted!")
        msg.notify(title='Hey Buddy!', message='Access Granted.',
                app_icon=r'./Software/HB-icon.ico', timeout=3)      
        print("\033[92mAccess Granted!\033[00m\n\n\n\n")
        print("Granting permissions.......\n")
        time.sleep(1)
        print("Logging in......\n")
        print("User Id= Rohan")
        print("Loading...")
        speak("Rohan")
        speak('Welcome Buddy')
        wishMe()
        time.sleep(2)
        speak("Hey there,feel free to reach out me as Hey Buddy")

        def wakeupBuddy():
            import pywhatkit as kit
            print("\033[91m--------------->>\033[00m[ \t\tHey Buddy is ready to take you commands\t\t ]\033[91m<<---------------\033[00m")
            msg.notify(title="Hey Buddy!", message="Listening...",
                    app_icon=r'./Software/HB-icon.ico')
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            # # print(voices[1].id)
            # # 1 female
            # # 0 male
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 171)
            # engine = pyttsx3.init()
            keyboard = KeyboardController()
            mouse = Controller()


            def speak(audio):
                engine.say(audio)
                engine.runAndWait()
            while True:
                query = takeCommand().lower()
                keyboard = KeyboardController()
                mouse = Controller()
                # Logic for executing tasks based on query
                if 'wikipedia search' in query:
                    query = query.replace('wikipedia serach', '')
                    speak('Searching  in Wikipedia...')
                    query = query.replace("in wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'tell me about yourself' in query or 'introduce yourself' in query:
                    
                    speak('''Hey Mate,
                            Greetings to you.
                            I trust your day is working out positively.
                            I am your Buddy, version 1.0
                            I am most grateful for my buddy Mr.Rohan, the master mind behind my creation.
                            If it wasn’t by him, I wouldn’t be here for sure.
                            I started out as an idea which struck his bright mind.
                            He then brought all his inventive ideas together and helped bring me to life, creating his very own personal voice assistant, just to make his life more operative.
                            You too can rely on me with no doubts to get your things done from scratch to an advanced level right away, just the way Rohan does.
                            If you need anything, just reach out to me as Hey Buddy!, I will be there to assist you anytime.
                            Your demand is always my command.
                            I would love to, and assure you, to also make your life be an uncomplicated one.
                            I am looking forward to assist you at the best.
                            Have a pleasant day ahead.''')
                elif "what's your name" in query or "what should i call you" in query:
                    speak("Hey there, my name is Buddy, If you need anything, just reach out to me as Hey Buddy!, I will be there to assist you anytime.")
                elif "what's your version" in query:
                    speak("Its Version 1.0")
                elif 'open youtube' in query:
                    youtube = 'https://www.youtube.com'
                    wb.open(youtube)
                    print("opening youtube")
                    speak("okay buddy opening youtube...")
                elif 'open google' in query:
                    google = 'https://www.google.com'
                    wb.open(google)
                    print("opening google")
                    speak("okay buddy opening google...")
                elif 'open stack overflow' in query:
                    stackoverflow = 'https://stackoverflow.com/'
                    wb.open(stackoverflow)
                    print("opening stack")
                    speak("okay buddy opening stack...")
                elif 'open chrome' in query:
                    os.system("start chrome.exe")
                elif 'open brave' in query:
                    os.system("start brave.exe")
                elif 'open task manager' in query:
                    keyboard.press(Key.ctrl_l)
                    keyboard.press(Key.shift)
                    keyboard.tap(Key.esc)
                    keyboard.release(Key.shift)
                    keyboard.release(Key.ctrl_l)
                elif 'close tab' in query:
                    keyboard.press(Key.ctrl_l)
                    keyboard.press(Key.f4)
                    keyboard.release(Key.f4)
                    keyboard.release(Key.ctrl_l)
                    print('closing window')
                elif 'open instagram' == query:
                    speak("okay buddy")
                    instagram = 'https://www.instagram.com'
                    wb.open(instagram)
                    print("Instagram")
                    speak("hmm hold on a second opening Instagram")
                elif 'open my college website' in query:
                    speak("okay Buddy")
                    college_website = 'http://www.kascc.in.net/'
                    wb.open(college_website)
                    print("clg website")
                    speak("hmm hold on a second opening your college website")
                elif 'open whatsapp web' == query:
                    speak('okay buddy')
                    whats_app = 'https://web.whatsapp.com/'
                    wb.open(whats_app)
                    print("whats app web")
                    speak("hold on a minute buddy opening your whats app messanger..")
                # elif 'open whats app' ==query:
                #     os.startfile(r"C:\Users\Rohan\AppData\Local\WhatsApp\WhatsApp.exe")
                elif 'play' in query: #online youtube player
                    query = query.replace('play', '')
                    if 'video' in query:
                        query = query.replace('on youtube', '')
                        query = query.replace('video', '')
                        print("waiting to play your desired song on youtube...")
                        query = str(query)
                        song = query
                        speak(f"ok playing....{song}")
                        print(f"playing....{song}")
                        kit.playonyt(song)
                    elif 'audio' in query:
                        query = query.replace(' audio', '')
                        onlineplayer(query)
                elif 'open full screen' in query:
                    keyboard.press('f')
                    keyboard.release('f')
                    print('opening full screen')
                elif 'close full screen' in query:
                    keyboard.press('f')
                    keyboard.release('f')
                    print('closing full screen mode')
                elif 'media' in query or 'play on' in query:
                    query = query.replace('media on', '')
                    query = query.replace('media off', '')
                    keyboard.tap(Key.media_play_pause)
                    print('media activated once...')
                elif 'media next' in query or 'next song' in query:
                    keyboard.tap(Key.meida_next)
                    print('media next activated once')
                elif 'mute' in query:
                    query = query.replace('mute on', '')
                    query = query.replace('mute off', '')
                    keyboard.tap(Key.media_volume_mute)
                    print('mute button activated')
                elif 'type' in query:
                    query = query.replace('type', '')
                    print("opening type writter")
                    writter()
                elif 'go back to the previous' in query:
                    query = query.replace('go back to the previous song', '')
                    query = query.replace('go back to the previous video', '')
                    query = query.replace('go back to the previous music', '')
                    keyboard.press(Key.media_previous)
                    keyboard.release(Key.media_previous)
                elif 'full window' == query:
                    keyboard.press(Key.cmd)
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    keyboard.release(Key.cmd)
                    print('maximized window')
                elif 'half window' == query:
                    keyboard.press(Key.cmd)
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    keyboard.release(Key.cmd)
                    print("minimize window")
                elif 'left window' == query:
                    keyboard.press(Key.cmd)
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    keyboard.release(Key.cmd)
                    print("window moved towards the left screen")
                elif 'right window' == query:
                    keyboard.press(Key.cmd)
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    keyboard.release(Key.cmd)
                    print("window moved towards the right screen")
                elif 'enter' in query or 'click' in query:
                    keyboard.tap(Key.enter)
                    print('enter buttom was clicked')
                elif 'refresh' in query:
                    mouse.position = (749, 278)
                    print('Now we have moved it to {0}'.format(mouse.position))
                    mouse.move(5, -5)
                    keyboard.tap(Key.f5)
                    print("reload done")
                elif 'close window' in query:
                    speak("wait a sec buddy closing window")
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.f4)
                    keyboard.release(Key.alt)
                    print("windows closed alt+f4 activated")
                    speak("i have closed buddy")
                elif "what's the time" in query:
                    hour = datetime.datetime.now().strftime("%I")
                    min = datetime.datetime.now().strftime("%M")
                    for h in hour:
                        string = strftime(f' {hour} : {min} %p ')
                        if hour=='01' or hour=='02' or hour=='03' or hour=='04' or hour=='05' or hour=='06' or hour=='07' or hour=='08' or hour=='09':
                            hour = hour.replace('01', '1')
                            hour = hour.replace('02', '2')
                            hour = hour.replace('03', '3')
                            hour = hour.replace('04', '4')
                            hour = hour.replace('05', '5')
                            hour = hour.replace('06', '6')
                            hour = hour.replace('07', '7')
                            hour = hour.replace('08', '8')
                            hour = hour.replace('09', '9')
                        if min=='00':
                            min =min.replace('00','')
                            string=string.replace(':','')
                        string = strftime(f' {hour}:{min} %p ')
                        print(f"Its \t{string}")
                        string=string.replace(":",' ')
                        speak(f"{string}")
                        
                        break

                elif "the day" in query:
                    date = datetime.datetime.now()
                    day = date.today().strftime('%d')
                    if day == '01' or day == '02' or day == '03' or day == '04' or day == '05' or day == '06' or day == '07' or day == '08' or day == '09' or day == '10':
                        day = day.replace('01', '1st')
                        day = day.replace('02', '2nd')
                        day = day.replace('03', '3rd')
                        day = day.replace('04', '4th')
                        day = day.replace('05', '5th')
                        day = day.replace('06', '6th')
                        day = day.replace('07', '7th')
                        day = day.replace('08', '8th')
                        day = day.replace('09', '9th')
                        day = day.replace('10', '10th')
                    if day == '11' or day == '12' or day == '13' or day == '14' or day == '15' or day == '16' or day == '17' or day == '18' or day == '19' or day == '20':
                        day = day.replace('11', '11th')
                        day = day.replace('12', '12th')
                        day = day.replace('13', '13th')
                        day = day.replace('14', '14th')
                        day = day.replace('15', '15th')
                        day = day.replace('16', '16th')
                        day = day.replace('17', '17th')
                        day = day.replace('18', '18th')
                        day = day.replace('19', '19th')
                        day = day.replace('20', '20th')
                    if day == '21' or day == '22' or day == '23' or day == '24' or day == '25' or day == '26' or day == '27' or day == '28' or day == '29' or day == '30' or day == '31':
                        day = day.replace('21', '21st')
                        day = day.replace('22', '22nd')
                        day = day.replace('23', '23rd')
                        day = day.replace('24', '24th')
                        day = day.replace('25', '25th')
                        day = day.replace('26', '26th')
                        day = day.replace('27', '27th')
                        day = day.replace('28', '28th')
                        day = day.replace('29', '29th')
                        day = day.replace('30', '30th')
                        day = day.replace('31', '31st')
                    today = date.today().strftime(f'%A {day}. %B %Y')
                    print('its\t'+today)
                    speak('its\t'+today)
                elif 'the date' in query:
                    day = date.today().strftime('%d')
                    if day == '01' or day == '02' or day == '03' or day == '04' or day == '05' or day == '06' or day == '07' or day == '08' or day == '09' or day == '10':
                        day = day.replace('01', '1st')
                        day = day.replace('02', '2nd')
                        day = day.replace('03', '3rd')
                        day = day.replace('04', '4th')
                        day = day.replace('05', '5th')
                        day = day.replace('06', '6th')
                        day = day.replace('07', '7th')
                        day = day.replace('08', '8th')
                        day = day.replace('09', '9th')
                        day = day.replace('10', '10th')
                    if day == '11' or day == '12' or day == '13' or day == '14' or day == '15' or day == '16' or day == '17' or day == '18' or day == '19' or day == '20':
                        day = day.replace('11', '11th')
                        day = day.replace('12', '12th')
                        day = day.replace('13', '13th')
                        day = day.replace('14', '14th')
                        day = day.replace('15', '15th')
                        day = day.replace('16', '16th')
                        day = day.replace('17', '17th')
                        day = day.replace('18', '18th')
                        day = day.replace('19', '19th')
                        day = day.replace('20', '20th')
                    if day == '21' or day == '22' or day == '23' or day == '24' or day == '25' or day == '26' or day == '27' or day == '28' or day == '29' or day == '30' or day == '31':
                        day = day.replace('21', '21st')
                        day = day.replace('22', '22nd')
                        day = day.replace('23', '23rd')
                        day = day.replace('24', '24th')
                        day = day.replace('25', '25th')
                        day = day.replace('26', '26th')
                        day = day.replace('27', '27th')
                        day = day.replace('28', '28th')
                        day = day.replace('29', '29th')
                        day = day.replace('30', '30th')
                        day = day.replace('31', '31st')
                    print(f"Its\t{day}")
                    speak(f"Its\t{day}")
                elif 'the week' in query:
                    date = datetime.datetime.now()
                    week = date.today().strftime('%A')
                    print(f'its {week} today')
                    speak('its'+week+'today')
                
                elif 'previous page' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.left)
                    keyboard.release(Key.alt)
                    print('going back to previous page \n')
                elif 'next page' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.left)
                    keyboard.release(Key.alt)
                    print('heading toward the next page \n')
                elif 'page up' in query:
                    keyboard.tap(Key.page_up)
                    print("page up button activated \n")
                elif 'page down' in query:
                    keyboard.tap(Key.page_down)
                    print('page down button activated \n')
                elif 'take a screenshot' in query:
                    speak('hold on a sec im gonna take screenshot')
                    keyboard.press(Key.cmd)
                    keyboard.tap(Key.print_screen)
                    keyboard.release(Key.cmd)
                    print('screenshot activated')
                    print('its done buddy please check it out \n')
                elif 'move down' in query:
                    keyboard.tap(Key.down)
                    print('down arrow activated \n')
                elif 'move up' in query:
                    keyboard.tap(Key.up)
                    print('up arrow activated \n')
                elif 'move left' in query or 'rewind' in query:
                    keyboard.tap(Key.left)
                    print('left arrow activated')
                elif 'move right' in query or 'forward' in query:
                    keyboard.tap(Key.right)
                    print('move arrow activated')
                elif 'delete' in query:
                    keyboard.tap(Key.delete)
                    print('delete button activated \n')
                elif 'escape' in query or 'exit' in query:
                    keyboard.tap(Key.esc)
                    print('esc button activated \n')
                elif 'open system notification' in query:
                    keyboard.press(Key.cmd)
                    keyboard.tap('a')
                    keyboard.release(Key.cmd)
                    print('system notification acticated \n')
                elif 'open windows' in query:
                    speak('okay opening windows explorer')
                    keyboard.press(Key.cmd)
                    keyboard.tap('e')
                    keyboard.release(Key.cmd)
                    print('windows explorer acticated \n')
                elif 'create new folder' in query:
                    mouse.move(5, -5)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    print('----left click done----')
                    keyboard.press(Key.ctrl)
                    keyboard.press(Key.shift)
                    keyboard.tap('n')
                    keyboard.release(Key.shift)
                    keyboard.release(Key.ctrl)
                    print("new folder created \n")
                    speak('created new folder')
                elif 'minimise apps' in query:
                    query = query.replace('minimise off', '')
                    query = query.replace('minimise on', '')
                    keyboard.press(Key.cmd)
                    keyboard.press('d')
                    keyboard.release('d')
                    keyboard.release(Key.cmd)
                    print('minimizing apps \n')
                    speak('minimizing apps')
                elif 'maximize apps' in query:
                    query = query.replace('minimise off', '')
                    query = query.replace('minimise on', '')
                    keyboard.press(Key.cmd)
                    keyboard.press('d')
                    keyboard.release('d')
                    keyboard.release(Key.cmd)
                    print('maximizing apps \n')
                    speak('maximizing apps')
                elif 'drag down all apps' in query:
                    query = query.replace('minimise off', '')
                    query = query.replace('minimise on', '')
                    keyboard.press(Key.cmd)
                    keyboard.press('d')
                    keyboard.release('d')
                    keyboard.release(Key.cmd)
                    print('minimizing all apps \n')
                    print("Note: win+m \n")
                    speak('all apps has been minimized buddy \n')
                elif 'save this' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('s')
                    keyboard.release(Key.ctrl)
                    print('saved \n')
                    speak('saved successfully \n')
                elif 'undo' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('z')
                    keyboard.release(Key.ctrl)
                    print('undo activated \n')
                elif 'redo' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('y')
                    keyboard.release(Key.ctrl)
                    print('redo activated \n')
                elif 'open downloads' in query or 'open download page' in query:
                    speak('okay wait a sec opening chrome dowloads')
                    keyboard.press(Key.ctrl)
                    keyboard.tap('j')
                    keyboard.release(Key.ctrl)
                    print('download page opened (in chrome) \n')
                    speak('download page is ready to view')
                elif 'open chrome history' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('h')
                    keyboard.release(Key.ctrl)
                    speak('okay wait a sec opening chrome history')
                    print('history page opened (in chrome) \n')
                    speak('history page is ready to view')
                elif 'open home page' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.home)
                    keyboard.release(Key.alt)
                    print('heading back to chrome home page \n')
                    speak('heading back to chrome home page')
                elif 'activate alt' in query:
                    keyboard.press(Key.alt)
                    print('alt button is pressed and its wating for the release command \n')
                    speak(
                        'okay done buddy but dont forget to release this button which is activated')
                elif 'release alt' in query:
                    keyboard.release(Key.alt)
                    print('alt button released \n')
                elif 'active tab' in query:
                    keyboard.tap(Key.tab)
                    print('tab button was clicked once \n')
                elif 'click space' in query:
                    keyboard.tap(Key.space)
                    print('space button was clicked once \n')
                elif 'minimise current tab' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.space)
                    keyboard.release(Key.alt)
                    keyboard.tap('n')
                    print('minimized the current tab \n')
                elif 'maximize current tab' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.space)
                    keyboard.release(Key.alt)
                    keyboard.tap('x')
                    print('maximized the current tab \n')
                elif 'open this pc' in query:
                    speak('wait buddy opening this pc')
                    thispc()
                    print('this pc opened')
                    speak('opened this pc')
                    
                elif 'open new tab' in query:
                    speak('opening new tab')
                    keyboard.press(Key.ctrl)
                    keyboard.press('t')
                    keyboard.release(Key.ctrl)
                    print('opened new tab\n')
                    speak('done buddy')
                elif 'open new window' in query:
                    speak('opening new window')
                    keyboard.press(Key.ctrl)
                    keyboard.press('n')
                    keyboard.release(Key.ctrl)
                    print('opened new window \n')
                    speak('done buddy')
                elif 'shutdown the system' in query:
                    try:
                        os.system("shutdown /s /t 1")
                    except:
                        speak('okay buddy turning off the system')
                        keyboard.press(Key.cmd)
                        keyboard.press('m')
                        keyboard.release('m')
                        keyboard.release(Key.cmd)
                        keyboard.press(Key.cmd)
                        keyboard.press('m')
                        keyboard.release('m')
                        keyboard.release(Key.cmd)
                        print('----minimized all apps----')
                        mouse.position = (749, 278)
                        mouse.move(5, -5)
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                        print('----left click on the center screen----')
                        keyboard.press(Key.alt)
                        keyboard.tap(Key.f4)
                        keyboard.release(Key.alt)
                        print('---window tab opened---')
                        speak('ba bye buddy seen you soon...')
                        speak('power off')
                        keyboard.tap(Key.enter)
                        print('enter key pressed')
                elif 'restart the system' in query:
                    try:
                        os.system("shutdown /r /t 5")

                    except:
                        speak('wait a minute restarting the system')
                        keyboard.press(Key.cmd)
                        keyboard.press('m')
                        keyboard.release('m')
                        keyboard.release(Key.cmd)
                        keyboard.press(Key.cmd)
                        keyboard.press('m')
                        keyboard.release('m')
                        keyboard.release(Key.cmd)
                        print('----minimized all apps----')
                        mouse.position = (749, 278)
                        mouse.move(5, -5)
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                        print('----left click on the center screen----')
                        keyboard.press(Key.alt)
                        keyboard.tap(Key.f4)
                        keyboard.release(Key.alt)
                        print('---window tab opened---')
                        keyboard.tap(Key.down)
                        print('---down arrow clicked---')
                        speak('hey buddy will be back soon...')
                        speak('hey buddy will be back soon')
                        keyboard.tap(Key.enter)
                elif 'open tab number' in query:
                    query = query.replace('open tab number', '')
                    query = query.replace(' ', '')
                    query = str(query)
                    keyboard.press(Key.ctrl)
                    keyboard.press(query)
                    keyboard.release(query)
                    keyboard.release(Key.ctrl)
                    print(f'opened tab number {query}\n')
                elif 'open next tab' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap(Key.tab)
                    keyboard.release(Key.ctrl)
                    print('opened next tab')
                elif 'open previous tab' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.press(Key.shift)
                    keyboard.tap(Key.tab)
                    keyboard.release(Key.shift)
                    keyboard.release(Key.ctrl)
                    print('opened previous tab \n')
                elif 'next window' in query:
                    keyboard.press(Key.alt)
                    keyboard.tap(Key.tab)
                    keyboard.release(Key.alt)
                    print('heading towards the next window \n')
                elif 'open closed previous tab' in query or 'reopen previous tab' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.press(Key.shift)
                    keyboard.tap('t')
                    keyboard.release(Key.ctrl)
                    keyboard.release(Key.shift)
                    print('opened closed previous tabs')
                elif 'rename this folder' in query:
                    keyboard.tap(Key.f2)
                elif 'clear all' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('a')
                    keyboard.release(Key.ctrl)
                    keyboard.tap(Key.backspace)
                    print('cleared all \n')
                elif 'Select all' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('a')
                    keyboard.release(Key.ctrl)
                    print('queryed all \n')
                    speak('queryed')
                elif 'copy' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('c')
                    keyboard.release(Key.ctrl)
                    print('copied! \n')
                    speak('copied')
                elif 'cut' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('x')
                    keyboard.release(Key.ctrl)
                    print('cut process done! \n')
                    speak('cut process done')
                elif 'paste' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('v')
                    keyboard.release(Key.ctrl)
                    print('paste process completed! \n')
                    speak('paste process completed')
                elif 'find' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('f')
                    keyboard.release(Key.ctrl)
                    print('find process activated! \n')
                elif 'print' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('p')
                    keyboard.release(Key.ctrl)
                    print('printing process activated! \n')
                elif "what's my internet speed" in query: #module issue (module changed to speedtest-cli)
                    
                    test = speedtest.Speedtest()
                    print("performing download test...")
                    download_result = test.download()
                    print("performing upload test...")
                    upload_result = test.results.ping
                    print(f'Download speed: {download_result / 1024 /1024:.2f} Mbit/s')
                    print(f'Upload speed: {upload_result / 1024 /1024:.2f} Mbit/s')
                    print(f'Ping: {download_result:.2f} ms')
                    speak(
                        f'Download speed: {download_result / 1024 /1024:.2f} Mb per second')
                    speak(
                        f'Upload speed: {upload_result / 1024 /1024:.2f} Mb per second')
                    speak(f'Ping: {download_result:.2f} ms')
                elif 'open vscode' in query:
                    vscd = "C:\\Users\\Rohan\\AppData\\Local\\Programs\\Microsoft VS Code/\Code.exe"
                    os.startfile(vscd)
                elif 'open cmd' in query or 'open command prompt' in query:
                    os.system("start cmd")
                elif 'open firefox' in query or 'open fire fox' in query:
                    firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    os.startfile(firefox)
                elif 'open new incognito' in query or 'open incognito' in query:
                    keyboard.press(Key.ctrl_l)
                    keyboard.press(Key.shift)
                    keyboard.press('n')
                    print("keys pressed..")
                    keyboard.release('n')
                    keyboard.release(Key.shift)
                    keyboard.release(Key.ctrl_l)
                    print("keys released...")
                    speak("okay Done buddy")
                elif 'open youtube homepage' in query or 'youtube homepage' in query:
                    speak("opening youtube homepage")
                    ythomepage()            
                    print("process completed successfully...")
                elif 'copy url' in query or 'copy this page url' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('l')
                    keyboard.release(Key.ctrl)
                    print('\t\t\tlink queryed')
                    keyboard.press(Key.ctrl)
                    keyboard.tap('c')
                    keyboard.release(Key.ctrl)
                    print('\t\t\tcopied!')
                    speak("yes done")
                elif 'full volume' in query:
                    pyautogui.press(['volumeup', 'volumeup', 'volumeup', 'volumeup', 'volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup'])
                    pyautogui.press(['volumeup', 'volumeup', 'volumeup', 'volumeup', 'volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup'])
                    pyautogui.press(['volumeup', 'volumeup', 'volumeup', 'volumeup', 'volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup'])
                    pyautogui.press(['volumeup', 'volumeup', 'volumeup', 'volumeup', 'volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup'])
                    pyautogui.press(['volumeup', 'volumeup', 'volumeup', 'volumeup', 'volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup','volumeup'])
                    print("Activated")
                elif 'reduce volume' in query:
                    pyautogui.press(['volumedown', 'volumedown', 'volumedown', 'volumedown', 'volumedown', 'volumedown',
                                    'volumedown', 'volumedown', 'volumedown', 'volumedown', 'volumedown', 'volumedown'])
                    print('done')
                elif 'auto play on' in query or 'auto play off' in query:
                    print('The current pointer position is {0}'.format(mouse.position))
                    mouse.position = (826, 698)
                    print('Now the pointer position moved it to {0}'.format(mouse.position))
                    mouse.move(5, -5)
                    # Press and release
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    # Double click; this is delifferent from pressing and releasing
                    # twice on macOS
                    mouse.click(Button.left, 2)
                    # Scroll two steps down
                    mouse.scroll(0, 2)
                    print("process completed successfully...")
                    speak('done buddy')
                elif 'turn on caption' in query or 'turn on subtitles' in query or 'turn off caption' in query or 'turn off subtitiles' in query:
                    speak('ya sure buddy')
                    keyboard.tap('c')
                    print("the key activated")
                    speak("its done")
                elif 'open youtube notifications' in query:
                    ytnotification()
                elif 'close youtube notifications' in query:
                    keyboard.tap(Key.esc)
                elif 'i dont want to save' in query or 'cancel save to' in query:
                    keyboard.tap(Key.esc)
                    print("canceled")
                elif 'open youtube search bar' in query:
                    ytsearch()
                    print('opened youtube search bar')
                elif 'search this buddy' in query:
                    try:
                        ytsearchbutton()
                    except:
                        keyboard.tab(Key.enter)
                elif 'open this video discription' in query:
                    showmore()
                elif 'close this video discription' in query:
                    showless()
                elif 'comment on this video' in query:
                    comment()
                    print("what you wanna comment on this video")
                    speak("what you wanna comment on this video")
                    writter()
                    speak("buddy should i post this comment")
                elif 'okay post this comment' in query or 'post this' in query:
                    postcomment()
                    print("i have posted your comment")
                    speak("i have posted yout comment")
                elif 'no dont post' in query or 'dont post this commant' in query  or 'no cancel this comment' in query:
                    cancelcomment()
                    speak("canceled you comment")
                elif 'subscribe this channel' == query:
                    speak("subscribing this youtube channel")
                    subscribe_buttonClick()
                elif 'cancel the subscription' == query:
                    speak("canceling the subscription of this channel")
                    unSubscribe_buttonClick()
                    speak("done buddy")
                elif 'save this video' in query:
                    saveplaylist()
                    speak("tell me the name of the playlist")
                    query=query.lower()
                    if 'watch later' in query:
                        savetoWatchlater()
                    elif 'project' in query:
                        savetoProject()
                    elif 'songs' in query:
                        savetoSongs()
                    elif 'movies' in query:
                        savetoMovies()
                    speak("i have saved this")
                    query=query.lower()
                    if 'okay buddy' in query or 'thank you' in query:
                        keyboard.tap(Key.esc)
                        speak('hmmm')
                elif 'watch later' in query:
                    savetoWatchlater()
                elif 'project' in query:
                    savetoProject()
                elif 'songs' in query:
                    savetoSongs()
                elif 'movies' in query:
                    savetoMovies()
                elif 'skip ads' in query or 'skip this ads' in query or 'skip this add' in query or 'skip this adds' in query:
                    skip_Ads()
                    print('ads removed')
                elif 'remove screen ads' in query:
                    removefulscreenskip_Ads()
                    print("process completed successfully...")
                elif 'open run' in query or 'open run window' in query:
                    keyboard.press(Key.ctrl)
                    keyboard.tap('r')
                    keyboard.release(Key.ctrl)
                    speak("done buddy its opened")
                elif 'project pc screen only' in query:
                    keyboard.press(Key.cmd)
                    keyboard.tap('p')
                    keyboard.release(Key.cmd)
                    keyboard.tap(Key.enter)
                    speak('projected to pc screen only')
                elif 'project duplicate screen' in query:
                    keyboard.press(Key.cmd)
                    keyboard.tap('p')
                    time.sleep(2)
                    keyboard.tap('p')
                    keyboard.release(Key.cmd)
                    keyboard.tap(Key.enter)
                    speak("projected to duplicate screen")
                elif 'project extend screen' in query:
                    keyboard.press(Key.cmd)
                    keyboard.tap('p')
                    time.sleep(2)
                    keyboard.tap('p')
                    keyboard.tap('p')
                    keyboard.release(Key.cmd)
                    keyboard.tap(Key.enter)
                    speak('screen extended')
                elif 'project second screen only' in query:
                    keyboard.press(Key.cmd)
                    keyboard.tap('p')
                    time.sleep(2)
                    keyboard.tap('p')
                    keyboard.tap('p')
                    keyboard.tap('p')
                    keyboard.release(Key.cmd)
                    keyboard.tap(Key.enter)
                    speak('projected second screen only')
                elif 'give a like to this video' == query or 'like this video' == query:
                    likebutton()
                    print("process completed successfully...")
                    speak("done")
                elif "i didn't like this video" in query or 'dislike this video' == query:
                    dislikebutton()
                    print("process completed successfully...")
                elif 'open chrome search bar' == query:
                    keyboard.press(Key.ctrl_l)
                    keyboard.tap('k')
                    keyboard.release(Key.ctrl_l)
                    speak("done buddy")
                elif 'close youtube menu' in query or 'open youtube menu' in query:
                    ytmenu()
                    print('youtube menu')
                elif 'change caption background' in query:
                    keyboard.tap('w')
                elif 'decrease font size' in query or 'decrease caption size' in query:
                    keyboard.tap('-')
                elif 'increase font size' in query or 'increase caption size' in query:
                    keyboard.tap('=')
                elif 'next youtube video' in query:
                    keyboard.press(Key.shift)
                    keyboard.tap('n')
                    keyboard.release(Key.shift)
                    speak('playing next video')
                elif 'previous youtube video' in query:
                    keyboard.press(Key.shift)
                    keyboard.tap('p')
                    keyboard.release(Key.shift)
                    speak('playing previous video')
                elif 'forward this video 5 seconds' in query or 'forward 5 seconds' in query:
                    keyboard.tap(Key.right)
                elif 'rewind this video 5 seconds' in query or 'rewind 5 seconds' in query:
                    keyboard.tap(Key.left)
                elif 'forward this video 10 second' in query or 'forward 10 seconds' in query:
                    keyboard.tap('l')
                elif 'rewind this video 10 seconds' in query or 'rewind 10 seconds' in query:
                    keyboard.tap('j')
                elif 'video play' in query:
                    keyboard.tap('k')
                elif 'increase video volume' in query:
                    keyboard.tap(Key.up)
                elif 'decrease video volume' in query:
                    keyboard.tap(Key.down)
                elif f'skip 50% of this video' in query:
                    keyboard.tap('5')
                elif 'play again' == query:
                    keyboard.tap('0')
                elif 'skip to the end of this video' in query:
                    keyboard.tap('9')
                elif 'increase youtube video speed' in query:
                    keyboard.press(Key.shift)
                    keyboard.tap('.')
                    keyboard.release(Key.shift)
                elif 'decrease youtube video speed' in query:
                    keyboard.press(Key.shift)
                    keyboard.tap(',')
                    keyboard.release(Key.shift)
                elif 'change caption brightness' in query:
                    keyboard.tap('o')
                elif 'close QR code' in query:
                    keyboard.tap(Key.esc)
                    print('esc was clicked once')
                elif 'open QR code of this page' == query:
                    print('opened QR code of this page')
                    speak("its ready. scan it, if u wanna access this page in your device")
                    openqrc()
                elif 'open youtube notification' in query:
                    pass
                elif 'open subscribed channels' == query:
                    speak("opening all subscribed channels list")
                    channels_page='https://www.youtube.com/feed/channels'
                    wb.open(channels_page)
                    print('youtube subscribed channel list')
                elif 'mini screen' in query or 'close mini screen' in query:
                    keyboard.tap('i')
                    speak("done")
                elif 'theater mode' in query or 'exit theater mode' in query or 'close theater mode' in query:
                    keyboard.tap('t')
                    speak("done")
                elif 'turn on youtube voice search' in query:
                    ytvoicesearch()
                    print('yt voice search is ON')
                elif 'turn off youtube voice search' in query:
                    cancelvoicesearch()
                    print("turning off the youtube voice search")
                    speak("turning off the youtube voice search")
                elif 'open youtube watch  playlist' in query:
                    watchlater='https://www.youtube.com/playlist?list=WL'
                    wb.open(watchlater)
                    print('opening watch later playlist')
                    speak('opening watch later playlist')
                elif 'open youtube history' == query:
                    history='https://www.youtube.com/feed/history'
                    wb.open(history)
                    print('opening youtube videos history playlist')
                    speak('opening youtube videos history playlist')
                elif 'open liked videos' == query:
                    liked_videos='https://www.youtube.com/playlist?list=LL'
                    wb.open(liked_videos)
                    print('opening liked videos in yotube')
                    speak('opening liked videos in yotube')
                elif 'open duck duck go search engine' in query:
                    ddg='https://duckduckgo.com/'
                    wb.open(ddg)
                    print('opening duck duck go search engine')
                    speak('opening duck duck go search engine')
                elif "empty recycle bin" in query:
                    winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)
                    keyboard.tap(Key.enter)
                    speak("Recycle Bin Emptied")
                elif "don't listen" in query or "stop listening" in query or "do not listen" in query:
                    speak("for how many seconds do you want me to sleep")
                    a = int(takeCommand().lower())
                    time.sleep(a)
                    speak = speak + \
                        str(a) + " seconds completed. Now you can ask me anything"
                elif 'get youtube notifications' in query:
                    mouse.position = (1426, 98)
                    mouse.move(5, -5)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    mouse.scroll(0, 2)
                    print('opened youtube notification')
                    speak('opened youtube notification')
                elif 'open trending videos in youtube' == query:
                    speak('okay let me find trending videos in youtube')
                    trending_vyt = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
                    wb.open(trending_vyt)
                    print('yt trending videos')
                    speak('done buddy')
                elif 'open youtube music page' == query:
                    speak('opening youtube music page')
                    yt_musicpage = 'https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured'
                    wb.open(yt_musicpage)
                    print('youtube music page opened')
                    speak('pom-pom brought you to the music world of youtube')
                elif 'delete temporary files' in query:
                    speak('okay lemme see')
                    dt="C:\\Users\\Rohan\\AppData\\Local\\Temp"
                    os.startfile(dt)
                    keyboard.press(Key.ctrl)
                    keyboard.tap('a')
                    keyboard.release(Key.ctrl)
                    print('queryed all \n')
                    keyboard.tap(Key.delete)
                    keyboard.tap(Key.enter)
                    print("deleted all temporary files")
                    speak("deleted all temporary files")
                elif "search" in  query:
                    query=query.replace('search','')
                    query=query.replace('in google','')
                    wb.open(f"https://www.google.com/search?q={query}")
                    speak(f"Opening {query} on google")
                elif "youtube" in query:
                    query=query.replace('search','')
                    query=query.replace('in youtube','')
                    wb.open(f"http://www.youtube.com/results?search_query={query}")
                    speak(f"Opening {query}on youtube")
                elif "take a note" in query:
                    print("........creating note.........")
                    create_note(query)
                    print("I have noted everything which you have said")
                elif 'open my notes' in query:
                    print(".........opening saved notes.........")
                    open_note(query)
                    print("\n\n________existing notes closed_________")
                elif 'clear my notes' in query:
                    print("_____deleting the file______")
                    delete_exisisting_note(query)
                    print("______File deleted______")
                elif 'take a list' in query:
                    print("_____Taking TODO list_____")
                    speak("hey buddy, choose a list in which you wanna add up, internal or external ")
                    print("\t\t\t\tInternal or External ?")
                    query=query.lower()
                    if 'internal' in query:
                        print("_______taking your internal notes_______")
                        add_internal_todo(query)
                        print('_____added up to Internal ToDo List_____')
                    elif 'external' in query:
                        add_external_todo(query)
                        print('_____added up to External ToDo List_____')
                elif "is there any pending works to do" in query or "pending workings list" in query:
                    print("_____Your TODO List_____")
                    speak("hey buddy, choose a to do list which you wanna Access, internal or external ")
                    print("\t\t\t\tInternal or External ?")
                    query=query.lower()
                    if 'internal' in query:
                        show_internal_todo(query)
                        print("End of Internal TODO List")
                    elif 'external' in query:
                        show_external_todo(query)
                        print("End of External TODO List")
                elif 'thank you' in query:
                    speak('you got it')
                elif "lock my system" in query:
                    speak("locking pc")
                    ctypes.windll.user32.LockWorkStation()
                
                elif "tell me the weather condition of" in query or 'weather condition' in query: # module error (scraping issue)
                    query=query.replace("tell me the weather conditions of",'')
                    query=query.replace("weather condition",'')
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                    def weather(city):
                        engine.setProperty('voice', voices[1].id)
                        engine.setProperty('rate', 165)
                        city = city.replace(" ", "+")
                        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                        soup = BeautifulSoup(res.text, 'html.parser')
                        location = soup.query('#wob_loc')[0].getText().strip()
                        time = soup.query('#wob_dts')[0].getText().strip()
                        info = soup.query('#wob_dc')[0].getText().strip()
                        weather = soup.query('#wob_tm')[0].getText().strip()
                        print(location)
                        print(time)
                        print(info)
                        print(weather+"°C")
                        speak(location)
                        speak(time)
                        speak(info)
                        speak(weather+"°C")
                    city = query
                    print(f"Searching {city} weather conditions in google......\n")
                    speak(f"Searching {city} weather conditions in google")
                    city = city+" weather"
                    weather(city)
                elif 'open gmail' in query:
                    gmail='www.gmail.com'
                    speak("opening your gmail account")
                    wb.open(gmail)
                elif 'download this video' == query:     #issue with module modify code               
                    keyboard.press(Key.ctrl)
                    keyboard.tap('l')
                    keyboard.release(Key.ctrl)
                    time.sleep(1)
                    keyboard.press(Key.ctrl)
                    keyboard.tap('c')
                    keyboard.release(Key.ctrl)
                    text=clipboard.paste()
                    
                    url = f"{text}"
                    print("\n\ncopied youtube video link :\t"+url)
                    yt = YouTube(url)
                    
                    print("\n")
                    print("_________________________Video Title_____________________________\n")
                    print("Video Title :\t"+yt.title+"\n")
                    filename = yt.title
                    print("_________________________Video Title_____________________________\n\n\n")
                    print("_________________________Thumbnail image link____________________\n")
                    print("Thumbnail link :\t"+yt.thumbnail_url+"\n")
                    print("_________________________Thumbnail image link____________________\n")
                    print("Downloading this video buddy....")
                    speak("Downloading this video buddy....")
                    print("\nWait Buddy Downloading this video buddy....")
                    print("_________________________please wait_____________________________\n")
                    print("\nWait Buddy Downloading this video buddy....")
                    print("_________________________wait Until download is finished_____________________________\n")
                    yt.streams.first().download(fr"./Software/downloads")
                    list = [1]
                    for i in tqdm(list):
                        time.sleep(2)
                    list = [1]
                    print(yt.title+"\tVideo downloaded")
                    print("________________________________download completed__________________________________\n")
                    speak("download completed")
                    time.sleep(3)
                    speak("do you want me to open the downloaded video?")
                    condition=takeCommand().lower()
                    if 'yes' == condition:
                        filename=yt.title
                        # filename = filename.replace("|", '')
                        video = fr"./Software/downloads/{filename}"
                        os.startfile(video)
                    elif 'no' in condition:
                        speak("okay not a problem")
                    else:
                        speak("hmmmmmm!, i think your not interested")
                    
                elif 'i want this video in mp3 format' == query :
                    speak("ya sure buddy")
                    youtube_video2mp3_converter()
                    print('video converted to Mp3')
                elif 'in jio saavn' in query or 'in jiosaavn' in query:
                    query = query.replace('in jio saavn', '')
                    query = query.replace('in jiosaavn', '')
                    speak(f"Okay buddy opening {query} song in jio saavn.")
                    print(f"yes buddy opening {query} song in jio saavn.")
                    saavn = f"https://www.jiosaavn.com/search/{query}"
                    wb.open(saavn)
                elif 'open  colors kannada channel' == query:
                    speak("opening colors kannada channel")
                    wb.open("https://vimoviesandtv.in/live-tv-channels/colors-kannada-hd/361388")
                elif 'hey google' == query:
                    if True:
                        okgoogle= pyautogui.locateCenterOnScreen("./Software/ok google.png")
                        if okgoogle is not None:
                            pyautogui.click(okgoogle)
                            print("Hey google activated!")
                        else:
                            print("Not found!")
                elif 'ok google' == query:
                    if True:
                        okgoogle= pyautogui.locateCenterOnScreen("./Software/google voice.png")
                        if okgoogle is not None:
                            pyautogui.click(okgoogle)
                            print("ok google activated!")
                        else:
                            print("Not found!")
                elif 'map' in query or 'open map' in query:
                    query=query.replace('map from','')
                    query=query.replace('open map from','')
                    query=query.replace('to','/')
                    print(query)
                    mapsite=f"https://www.google.com/maps/dir/{query}"
                    speak("ya buddy opening maps")
                    wb.open(mapsite)
                elif 'Record video' in query:
                    speak("okay buddy opening cam to record video")
                    if True:
                        subprocess.run('start microsoft.windows.camera:', shell=True)
                    speak("Hey buddy, look at the camera and just say, i'm ready. then ill start recording.")
                    while True:
                        print("----------------------------------\tI'm waiting for your command\t---------------------------------(camera)")
                        speak("im waiting for yours command.")
                        condition=takeCommand().lower()
                        if 'im ready' in condition or "i'm ready" in condition or 'ready' in condition:
                            videobutton= pyautogui.locateCenterOnScreen("./Software/videobutton.png")
                            try:
                                speak("Recording starts in.")
                                speak("3")
                                speak("2")
                                speak("1")
                                speak("Lights, camera, action.")
                                keyboard.tap(Key.space)
                            except Exception as e:
                                pyautogui.click(videobutton)
                                condition=takeCommand().lower()
                            if 'stop recording' in condition:
                                keyboard.tap(Key.space)
                                speak("would you like me to open the file location")
                                if 'yes' in condition or 'ok' in condition:
                                    speak("heading towards the file location")
                                    file = r"C:\Users\Rohan\Pictures\Camera Roll"
                                    os.startfile(file)
                                else:
                                    speak('okay not a problem..')
                                    speak("closing camera")
                                    keyboard.press(Key.ctrl)
                                    keyboard.tap(Key.f4)
                                    keyboard.release(Key.ctrl)
                                    break
                        elif 'im not ready' in condition or 'not yet' in condition or 'wait buddy' in condition:
                            speak("okay, i gonna wait another 30 seconds")
                            time.sleep(30)
                            if '' in condition:
                                break 
                elif 'open camera' in query:
                    speak("okay buddy opening camera")
                    if True:    
                        subprocess.run('start microsoft.windows.camera:', shell=True)
                    speak("Hey buddy, look at the camera and just say, capture to take a snap.")
                    time.sleep(4)
                    while True:
                        print("----------------------------------\tI'm waiting for your command\t---------------------------------(camera)")
                        speak("im waiting for yours command.")
                        condition=takeCommand().lower()
                        if 'capture' == condition or 'click' == condition:
                            capture= pyautogui.locateCenterOnScreen("./Software/capture.png")
                            try:
                                speak("lets take a snap in.")
                                speak("3")
                                speak("2")
                                speak("1")
                                speak("Lights, camera, action.")
                                pyautogui.click(capture)
                            except Exception as e:
                                keyboard.tap(Key.space)
                                condition=takeCommand().lower()
                            
                            speak("would you like me to open the file location")
                            if 'yes' in condition or 'ok' in condition:
                                speak("heading towards the file location")
                                file = r"C:\Users\Rohan\Pictures\Camera Roll"
                                os.startfile(file)
                            else:
                                speak('okay not a problem..')
                                speak("closing camera")
                                keyboard.press(Key.ctrl)
                                keyboard.tap(Key.f4)
                                keyboard.release(Key.ctrl)
                                break
                        elif 'wait buddy' in condition:
                            speak("okay, i gonna wait another 30 seconds")
                            time.sleep(30)
                            if '' in condition:
                                break 
                        elif 'stop' == condition or 'stop capturing' == condition:
                            break

                elif 'hide this file' in query or 'hide this folder' in query or 'hide this' in query:
                    os.system("attrib +h /s /d")

                elif 'open hidden files' in query:
                    os.system("attrib -h /s /d")

                elif 'in pdf drive' in query:
                    query=query.replace('search','') and query.replace('in pdf drive')
                    pdfdrive=f"https://www.pdfdrive.com/search?q={query}"
                    speak(f"opening {query} in pdfdrive website") 
                    print(f"opening {query} in pdfdrive website") 
                    wb.open(pdfdrive)    
                elif 'read pdf' in query:
                    speak("please tell me the pdf file name")
                    query=takeCommand().lower()
                    book=open (f'{query}.pdf', 'rb')
                    pdfReader = PdfFileReader(book)
                    pages = pdfReader.numPages
                    print(f"There are {pages} pages in this book")
                    speak(f"There are {pages} pages in this book")
                    print("Hey buddy please tell me the page number you want me to read")
                    query=takeCommand().lower()
                    query=query.replace("open page number",'')
                    query=query.replace("page number",'')
                    pg = int(query)
                    page = pdfReader.getPage(pg)
                    text = page.extractText()

                    print("---------------------------Pdf page----------------------------")
                    print(text)
                    speak(text)
                    print("---------------------------Pdf page----------------------------")

                    
                elif 'in gripper' in query or 'in grepper' in query: # first tell me the p-lang following with the question, by default it searches in py-lang(code grepper)
                    query=query.replace('in grepper','')
                    query=query.replace('in gripper','')
                    query=query.replace('search','')
                    query=query.replace('what is','')
                    codegrepper=f"https://www.codegrepper.com/code-examples/python/{query}" 
                    wb.open(codegrepper)
                elif 'hey buddy' == query:
                    speak("yes, tell me buddy. I'm still awake.")
                    speak('anything else from my side')
                    print('anything else from my side?')
                    query=takeCommand().lower()
                    if 'no' == query:
                        speak("okay not a problem i'll go to sleep")
                        break
                    else:
                        pass
                elif 'shut up'== query or 'sleep'==query:
                    if True:
                        speak("okay buddy, i'm gonna sleep now.")
                        break
                elif 'full screen window' == query:
                    keyboard.tap(Key.f11)
                
                elif "what's the petrol price" == query: #error: NonType object is not callable
                    link = "https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-karnataka.cms"
                    speak("fetching info from economic times website")
                    res= requests.get(link)
                    soup=BeautifulSoup(res.text,"lxml")
                    karnataka = soup.find('div', {'class': 'heading moretext'})
                    karnataka=str(karnataka.text)
                    print(karnataka[0:74]+karnataka[118:155]) 
                    speak(karnataka[0:74]+karnataka[118:155])
                    speak('please lemme know if you wanna know more on this topic')
                    topic=takeCommand().lower()
                    if 'yes' in topic or 'okay' in topic:
                        print(karnataka[185:902])
                        speak(karnataka[185:902])
                    else:
                        print("exit -> petrol updates")
                elif 'favourite songs in jio saavn'==query or 'favourite songs in jiosaavn' == query:
                    link="https://www.jiosaavn.com/s/playlist/0be5b92e9871d4f0351f69a443017cff/Kannada/H4SrPKEeBf1ieSJqt9HmOQ__"
                    speak("playing your favourite songs, from your playlist in jio saavn")
                    wb.open(link)
                    time.sleep(3)
                    play_list=pyautogui.locateCenterOnScreen("./Software/playlist_button.png")
                    if play_list is not None:
                        pyautogui.click(play_list)
                        print("playing Fav playlist in jiosaavn!")
                elif 'spotify' in query:
                    query=query.replace('spotify play','')
                    query=query.replace('spotify','')
                    query=query.replace('in spotify','')
                    link = f"https://open.spotify.com/search/{query}"
                    wb.open(link)
                    print(f"playing {query} in spotify")
                    time.sleep(11)
                    mouse = Controller()
                    print('The current pointer position is {0}'.format(mouse.position))
                    mouse.position = (484, 315)
                    print('Now the pointer position moved it to {0}'.format(mouse.position))
                    mouse.move(5, -5)
                    print("process completed successfully...")
                    time.sleep(3)
                    play_btn = pyautogui.locateCenterOnScreen('splay.png')
                    if play_btn is not None:
                        pyautogui.click(play_btn)
                elif 'add this song to my favourite list' in query:
                    query = query.replace('add this song to my favourite list', '')
                    if 'spotify'==query or 'in spotify'==query:
                        s_addFav = pyautogui.locateCenterOnScreen('spotify add to fav.png')
                        if s_addFav is not None:
                            pyautogui.click(s_addFav)
                            print(f"adding {query} to you favourite songs list in spotify!")
                elif 'get latest news updates' ==query or 'latest new updates' == query:
                    speak("ya sure buddy")
                    print("In which language buddy, english or kannada?")
                    speak("In which language buddy, english or kannada?")

                    query = takeCommand().lower()
                    if 'kannada' in query:
                        print("fetching Kannada Latest news...")
                        speak("fetching Kannada Latest news...")
                        k.knews()
                    elif 'english' in query:
                        print("fetching English Latest news...")                        
                        speak("fetching English Latest news...")
                        english.enews()

                elif 'get some news updates' == query or 'get some recent news updates' == query:
                    speak("ya sure buddy")
                    speak("in which language buddy, english or kannada?")
                    query=takeCommand().lower()
                    if 'kannada' in query:
                        speak("plese wait Buddy fetching data...")
                        res = requests.get('https://www.60secondsnow.com/kn/')
                        soup = BeautifulSoup(res.text, 'lxml')
                        data = soup.find('div', {"class": "listingpage"})
                        articles = data.find_all('article')
                        print("*********************************************************************************Headlines***************************************************************************************************************")
                        for article in articles:
                            adds = article.find('div', {'class': 'photos-add'})
                            if adds in article:
                                continue

                            postcontainer = article.find('div', {"class": "post-container"})
                            article_content = postcontainer.find(
                                'div', {'class': 'post-header clearfix'})

                            article_content = article_content.find('div', {'class': 'article-content'})
                            header = article_content.find('h2')
                            updated_time = article_content.find('div', {'class': 'article-datetime'})

                            categories = updated_time.find('a')

                            article_desc = article_content.find('div', {'class': 'article-desc'})
                            article_desc = article_desc.find('p')
                            updated_time = updated_time.text
                            if '-' in updated_time:
                                updated_time = updated_time.replace('-', '')
                            if 'min ago' in updated_time:
                                updated_time = updated_time.replace('min ago', 'ನಿಮಿಷದ ಹಿಂದೆ')
                            article_desc = article_desc.text
                            categories = categories.text
                            print(f"\n\n\nHeadlines: {header.text}\n\nCategory: {categories[23:]}\n\nNews updated time: {updated_time[40:]}\n")
                            print("*************************************************************************Article*************************************************************************************************************************")
                            print(f"\n{article_desc}\n")
                            print("*********************************************************************************************************************************************************************************************************\n\n\n")

                            updates_readerInkannada = f"""ವರ್ಗ {categories[23:]}. ಅಪ್‌ಲೋಡ್ ಅಧಾ ಸಮಯ {updated_time[38:]}. {article_desc} ಈ ರೀತಿ ಬರಹಗಾರ ಹೇಳುತ್ತಾರೆ"""
                            language = 'kn'
                            myobj = gTTS(text=updates_readerInkannada, lang=language, slow=False)
                            file = "kannada reader.mp3"
                            myobj.save(file)
                        AudioPlayer(file).play(loop=False, block=True)
                        os.remove(file)



                    elif 'english' in query:
                        res=requests.get('https://www.60secondsnow.com/')
                        soup=BeautifulSoup(res.text,'lxml')
                        data=soup.find('div',{"class":"listingpage"})
                        articles=data.find_all('article')
                        speak("plese wait Buddy fetching data...")
                        for article in articles:
                            adds = article.find('div', {'class': 'photos-add'})
                            if adds in article:
                                continue
                            postcontainer = article.find('div', {"class": "post-container"})
                            article_content = postcontainer.find('div', {'class': 'post-header clearfix'})
                            
                            article_content = article_content.find('div', {'class': 'article-content'})
                            header=article_content.find('h2')
                            updated_time = article_content.find('div', {'class': 'article-datetime'})

                            categories=updated_time.find('a')

                            article_desc=article_content.find('div',{'class':'article-desc'})
                            article_desc=article_desc.find('p')
                            updated_time=updated_time.text
                            if '-' in updated_time:
                                updated_time=updated_time.replace('-','')
                            article_desc=article_desc.text
                            categories=categories.text
                            print(f"\n\n\nHeadlines: {header.text}\n\nCategory: {categories[23:]}\n\nNews updated time: {updated_time[40:]}\n")
                            print("*************************************************************************Article*************************************************************************************************************************")
                            print(f"\n{article_desc}\n")
                            print("*********************************************************************************************************************************************************************************************************\n\n\n")
                            print('-------------------------------------------------------------------------------------------------------------------------------\n')
                            updates_readerInEnglish1 = f"""Category {categories[23:]}, the news was uploaded {updated_time[40:]}, The article says {article_desc}"""

                            language = 'en'
                            myobj = gTTS(text=updates_readerInEnglish1,
                                        lang=language, slow=False)
                            file = "english reader1.mp3"
                            myobj.save(file)
                        AudioPlayer(file).play(loop=False, block=True)
                        os.remove(file)
                elif "open insta story" ==query:
                    speak("okay")
                    insta_story()
                elif "clear clipboard" == query:
                    speak("clearing clipboard")
                    clearall = pyautogui.locateCenterOnScreen("./Software/clearall.png")
                    print(clearall)
                    if clearall is not None:
                        pyautogui.click(clearall)
                        print("clipboard empty!")
                    keyboard.tap(Key.esc) #closing clipboard
                    speak("Done!")
                
                elif 'dictionary ' in query:
                    question=query.replace('dictionary search','')
                    question=question.replace(' ','%20')
                    link = f"https://www.google.com/search?q=meaning%20of%20{question}&gs_ivs=1#tts=0&dobs={question}"
                    wb.open(link)
                
                elif 'connect to my device' == query:
                    os.system('adb connect 192.168.1.101:9090')
                if 'connect my device' == query:
                    try:
                        os.system('adb connect 192.168.1.101:9090')
                    except:
                        print('IP address please...')
                        speak('tell me the ip address')
                        query = takeCommand().lower()
                        query = query.replace('port number', ':')
                        query = query.replace(' ', '')
                        os.system(f'adb connect {query}')


                elif 'call' == query:
                    print("Tell me the Person name: ")
                    speak("Tell me the Person name: ")
                    query=takeCommand().lower()
                    call_book = {'ajji':'7676062533','amma':'7483132135','akka':'7411678135','appa':'9480477169','anita Mam':'9901006412','arpitha':'9972691769','janaki Mam':'9480443972','khushi':'8088408445','komal':'6360696740','naveen':'8050039951','nayana akka':'6364414046','nishu':'8095820463','pranitha':'8296132796','pushpa aunty':'9008252604','rishi':'8861742604','sachin':'7795442095','sai bro bhalki':'6362587380','sangeetha Mam':'9035298900','santhu':'8088152109','sarika':'9108975122','shashi biradar':'9110239301','shashidhar':'8147484364','shilpa mam':'7022007065','appaji':'9008099597'}  # ------------- List of phone number
                    names=f'{list(call_book)}'
                    person = query
                    print(f'Searching {person} in callbook...')
                    if person in names: 
                        print("command accepted...")
                        call(person)
                
                elif 'cut the call' == query:
                    call_End()

                elif 'on loudspeaker' == query or 'off loudspeaker' ==query:
                    on_Off_LoudSpeaker()
                
                elif 'mute call'==query or 'unmute call'==query:
                    OnOff_mutecall()

                elif 'open keypad'==query:
                    call_dailing_Keypad()

                elif 'dial' in query:
                    rnumber = query.replace('dial', '')
                    rnumber=rnumber.replace(' ','')
                    print(f'Dailing {rnumber} please wait')
                    dail_random(rnumber)

                elif 'connect bluetooth' ==query or 'disconnect bluetooth'==query:
                    connectBluetooth()

                elif 'put the call on hold' ==query:
                    callhold_onOff()

                elif 'remove hold'==query:
                    resume_call()

                elif 'add coference call'==query or 'merge call' ==query:
                    os.system('adb shell input tap 735 525')

                elif 'swap call' ==query or 'switch call' ==query:
                    os.system('adb shell input tap 918 528')

                elif "android version"== query:
                    os.system('adb shell getprop "ro.build.version.release"')

                elif 'disconnect my device' == query:
                    try:
                        os.system('adb disconnect 192.168.1.100:5555')
                    except:
                        query = takeCommand().lower()
                        print('IP adress please...')
                        query = takeCommand().lower()
                        query = query.replace('port number', ':')
                        query = query.replace(' ', '')
                        os.system(f'adb disconnect {query}')

                elif 'build connect' == query:
                    os.system('adb tcpip 5555')

                elif 'change port number' ==query:
                    mylist = ["5555", "8080", "9090","6969"]
                    import random
                    os.system(f'adb tcpip {random.choice(mylist)}')

                elif 'add call'== query:
                    add_call()
                                
                
                    
                
                elif "bye buddy"== query or 'bye'== query or "im going out bye"==query or 'got some work to do bye' ==query:
                    # playsound(r"Off.mp3")
                    time.sleep(2)
                    print("Processing....")
                    print("Turning off...")
                    speak("Hey Buddy, deactivated.")
                    print(">>>>>>>>>>>>>>>>>>[ Hey Buddy Deactivated ]<<<<<<<<<<<<<<<<<<<<<")
                    sys.exit()
        if True:
            print("\t\t\t\tSay Hey Buddy to activate your Assistant.")
            while True:
                query=takeCommand().lower()
                if 'hey buddy' in query:
                    msg.notify(title="Hey Buddy!", message="Yes buddy, I'm waiting for your command...",
                            app_icon=r'./Software/HB-icon.ico', timeout=3)
                    wakeupBuddy()
                elif "bye buddy" in query:
                    playsound(
                        r"./Software/Off.mp3")
                    time.sleep(2)
                    print("Processing....")
                    print("Turning off...")
                    speak("Hey Buddy deactivated")
                    msg.notify(title="Hey Buddy!",message="Hey Buddy Deactivated...",app_icon=r'./Software/HB-icon.ico', timeout=3)
                    print('\033[92m>>>>>>>>>>>>>>>>>>>>[\033[00m' +" Hey Buddy Deactivated "+'\033[92m]<<<<<<<<<<<<<<<<<<<<\033[00m')
                    
                    sys.exit()
    
                        
    else:
        import vlc
        good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
        try:
            ply = vlc.MediaPlayer(r"./Software/denied.mp3")
            while str(ply.get_state()) in good_states:
                ply.play()
            print("\033[91mAccess denied!\033[00m")
            speak("Access denied!")
            print("Unauthorized user")
            m = vlc.MediaPlayer(r"./Software/Off.mp3")
            while str(m.get_state()) in good_states:
                m.play()
        except:
            print("ON")
        print("\033[93m>>>>>>>>>>>>>>>>>>[ Hey Buddy Deactivated ]<<<<<<<<<<<<<<<<<<<<\033[00m3")
        speak("Hey Buddy Deactivated")
        speak("locking pc")
        ctypes.windll.user32.LockWorkStation()
        sys.exit()
