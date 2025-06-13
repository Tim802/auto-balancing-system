import serial
import time
import customtkinter as tkinter

class SliderFrame(tkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        self.title = title
        self.title = tkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky='ew')

        #instantiate sliders here
        self.slider1 = Slider(1,0,0,180,self)
        self.slider2 = Slider(2,0,0,180,self)
        self.slider3 = Slider(3,0,0,180,self)

    def slider_event_print(self):
        print(
            f"Cont1: {self.slider1.val}, {self.slider1.byte}\nCont2: {self.slider2.val}, {self.slider2.byte}\nCont3: {self.slider3.val}, {self.slider3.byte}\n"
        )

class Slider(SliderFrame):
    def __init__(self, row, col, min, max, parentframe):
        self.row = row
        self.col = col
        self.min = min
        self.max = max
        self.frame = parentframe
        self.val = 90
        self.byte = self.val.to_bytes()
        self.slider = tkinter.CTkSlider(self.frame, from_=self.min, to=self.max, command=self.slider_event)
        self.slider.grid(row=self.row, column=self.col, padx=20, pady=20)

    def slider_event(self, val):
        #round val to int
        inpval = round(val)
        self.val = inpval
        #convert val to byte
        byteinp = self.val.to_bytes()
        self.byte = byteinp
        self.frame.slider_event_print()

class App(tkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Shmingus')
        self.geometry('400x220')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.slider_frame = SliderFrame(self, 'Servo Angles')
        self.slider_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

#initialise the app
app = App()
app.mainloop()