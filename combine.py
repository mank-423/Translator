#Module Import
import speech_recognition as sr
import pyttsx3
from googletrans import Translator


#one variable to use library
translator = Translator()

#Recognize the voice
r = sr.Recognizer()

#Mirophone voice is converted to audio file
with sr.Microphone() as source:
    print("Speak ANything")
    audio = r.listen(source)
    
try:
    #Converts to text for translation
    text = r.recognize_google(audio, language = "en-US")
    print("You said: {}".format(text))
except:
    print("Sorry")
    
    

#That's where the onverted text will be written
##sentence  = str(input("Say:"))


#trasnlated here here "src" keyword not needed,auto detection hai
translated = translator.translate(text, dest="es")
print(translated.text)



text_speech = pyttsx3.init()
