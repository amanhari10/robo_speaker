import pyttsx3
engine = pyttsx3.init()
engine.say("WECLOME TO ROBO SPEAKER")
engine.runAndWait()
while True:
    text_to_speech = input("Type what you want me to say: ")
    engine.say(text_to_speech)
    engine.runAndWait()

    if text_to_speech == "q":
        break

