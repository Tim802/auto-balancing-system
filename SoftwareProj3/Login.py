import customtkinter as tkinter

class LoginFrame(tkinter.CTkFrame):
    def __init__(self, master, row, col):
        super().__init__(master)
        self.row = row
        self.col = col
        self.grid(row=self.row, column=self.col, padx=20, pady=20, sticky='nsew')

        self.buttons = ButtonFrame(self, 0, 0)
        self.email = TextEntry(self, 'Enter Your Email', 1, 0)
        self.password = TextEntry(self, 'Enter Your Password', 2, 0)

class ButtonFrame(tkinter.CTkFrame):
    def __init__(self, master, row, col):
        super().__init__(master)
        self.row = row
        self.col = col
        self.grid(row=self.row, column=self.col, padx=20, pady=(10, 0), sticky='ew')

        self.loginbutton = LoginButton(self,'Log In', 0, 0)
        self.signinbutton = SignUpButton(self, 'Sign Up', 0, 1)

class Button(LoginFrame):
    def __init__(self, master, text, row, col):
        self.frame = master
        self.text = text
        self.row = row
        self.col = col
        self.button = tkinter.CTkButton(self.frame, text=self.text, command=self.button_event)
        self.button.grid(row=self.row, column=self.col, padx=20, pady=(10, 0))

    def button_event():
        pass

class LoginButton(Button):
    def button_event():
        #check login creds, move to page if required.
        pass

class SignUpButton(Button):    
    def button_event():
        #take to signup page
        pass

class TextEntry(LoginFrame):
    def __init__(self, master, temptxt, row, col):
        self.frame = master
        self.temptext = temptxt
        self.entry = tkinter.CTkEntry(self.frame, placeholder_text=self.temptext)

        self.row = row
        self.col = col
        #self.grid(row=self.row, column=self.col, padx=20, pady=(10, 0), sticky='ew')

    def call_text(self):
        self.text = self.entry.get()
        return self.text

class App(tkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Login Page')
        self.geometry('600x500')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.loginframe = LoginFrame(self, 0, 0)

#instantiate the app
app = App()
app.mainloop()