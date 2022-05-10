#Module Import
import speech_recognition as sr
from tkinter import *
##from googletrans import Translator
##import pyttsx3
    

root = Tk()
root.title("Sample")


#Elements of modules
global r 
r = sr.Recognizer()

##translator = Translator()

#Mirophone voice is converted to audio file



    
    #trasnlated here here "src" keyword not needed,auto detection hai
##translated = translator.translate(text, dest="es")
##print(translated.text)

def set_text():
    
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = "en-US")

    except:
        text = "ERROR!!"

        
    box.delete(0,END)
    box.insert(0,text)
    return

##STRUCTURE OF GUI
box= Entry(root,borderwidth=1, width=50)
box.grid(row=0,column=0)
but_mic = Button(root,text = "Mic", padx = 20, pady = 20,command=lambda:set_text())
but_mic.grid(row= 1, column=0)


'''
text_speech = pyttsx3.init()    
text_speech.say(translated.text)
text_speech.runAndWait()
'''

root.mainloop() 