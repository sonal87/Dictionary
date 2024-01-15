# Import Required Library
from tkinter import *
from PyDictionary import PyDictionary

# Create Objects
dictionary = PyDictionary()
root = Tk()

# Set geometry
root.geometry("1000x1000")


def dict():
	meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
	


# Add Labels, Button and Frames
Label(root, text="Dictionary", font=(
	"MADELYN 20 italic bold"), fg="teal").pack(pady=10)

# Frame 1
frame = Frame(root)
Label(frame, text="Enter Word", font=("MADELYN 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("MADELYN 15 bold"))
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font=("MADELYN 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("MADELYN 10"))
meaning.pack()
frame1.pack(pady=20)

Button(root, text="Submit", font=("MADELYN 15 bold"), command=dict).pack()

# Execute Tkinter
root.mainloop()
