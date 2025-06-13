import customtkinter as tkinter

class LoginFrame(tkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(self, master)

class App(tkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = 'Login Page'
        self.geometry = '600x500'
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
