import speech_recognition as sr
import pyaudio
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

query = takeCommand().lower()

if query=="hi":
    print("Hello buddy")

elif query=="hello":
    print("Hello buddy")