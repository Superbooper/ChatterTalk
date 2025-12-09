import pyttsx3
def speaker(words, rate, volume):
    '''
    Speaker function takes any data type in and speaks aloud
    words to speak =  bool, list, string, int, rate of speech = int, volume = double, float

    does not return any values but should cause a voice to speak the input
    '''
    #check if words are string
    if words == str:
        word_list = words.split()
        #if string continue into main code
     # if not string
    elif words != str:
        words = str(words)
        word_list = words.split()
        # make into string and continue
    else:
        #exception grab using print here because it should never ever hit this
        raise Exception("WORDS NOT IN STR OR OTHER DATA TYPES")
    #intialize speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    #read engine through list
    word_length = len(word_list)
    for i in range(0, word_length):
        try:
            word_1 = word_list[i]
            #handle a case where there are an odd number of worda
            word_2 = ''
            if i+1 < len(word_list):
                word_2 = word_list[i+1]
                engine.say(str(word_list[i]+word_list[i+1]))
                word_list.pop(i+1)
            else:
                engine.say(str(word_list[i]))
            engine.runAndWait()
        except IndexError:
            return