import pyttsx3
engine=pyttsx3.init()
#engine.setProperty('rate', 100)
#engine.setProperty('volume', 1.0)
engine.say('the quick brown fox jumped over the log')
engine.runAndWait()