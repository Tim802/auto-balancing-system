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

class TextEntry(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkEntry(self.master, placeholder_text=self.text)
        self.arrange(self.widget)

    def input_text(self):
        self.input = self.widget.get()
        return self.input
    
class Label(Widget):
    def __init__(self, master, row, col, padx, pady, sticky, text):
        super().__init__(master, row, col, padx, pady, sticky, text)
        self.widget = ctk.CTkLabel(self.master, text=self.text)
        self.arrange(self.widget)

class App(ctk.CTk):
    def __init__(self, title, dimx, dimy, contains_row, contains_col):
        super().__init__()
        self.row_objects = contains_row
        self.col_objects = contains_col

        self.row_index_list = []
        self.col_index_list = []

        for n in self.row_objects:
            self.row_index_list.append(self.row_objects.index(n))
        for n in self.col_objects:
            self.col_index_list.append(self.col_objects.index(n))

        self.title(title)
        self.geometry(f'{dimx}x{dimy}')

        self.grid_rowconfigure(self.row_index_list, weight=1)
        self.grid_columnconfigure(self.col_index_list, weight=1)


