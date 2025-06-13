import serial
import time
import customtkinter as tkinter

port = 'COM5'
baud = 115200

#arduino = serial.Serial(port, baud, timeout=.1)
app = tkinter.CTk()
app.title("Shmingus")
app.geometry("400x150")

class Slider:
    def __init__(self, row, col, min, max):
        self.row = row
        self.col = col
        self.min = min
        self.max = max
        self.slider = tkinter.CTkSlider(app, from_=self.min, to=self.max, command=self.slider_event)
        self.slider.grid(row=self.row, column=self.col, padx=20, pady=20)

    def slider_event(self, val):
        #round val to int
        inpval = round(val)
        #convert val to byte
        byteinp = inpval.to_bytes()
        self.val = inpval
        self.byte = byteinp

#init the slider controls
Slider1 = Slider(0,0,0,180)
Slider2 = Slider(1,0,0,180)
Slider3 = Slider(2,0,0,180)
#run main loop of app
app.mainloop()