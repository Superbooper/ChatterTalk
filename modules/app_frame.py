import tkinter as tk
from modules.chatter import converse
from modules.speaker import speaker
class chatterTalk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatter Talk")
        self.geometry('500x500')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(1, weight=0)
        self.create_widgets()
        #self.create_buttons()
    def create_widgets(self):
        # header
        self.label = tk.Label(self, text='Welcome to Chatter Talk')
        self.label.grid(pady=10)
        #text box for display
        self.text_bx = tk.Text(self, height= 30, width=40, wrap='word', font=('Arial', 10))
        self.text_bx.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.text_bx.insert(1.0,'System - Welcome to ChatterTalk, Please type a message and hit enter to begin!')
        self.text_bx.config(state='disabled')
        #scroll bar for chat history
        self.scrollbar_txt = tk.Scrollbar(self, command=self.text_bx.yview)
        self.scrollbar_txt.grid(row=0, column=1, sticky='ns', pady=10)
        self.text_bx['yscrollcommand'] = self.scrollbar_txt.set
        # text box for user submission
        self.text_enter = tk.Text(self, height=15, width=2, wrap='word', font =('Arial', 10))
        self.text_enter.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        #checks and displays user input
        self.text_enter.bind('<Return>', self.text_submission_user())
    #def create_buttons(self):
        #self.input
        #self.clarify
    def text_submission_user(self):
        '''
        small inner fucntion to allow top box to be non interactable by user
        displays user message to chat
        passes user message to bot and returns bot response
    
        '''
        message =  self.text_enter.get(1.0, 'end-1c')
        self.text_enter.delete(1.0, 'end')
        self.text_bx.config(state='normal')
        #puts users message into chat
        self.text_bx.insert(1.0, f"user- {message}")
        #passes user message to bot
        response = converse(message)
        #speak response 
        speaker(response)
        #display it
        self.text_bx.insert(1.0, f'bot - {response}')
        self.text_bx.config(state='disabled')


