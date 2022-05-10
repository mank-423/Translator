#Import the module 
#This one is working including all other libraries at once
from tkinter import *


#Window of tkinter
root= Tk()

#TItle of the GUI
root.title("Translator")

#Functions of program

#Function1 Open new window
def opennewwin():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    my = Label(newWindow, text = "This is a new window")
    my.grid(row=0,column=0)
    my2=Label(newWindow, text = "abcd")
    my2.grid(row=1,column=0)
    my3=Label(newWindow, text = "abcd")
    my3.grid(row=2,column=0)
    my4=Label(newWindow, text = "abcd")
    my4.grid(row=3,column=0)
    my5=Label(newWindow, text = "abcd")
    my5.grid(row=4,column=0)
    my6=Label(newWindow, text = "abcd")
    my6.grid(row=5,column=0)
    my7=Label(newWindow, text = "abcd")
    my7.grid(row=6,column=0)


#Function2 texttospeech
def tts():

    import pyttsx3
    
    text_speech = pyttsx3.init()
    
    answer = input("Enter the text:")
    text_speech.say(answer)
    text_speech.runAndWait()


#Function3 Speech recogniton
def Speech():    

    #Module Import
    import speech_recognition as sr
    #Recognize the voice
    r = sr.Recognizer()
    #Mirophone voice is converted to audio file
    with sr.Microphone() as source:
        print("Speak ANything")
        audio = r.listen(source)
        
    try:
        #Converts to text for translation
        texts = r.recognize_google(audio, language = "en-US")
        
        #print("You said: {}".format(text))
    except:
        print("Sorry")
        
    

#Fucntion4 Translate 
def Translate():
  
    #importing module
    from googletrans import Translator
    
    #one variable to use library
    translator = Translator()
    
    #auto detection code 
    #for using it comment out all other lines below it
    
    #That's where the onverted text will be written
    sentence  = str(input("Say:"))
    translator = Translator()
    
    #trasnlated here here "src" keyword not needed,auto detection hai
    translated = translator.translate(sentence, dest="en")
    print(translated.text)#print this in output box

#For Entry
def set_text(texts):
    e.delete(0,END)
    e.insert(0,texts)
    return


#clear content
#def clear():
       # e.delete()
       # o.delete() 



#Elements of the GUI
label1 = Label(root,text= "Main window")
but_list = Button(root, text = "Languages", padx = 10, pady = 10, command = opennewwin)
text = Text(root, height= 1)
label2= Label(root, text="From" )
#photo = PhotoImage(file ="mic.jpg")
button1= Button(root, text="mic", padx = 5, pady = 5, command=Speech)#mic
button4= Button(root, text="Text", padx = 5, pady = 5, command=set_text)
label3= Label(root, text="To")
e = Entry(root, borderwidth=1, width=50)#idhar print karo
e.insert(0, "enter your text here")
o = Entry(root, borderwidth=1, width=50)
o.insert(0, "translated text")
button2= Button(root, text="Translate",  padx = 5, pady = 5, command=Translate )
button3=Button(root, text="Clear", padx=5, pady=5)
#label4=Label(root, text=Speech.text(#))



#Structure of GUI
label1.grid(row = 0, column = 0, columnspan=4)#main_window
but_list.grid(row = 1, column = 0, columnspan=4)#languages
text.grid(row = 2, column = 0, columnspan=4)#white_space
label2.grid(row=3, column=0 ) #from
button1.grid(row=3, column=1) #mic
label3.grid(row=5, column=0) #to
e.grid(row=4, column=0, columnspan=2)#enter_text
o.grid(row=6, column=0, columnspan=2)#translated_text
button2.grid(row=5, column=1)#translate
button3.grid(row=7, column=0)#clear
button4.grid(row = 3, column = 2)

#Loop for the GUI
root.mainloop() 