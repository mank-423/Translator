from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3
import speech_recognition as sr


root = Tk()

root.title("Translate")
root.geometry("880x300")

global r 
r = sr.Recognizer()

#Functions
#translate function
def translate_it():
    #delete previous thing!!
    tr_text.delete(1.0,END)
       
    try:
        #get languages from dicitionary key
        #get the from
        for key,value in languages.items():
            if (value==og_combo.get()):
                global fr 
                fr = key
        
        
        #get to to
        for key,value in languages.items():
            if (value==tr_combo.get()):
                global to #variable declared
                to = key

        #turn original to textlblob
        global words
        words = textblob.TextBlob(og_text.get(1.0,END))
        
        #Translate tex
        words = words.translate( from_lang  = fr, to = to)

        #Output translated text
        tr_text.insert(1.0,words)

    except Exception as e:
        messagebox.showerror("Translator",e)

#text to speech function
def tts():
    #initialize speech engine
    engine= pyttsx3.init()
    #pass text
    engine.say(words)
    #run engine
    engine.runAndWait()

#clear text box
def clear():
    #Clear the text boxes
    og_text.delete(1.0,END)
    tr_text.delete(1.0,END)

#speech to text
def set_text():
    
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = "en-US")

    except:
        text = "ERROR!!"

        
    og_text.delete(1.0, END)
    og_text.insert(1.0, text)
    return


language_list = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,1,1,1,1,1,1,1,1]


#Lanaguage list from googletrans
languages  = googletrans.LANGUAGES
 
#convert to list 
language_list = list(languages.values())




#textboxes
og_text = Text(root, height = 10, width= 40)
og_text.grid(row=1, column=0, padx=20, pady=10) 

tr_text = Text(root, height = 10, width= 40)
tr_text.grid(row=1, column=2, padx=20, pady=10)

tras_button = Button(root, text = 'Translate', command = translate_it)
tras_button.grid(row=1, column=1,padx=10)

#Combobox
og_combo = ttk.Combobox(root,width=50,value = language_list)
og_combo.current(21)
og_combo.grid(row=0,column=0)

tr_combo = ttk.Combobox(root,width=50,value = language_list)
tr_combo.current(26)
tr_combo.grid(row=0,column=2)

#microphone button
mic_button= Button(root, text="mic", padx = 10, command=lambda:set_text())
mic_button.grid(row=2, column=0)

#Clear button
clear_button = Button(root,text = "Clear!", command = clear )
clear_button.grid(row=2,column=1)

#speaker button
speaker_button= Button( root, text="Speaker", command= tts)
speaker_button.grid(row=2, column=2)


#Elements of modules


##translator = Translator()

#Mirophone voice is converted to audio file
#trasnlated here here "src" keyword not needed,auto detection hai
##translated = translator.translate(text, dest="es")
##print(translated.text)



##STRUCTURE OF GUI
#box= Entry(root,borderwidth=1, width=50)
#box.grid(row=0,column=0)
#but_mic = Button(root,text = "Mic", padx = 20, pady = 20,)
#but_mic.grid(row= 1, column=0)


'''
text_speech = pyttsx3.init()    
text_speech.say(translated.text)
text_speech.runAndWait()
'''

root.mainloop()