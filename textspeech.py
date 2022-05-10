def tts():


    import pyttsx3
    
    text_speech = pyttsx3.init()
    
    answer = input("Enter the text:")
    text_speech.say(answer)
    text_speech.runAndWait()

tts()