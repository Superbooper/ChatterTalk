import speech_recognition
import os
import pyaudio
import sphinx
# get mic audio
def user_speech_grab():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        #space for tk console slot here
        audio = r.listen(source)
    #recognize speech
    r.recognize_wi