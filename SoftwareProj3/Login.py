import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master)
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.rowNum = rowNum
        self.colNum = colNum

        self.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)
        self.grid_rowconfigure(self.rowNum, weight=1)
        self.grid_columnconfigure(self.colNum, weight=1)

class LoginFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add entry frame, button frame, and title frame
        self.title = TitleFrame(self, 0, 0, 20, 20, 'ew', 0, 0)
        self.entry = EntryFrame(self, 1, 0, 20, 20, 'ew', (0,1), 0)
        self.buttons = ButtonFrame(self, 2, 0, 20, 20, 'ew', 0, (0,1))

class ButtonFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add buttons
        self.login = LoginButton(self, 0, 0, 20, 20, 'ew', 'Log In')
        self.signup = SignUpButton(self, 0, 0, 20, 20, 'ew', 'Sign Up')

class EntryFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add text entries
        self.email = EmailEntry(self, 0, 0, 20, 20, 'ew', 'Enter Your Email')
        self.password = PasswordEntry(self, 0, 0, 20, 20, 'ew', 'Enter Your Password')

class TitleFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add title labels
        self.title = PageTitle(self, 0, 0, 20, 20, 'ew', 'Please Enter Your Log In Details')

class Widget:
    def __init__(self, master, row, col, padx, pady, sticky, text):
        self.master = master
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.text = text

class Button(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.button = ctk.CTkButton(self.master, text=self.text, command=self.button_event)

    def button_event():
        print('Button Pressed')

class LoginButton(Button):
    def button_event():
        print('Login Button Pressed')

class SignUpButton(Button):
    def button_event():
        print('Sign Up Button Pressed')

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.textentry = ctk.CTkEntry(self.master, placeholder_text=self.text)

class EmailEntry(TextEntry):
    pass

class PasswordEntry(TextEntry):
    pass

class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.label = ctk.CTkLabel(self.master, text=self.text)

class PageTitle(Label):
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Log In Page')
        self.geometry('600x500')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.loginframe = LoginFrame(self, 0, 0, 100, 20, 'ew', (0, 1, 2), 0)

#instantiate the app
app = App()
app.mainloop()