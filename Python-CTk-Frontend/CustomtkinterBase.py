import customtkinter as ctk

class Window:
    def __init__(self, layout_dict):
        self.layout = layout_dict
        self.title = self.layout["title"]
        self.dimensions = self.layout["dim"]

        self.initframe = Frame()


        #run decode on massive dictionary

        #init proper classes based on obj id and parameters
        pass

    def run(self):
        #init app and run mainloop

        #close dependencies when finished (may be done on the page locally)
        pass

    def class_instance_finder(self, obj_dict, obj_key):
        obj_type = obj_dict["obj"]

        def class_identifier(obj, name):
            if obj in globals():
                ObjectClass = globals()[obj]
                return ObjectClass(name)
            else:
                print(f"ERROR: Object Class {obj} cannot be found")
                return None
            
        return class_identifier(obj_type, obj_key)    
        
class Frame(ctk.CTkFrame):
    def __init__(self, master, row, col, padx, pady, sticky, contains):
        super().__init__(master)
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.contain = contains

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
        self.widget = ctk.CTkButton(self.master, text=self.text, command=self.button_event)

    def button_event(self):
        print("button moment")

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkEntry(self.master, placeholder_text=self.text)

class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkLabel(self.master, text=self.text)

class App(ctk.CTk):
    def __init__(self, headtext, dimensions, contains):
        super().__init__()
        self.headtext = headtext
        self.dimensions = dimensions
        self.contain = contains

        self.title(self.headtext)
        self.geometry(self.dimensions)
