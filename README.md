# ChatterTalk 
Chatter talk is a combination project aiming to give the ChatterBot Project a voice through the
Pyttsx3 library. At its core it utilizes tkinter and the Pyttsx3 to give a GUI
in Which you can control how to bot speaks and interact with it.
## Requirement Installation
There is a requirements.txt file you must create a venv from in order to run the application
once you are in the venv you just created run the main.py file, the GUI will 
pop up and your ready to use.
You may need to install the Espeak module seperately which pyttsx3 needs to run
## How to use
Once your in the gui youll see 5 elements
1. the Upper chat box is to see the chat history and responses in text form.
2. in the bottom box you will type you messages to the bot 
3. once your message is written hit the submit button to send it to the bot
4. the volume slider is used to control the volume bot and is set to go between 0
5. the rate slider this controls the rate at which the bot speaks in WPM
    (words per minute), this is set to 0-1000, but anything above 250 may be difficult
    to understand.