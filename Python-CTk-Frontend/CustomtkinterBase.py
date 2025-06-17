import customtkinter as ctk

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

    def decode_input_dict(self, inp_dict, master_object):
        output_dict = {}
        for key, object in inp_dict.items():
            if isinstance(object, dict):
                if "contains" in object:
                    container_objects = self.decode_input_dict(object["contains"], master_object)
                    new_class = self.class_constructor(object)
                    new_class_instance = new_class(master=master_object, contains=container_objects, **object["params"])
                    output_dict.update({key: new_class_instance})
                    print(vars(new_class_instance))
                else:
                    new_class = self.class_constructor(object)
                    new_class_instance = new_class(master=master_object, **object["params"])
                    output_dict.update({key: new_class_instance})
                    print(vars(new_class_instance))
        
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
    def __init__(self, master, row, col, padx, pady, sticky, contains):
        super().__init__(master)
        print("shmingus")
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.contain = contains

        self.arrange()

    def __repr__(self):
        print(f"object Frame at: {self.row}, {self.col}")

    def arrange(self):
        self.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)
        self.row_index = []
        self.col_index = []

        for n in self.contain:
            if "row" in n["params"]:
                self.row_index.append(n["params"]["row"])
            elif "col" in n["params"]:
                self.col_index.append(n["params"]["col"])

        self.grid_rowconfigure(tuple(self.row_index), weight=1)
        self.grid_columnconfigure(tuple(self.col_index), weight=1)

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
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkButton(self.master, text=self.text, command=self.button_event)
        self.arrange(self.widget)

    def button_event(self):
        print("button moment")

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkEntry(self.master, placeholder_text=self.text)
        self.arrange(self.widget)

class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkLabel(self.master, text=self.text)
        self.arrange(self.widget)

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
