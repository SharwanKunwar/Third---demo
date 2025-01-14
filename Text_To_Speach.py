import pyttsx3
import pyjokes



#get a single joke
joke = pyjokes.get_joke()

#printing joke on console
print(joke)

# Initialize the TTS engine
engine = pyttsx3.init()

# Speak a simple text
engine.say(joke)
engine.runAndWait()
