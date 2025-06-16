import customtkinter as ctk

class Object_Creator:
    def __init__(self, master, row, col, padx, pady, sticky, contains_row, contains_col):
        self.master = master
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.sticky = sticky
        self.row_objects = contains_row
        self.col_objects = contains_col

        self.arrange()
        self.instance(self.row_objects)
        self.instance(self.col_objects)

    def arrange(self):

        self.row_index_list = []
        self.col_index_list = []

        for n in self.row_objects:
            self.row_index_list.append(self.row_objects.index(n))
        for n in self.col_objects:
            self.col_index_list.append(self.col_objects.index(n))

        self.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady, sticky=self.sticky)
        self.grid_rowconfigure(self.row_index_list, weight=1)
        self.grid_columnconfigure(self.col_index_list, weight=1)

    def instance(self, obj_list):
        #obj_list will be a list of tuples of the form (title, object)
        for i in obj_list:
            self.i[0] = i[1]