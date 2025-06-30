from CustomtkinterBase import Window, InvLogin
from DataHandling import Encryption, DatabaseAccess
import sys
import subprocess

def log_in_attempt():
    print("login button pressed")
    inp_email = login.application.contain["CentralFrame"].contain['EntryFrame'].contain['EmailEntry'].text_return()
    inp_password = login.application.contain["CentralFrame"].contain['EntryFrame'].contain['PasswordEntry'].text_return()
    print(inp_email, inp_password)
    print('shmigus')

    data = Encryption.Encrypt(inp_email, inp_password)
    db = DatabaseAccess.fetch()
    print('database:', db)
    id_list = []
    email_list = []
    password_list = []

    for n in db:
        id_list.append(n[0])
        email_list.append(n[1])
        password_list.append(n[2])

    for i in email_list:
        if data.hash_checker(data.b_email, i):
            user_index = email_list.index(i)
            valid_email = True
            break
    else:
        valid_email = False
        err_msg = InvLogin()

    print('valid email:', valid_email)

    if valid_email:
        if data.hash_checker(data.b_password, password_list[user_index]):
            print('Valid email and password. Login successful')
            subprocess.Popen(['python', 'python-CTk-Frontend/Pyser_V1.py'])
            sys.exit("Login Complete")            
        else:
            print("Invalid Password entered")
            err_msg = InvLogin()

def sign_in_attempt():
    print("sign in button pressed")

#this should be parsed into a class of CustomtkinterBase that should create the website with a command to start the mainloop
layout = {
    "title": "Log In Page",
    "dim": "600x500",
    "CentralFrame": {
        "obj": "Frame",
        "params": {
            "row": 0,
            "col": 0,
            "padx": 100,
            "pady": 20,
            "sticky": "ew"
        },
        "contains": {
            "TitleFrame": {
                "obj": "Frame",
                "params": {
                    "row": 0,
                    "col": 0,
                    "padx": 20,
                    "pady": 20,
                    "sticky": "ew"
                },
                "contains": {
                    "PageTitle": {
                        "obj": "Label",
                        "params": {
                            "row": 0,
                            "col": 0,
                            "padx": 20,
                            "pady": 20,
                            "sticky": "ew",
                            "text": "Please Enter Your Log In Details"
                        }
                    }
                }
            },
            "EntryFrame": {
                "obj": "Frame",
                "params": {
                    "row": 1,
                    "col": 0,
                    "padx": 20,
                    "pady": 20,
                    "sticky": "ew"
                },
                "contains": {
                    "EmailEntry":{
                        "obj": "TextEntry",
                        "params": {
                            "row": 0,
                            "col": 0,
                            "padx": 20,
                            "pady": 20,
                            "sticky": "ew",
                            "text": "Enter Your Email"
                        }
                    },
                    "PasswordEntry": {
                        "obj": "TextEntry",
                        "params": {
                            "row": 1,
                            "col": 0,
                            "padx": 20,
                            "pady": 20,
                            "sticky": "ew",
                            "text": "Enter Your Password"
                        }
                    }
                }
            },
            "ButtonFrame": {
                "obj": "Frame",
                "params": {
                    "row": 2,
                    "col": 0,
                    "padx": 20,
                    "pady": 20,
                    "sticky": "ew"
                },
                "contains": {
                    "LoginButton": {
                        "obj": "Button",
                        "params": {
                            "row": 0,
                            "col": 0,
                            "padx": 20,
                            "pady": 20,
                            "sticky": "ew",
                            "text": "Log In",
                            "command": log_in_attempt
                        }
                    }                    
                }
            }
        }
    }
}

login = Window(layout)
login.run()