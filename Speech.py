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
        text = r.recognize_google(audio, language = "en-US")
        print("You said: {}".format(text))
    except:
        print("Sorry")
        
Speech()
