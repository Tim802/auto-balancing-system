from CustomtkinterBase import App, Frame, Button, TextEntry, Label

def log_in_attempt():
    pass

def sign_in_attempt():
    pass

#this should be parsed into a class of CustomtkinterBase that should create the website with a command to start the mainloop
layout = {
    "title": "Log In Page",
    "dim": "600x500",
    "CentralFrame": {
        "obj": "Frame",
        "master": "PLACEHOLDER",
        "row": 0,
        "col": 0,
        "padx": 100,
        "pady": 20,
        "sticky": "ew",
        "contains": {
            "TitleFrame": {
                "obj": "Frame",
                "master": "PLACEHOLDER",
                "row": 0,
                "col": 0,
                "padx": 20,
                "pady": 20,
                "sticky": "ew",
                "contains": {
                    "PageTitle": {
                        "obj": "Label",
                        "master": "PLACEHOLDER",
                        "row": 0,
                        "col": 0,
                        "padx": 20,
                        "pady": 20,
                        "sticky": "ew",
                        "text": "Please Enter Your Log In Details"
                    }
                }
            },
            "EntryFrame": {
                "obj": "Frame",
                "master": "PLACEHOLDER",
                "row": 1,
                "col": 0,
                "padx": 20,
                "pady": 20,
                "sticky": "ew",
                "contains": {
                    "EmailEntry":{
                        "obj": "TextEntry",
                        "master": "PLACEHOLDER",
                        "row": 0,
                        "col": 0,
                        "padx": 20,
                        "pady": 20,
                        "sticky": "ew",
                        "text": "Enter Your Email"
                    },
                    "PasswordEntry": {
                        "obj": "TextEntry",
                        "master": "PLACEHOLDER",
                        "row": 1,
                        "col": 0,
                        "padx": 20,
                        "pady": 20,
                        "sticky": "ew",
                        "text": "Enter Your Password"
                    }
                }
            },
            "ButtonFrame": {
                "obj": "Frame",
                "master": "PLACEHOLDER",
                "row": 2,
                "col": 0,
                "padx": 20,
                "pady": 20,
                "sticky": "ew",
                "contains": {
                    "LoginButton": {
                        "obj": "Button",
                        "master": "PLACEHOLDER",
                        "row": 0,
                        "col": 0,
                        "padx": 20,
                        "pady": 20,
                        "sticky": "ew",
                        "text": "Log In",
                        "command": log_in_attempt
                    },
                    "SignUpButton": {
                        "obj": "Button",
                        "master": "PLACEHOLDER",
                        "row": 0,
                        "col": 1,
                        "padx": 20,
                        "pady": 20,
                        "sticky": "ew",
                        "text": "Sign Up",
                        "command": sign_in_attempt
                    }
                }
            }
        }
    }
}