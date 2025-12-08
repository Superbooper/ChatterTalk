import speech_recognition as sr
import pyttsx3
import sphinx
# get mic audio
def user_speech_grab():
    r= sr.Recognizer()
    with sr.Microphone(device_index=16) as source:
        #space for tk console slot here
        audio = r.listen(source)
        text = r.recognize_sphinx(audio)
        print(text)
user_speech_grab()