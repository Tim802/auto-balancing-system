import customtkinter as ctk
from DataHandling import Encryption, DatabaseAccess

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
        self.signup = SignUpButton(self, 0, 1, 20, 20, 'ew', 'Sign Up')

class EntryFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add text entries
        self.email = EmailEntry(self, 0, 0, 20, 20, 'ew', 'Enter Your Email')
        self.password = PasswordEntry(self, 1, 0, 20, 20, 'ew', 'Enter Your Password')

class TitleFrame(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, rowNum, colNum):
        super().__init__(master, row, col, padx, pady, sticky, rowNum, colNum)

        #add title labels
        self.title = PageTitle(self, 0, 0, 20, 20, 'ew', 'Please Enter Your Log In Details')

class Widget(Frame):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        self.master = master
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.text = text

    def arrange(self, widget):
        widget.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)        

class Button(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkButton(self.master, text=self.text, command=self.button_event)
        self.arrange(self.widget)

    def button_event(self):
        print('Button Pressed')

class LoginButton(Button):
    def button_event(self):
        print('Login Button Pressed')
        #call login attempt function
        app.log_in_attempt()

class SignUpButton(Button):
    def button_event(self):
        print('Sign Up Button Pressed')

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkEntry(self.master, placeholder_text=self.text)
        self.arrange(self.widget)

class EmailEntry(TextEntry):
    def find_email(self):
        inp = self.widget.get()
        enc = Encryption.encrypt(inp)

        Users = DatabaseAccess.retreive_all('EMAIL')

        for n in Users:
            print(n)
            print(enc.decode())
            if Encryption.check(enc, n[0]):
                user_id = DatabaseAccess.retreive_id(enc.decode(), 'EMAIL')
                return user_id
        else:
            return 0
        
class PasswordEntry(TextEntry):
    def password_check(self, user_id):
        inp = self.widget.get()
        enc = Encryption.encrypt(inp)
        db_pass = DatabaseAccess.retreive_val(user_id, 'id', 'PASSWORD')

        if Encryption.check(enc.decode(), db_pass.encode()):
            return True
        else:
            return False

class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkLabel(self.master, text=self.text)
        self.arrange(self.widget)

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

    def log_in_attempt(self):
        email_id = self.loginframe.entry.email.find_email()
        print(email_id)
        if email_id == 0:
            print('Invalid Email, Log In Failed')
            return
        elif self.loginframe.entry.password.password_check(email_id):
            print('Valid login details, Login Successful')
            return
        else:
            print('Invalid Password, Login Failed')
            return

#instantiate the app
app = App()
app.mainloop()

#closes user database when not in use
DatabaseAccess.close_connection()