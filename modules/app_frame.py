import tkinter as tk
class chatterTalk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatter Talk")
        self.geometry('500x500')
        self.create_widgets()
        #self.create_buttons()
    def create_widgets(self):
        self.label = tk.Label(self, text='Welcome to Chatter Talk')
        self.label.pack(pady=10)
    #def create_buttons(self):
        #self.input
        #self.clarify