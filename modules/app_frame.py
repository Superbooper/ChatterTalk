import tkinter as tk
from modules.chatter import converse
from modules.speaker import speaker
class chatterTalk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatter Talk")
        self.geometry('600x400')
        self.config(bg='dark grey')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        #volume and rate sliders variables
        self.volume = tk.DoubleVar(value = 0.5)
        self.rate = tk.IntVar(value = 250)
        self.create_widgets()
        #submit button
        self.submit_btn = tk.Button(self, text='Submit', command=self.text_submission_user)
        self.submit_btn.grid(row=1, column=1,)

    def create_widgets(self):
        '''
        creates the widgets for the tkinter chatter talk app
        '''
        # header
        self.label = tk.Label(self, text='Welcome to Chatter Talk')
        self.label.grid(pady=10)
        #text box for display
        self.text_bx = tk.Text(self, height= 30, width=40, wrap='word', font=('Arial', 10))
        self.text_bx.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.text_bx.insert(1.0,'System - Welcome to ChatterTalk, Please type a message and hit submit to begin!\n')
        self.text_bx.config(state='disabled')
        #scroll bar for chat history
        self.scrollbar_txt = tk.Scrollbar(self, command=self.text_bx.yview)
        self.scrollbar_txt.grid(row=0, column=1, sticky='ns', pady=10)
        self.text_bx['yscrollcommand'] = self.scrollbar_txt.set
        # text box for user submission
        self.text_enter = tk.Text(self, height=5, width=2, wrap='word', font =('Arial', 10))
        self.text_enter.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        #rate and volume sliders
        self.volume_label = tk.Label(self,text='Volume')
        self.volume_label.grid(row=1,column=2, padx = 15, pady=50)
        self.volume_scale = tk.Scale(
            self,
            from_=10.00,
            to=0.00,
            orient=tk.VERTICAL,
            resolution=0.001,
            length=300,
            variable=self.volume
        )
        self.volume_scale.grid(row=0,column=2, padx=10,pady=10)
        self.rate_label = tk.Label(self, text='rate')
        self.rate_label.grid(row=1,column=3, padx = 15, pady=50)
        self.rate_scale = tk.Scale(
            self,
            from_=1000,
            to=0,
            orient=tk.VERTICAL,
            resolution=1,
            length=300,
            variable=self.rate
        )
        self.rate_scale.grid(row=0,column=3, padx=20,pady=10)
    def text_submission_user(self):
        '''
        function to handle displaying and handling user input and bot responses
        handles inner object variables and has no input or return values
        '''
        message =  self.text_enter.get(1.0, 'end-1c')
        self.text_enter.delete(1.0, 'end')
        self.text_bx.config(state='normal')
        #puts users message into chat
        self.text_bx.insert('end', f"user- {message}\n")
        #passes user message to bot
        response = converse(message)
        #speak response 
        speaker(response, self.rate.get(), self.volume.get())
        #display it
        self.text_bx.insert('end', f'bot - {response}\n')
        self.text_bx.config(state='disabled')


