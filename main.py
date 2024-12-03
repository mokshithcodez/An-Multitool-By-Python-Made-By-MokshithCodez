import pyttsx3
import webbrowser
import wikipedia
import time
import random
from tools import password_genarator,number_guessing_game,random_song,wikipedia_search,speak,texttospeech
from greeting import greeting

greeting()

time.sleep(2)
speak("Welcome To  My Multitool !")
while True :
    heading = '''

    1.Password_Genarator    2.Number_Guessing Game      3.Random Song

    4.Wikipedia Search Engine   5.Text To Speech   6.Exit



    '''
    print(heading)
    time.sleep(2)
    speak("Select Option")
    op = str(input("Select Any Option : ").lower())

    if op == "1" or op == "password genarator" :
        password_genarator()
        continue

    elif op == "2" or op == "number guessing game" :
        number_guessing_game()
        continue

    elif op == "3" or op == "random song" :
        random_song()
        continue

    elif op == "4" or op == "wikipedia search engine" :
        wikipedia_search()
        continue

    elif op == "5" or op == "text to speech" :
        texttospeech()
        continue

    elif op == "6" or op == "exit" :
        break

    else :
        speak("Enter Correct Choice And Enter In Integers")
        print("Enter Correct Choice And Enter In Integers")




