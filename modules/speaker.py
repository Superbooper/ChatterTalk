import pyttsx3
def spearker(words):
    #check if words are string
    if words == str:
        word_list = words.split
        #if string continue into main code
     # if not string
    elif words != str:
        words = str(words)
        word_list = words.split
        # make into string and continue
    else:
        #exception grab
        print("WORDS NOT IN STR OR OTHER DATA TYPES")
        exit
    #intialize speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    
    #read engine through list
    #finish