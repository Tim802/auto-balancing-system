import customtkinter as ctk
import pygyat


class Window:
    def __init__(self, layout_dict):
        self.layout = layout_dict
        self.title = self.layout["title"]
        self.dimensions = self.layout["dim"]
        self.application = App(self.title, self.dimensions)

    def run(self):
        print(f"Initialising Page: {self.title}")
        self.layout_object_dict = self.decode_input_dict(self.layout, self.application)
        self.application.run(self.layout_object_dict)
        self.application.mainloop()
        #may need to close dependencies after running

    def text_get(self):
        print("gathering text entries")
        entered_text_dict = {}
        print(self.layout_object_dict.items())
        for key, object in self.layout_object_dict.items():
            if isinstance(object, dict):
                print("dict object found")
                if object["obj"] == 'TextEntry':
                    entered_text = object.text_return()
                    entered_text_dict.update({key: entered_text})

        print(entered_text_dict)
        return entered_text_dict
    
    def decode_input_dict(self, inp_dict, master_object):
        output_dict = {}
        for key, object in inp_dict.items():
            if isinstance(object, dict):
                if "contains" in object:
                    new_class = self.class_constructor(object)
                    new_class_instance = new_class(master=master_object, **object["params"])
                    container_objects = self.decode_input_dict(object["contains"], new_class_instance)
                    new_class_instance.contain = container_objects
                    new_class_instance.arrange()
                    output_dict.update({key: new_class_instance})
                else:
                    new_class = self.class_constructor(object)
                    new_class_instance = new_class(master=master_object, **object["params"])
                    new_class_instance.arrange(new_class_instance.widget)
                    output_dict.update({key: new_class_instance})
        
        print(output_dict)
        return output_dict

    def class_constructor(cls, obj_dict):
        obj_type = obj_dict["obj"]

        if obj_type == "Frame":
            return Frame
        elif obj_type == "Button":
            return Button
        elif obj_type == "TextEntry":
            return TextEntry
        elif obj_type == "Label":
            return Label
        else:
            print(f'ERROR: object type {obj_type} does not exist')
            return
        
class Frame(ctk.CTkFrame):
    def __init__(self, master, row, col, padx, pady, sticky):
        super().__init__(master)
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky

    def arrange(self):
        self.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)
        self.row_index = []
        self.col_index = []

        for n in self.contain.values():
            if hasattr(n, 'row'):
                self.row_index.append(n.row)
            if hasattr(n, 'col'):
                self.col_index.append(n.col)

        self.grid_rowconfigure(tuple(set(self.row_index)), weight=1)
        self.grid_columnconfigure(tuple(set(self.col_index)), weight=1)

class Widget:
    def __init__(self, master, row, col, padx, pady, sticky, text):
        self.master = master
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.text = text

    def arrange(self, widget):
        print(f"arranging {self} at ({self.master})({self.row}, {self.col})")
        widget.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)

class Button(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text, command):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.command = command
        self.widget = ctk.CTkButton(self.master, text=self.text, command=self.command)

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkEntry(self.master, placeholder_text=self.text)

    def text_return(self):
        self.inptext = self.widget.get()
        return self.inptext

class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkLabel(self.master, text=self.text)

class App(ctk.CTk):
    def __init__(self, headtext, dimensions):
        super().__init__()

        self.headtext = headtext
        self.dimensions = dimensions

        self.title(self.headtext)
        self.geometry(self.dimensions)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def run(self, contains):
        self.contain = contains
