import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

myLabel = Label(text="I am a Label", font=("Arial", 24, "bold"))
myLabel.pack()

myLabel["text"] = "New Text"
myLabel.config(text="New Text")

#Button

def buttonClicked():
    print("I got clicked")
    newText = input.get()
    myLabel.config(text=newText)

button = Button(text="Click me", command=buttonClicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
print(input.get())




window.mainloop()
