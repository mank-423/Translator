def Translate():
  
    #importing module
    from googletrans import Translator
    
    #one variable to use library
    translator = Translator()
    
    #auto detection code 
    #for using it comment out all other lines below it
    '''
    text = "Hello guys" 
    text2 = "Hola gracias"
    print(translator.detect(text))
    print(translator.detect(text2))
    '''
    
    #That's where the onverted text will be written
    sentence  = str(input("Say:"))
    translator = Translator()
    
    #trasnlated here here "src" keyword not needed,auto detection hai
    translated = translator.translate(sentence, dest="en")
    print(translated.text)

Translate()