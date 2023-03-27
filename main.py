import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import predictor

HEIGHT = 500
WIDTH = 1000

data = str()
root = tk.Tk(className=' Predicting Epileptic seizure')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, )
image = ImageTk.PhotoImage(Image.open("bg2.png").resize((WIDTH, HEIGHT)))
canvas.create_image(0, 0, anchor='nw', image=image)
canvas.pack()

frame = tk.Frame(root, bg='#708090', bd=5)
frame.place(relx=0.6, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

fnamelbl = tk.Label(frame, font=40, text="")
fnamelbl.place(relwidth=0.37, relheight=1)


def xd():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image", filetype=[("csv", "*.csv")])
    basefilename = os.path.basename(filename)
    fnamelbl.configure(text=basefilename)
    button2['state'] = tk.ACTIVE


def yd():
    res = predictor.predict(filename)
    display(res)


button1 = tk.Button(frame, text="Upload", font=40, command=xd)
button1.place(relx=0.45, relheight=1, relwidth=0.2)
button2 = tk.Button(frame, text="Predict", font=40, command=yd)
button2.place(relx=0.78, relheight=1, relwidth=0.2)
button2['state'] = tk.DISABLED


# bg='#f2f542'

def display(res):
    if (res == 1):
        data = "Epilepsy detected"
    else:
        data = "No Epilepsy detected"


    label = tk.Label(root, bd=3, text=data, fg='#000000')
    label.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.4, anchor='n')
    label.config(font=("Verdana", 24))


root.mainloop()

