import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate', 1000.00)
engine.setProperty('volume', 1.0)
engine.say('fox')
engine.runAndWait()
