import serial
import customtkinter
import time

port = 'COM5'
baud = 115200

arduino = serial.Serial(port, baud, timeout=.1)
app = customtkinter.CTk()
app.title("Shmingus")
app.geometry("400x150")

def button_event():
    print("Button moment")

button = customtkinter.CTkButton(app, text='CTkButton', command=button_event)
button.grid(row=0,column=0,padx=20,pady=20)

def write_loop(inp):
    byteinp = inp.to_bytes()
    print(byteinp)
    arduino.write(byteinp)

def slider_event(val):
    inpval = round(val)
    print(inpval)
    write_loop(inpval)

slider = customtkinter.CTkSlider(app, from_=0, to=180, command=slider_event)
slider.grid(row=1, column=0,padx=20,pady=20)




app.mainloop()