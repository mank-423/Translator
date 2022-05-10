
import speech_recogntion as sr

from tkinter import *

global r
r = sr.Recognizer()
global mic 
mic = sr.Microphone()


def set_text():
    with mic as source:
        audio = r.listen(source)
    text = r.recognize_google(audio, language = "en-US")
    e.delete(0,END)
    e.insert(0,text)
    return

win = Tk()

e = Entry(win,width=10)
e.pack()

a ="HENLO GUIYSS"

b1 = Button(win,text="animal",command=lambda:set_text(a))
b1.pack()

b2 = Button(win,text="plant",command=lambda:set_text("plant"))
b2.pack()

win.mainloop()


