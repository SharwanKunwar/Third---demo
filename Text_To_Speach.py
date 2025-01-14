import pyttsx3
import pyjokes

#Author: Sharwan jung kuwnar
#Purpose: To create a program which can print joke and tell



#get a single joke
joke = pyjokes.get_joke()

#printing joke on console
print(joke)

# Initialize the TTS engine
engine = pyttsx3.init()

# Speak a simple text
engine.say(joke)
engine.runAndWait()
