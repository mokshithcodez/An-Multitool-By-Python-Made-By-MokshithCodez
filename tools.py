import pyttsx3
import random
import webbrowser
import pandas
from songs import songslist
import wikipedia

engine = pyttsx3.init()

def speak(text) :
    
    engine.say(text)
    engine.runAndWait()


def password_genarator() :
    chars = ["A","B","C","D","E","F","I","J","K","L","M","N","O","P","Q","R","S","2","1@","#","5"]


    a = random.choice(chars)
    b = random.choice(chars)
    c = random.choice(chars)
    d = random.choice(chars)
    e = random.choice(chars)
    f = random.choice(chars)

    abc = a+b+c+d+e+f

    print("Here Is Genarated Password  : ",abc)
    speak("Here Is Genarated Password")



def random_song():
    speak("Playing Random Song !")
    songsks = random.choice(songslist)
    webbrowser.open(songsks)


def wikipedia_search() :
    speak("What You Wanna Search")
    search_field = str(input("What You Wanna Search :"))
    
    
    output_field = wikipedia.summary(search_field)
    print(output_field)
    speak(output_field)

    


def number_guessing_game() :
    print("Hmm Wait I am Selecting")
    speak("Hmm Wait I am Selecting")

    print("done")
    speak('done')
    speak("Now GUess My Number")

    orginial = random.randint(0,200)
    while True :
        user_guess = int(input("Your Guess : "))

        if user_guess > orginial :
            speak("Too High")
            print("Too High")

        elif user_guess < orginial :
            speak("Too Low")
            print("Too Low")

        else : 
            speak("You Gussed It Right Yay")
            print("you Guessing It !")
            break



def texttospeech() :
    speak("Enter Your Text")
    iop = str(input("Your Text : "))
    print(iop)
    speak(iop)
    engine.save_to_file(iop,"speech.mp3")
    engine.runAndWait()













    
   









    

    
    

   







    


        





    

