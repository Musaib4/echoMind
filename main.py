import modules as m
from command import processCommand,speak

def main():
    while True:
        r = m.sr.Recognizer()
        print("recognizing...")
        try:
         with m.sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            speak("Got it, give me a second to think...")
            print(f"Recognized word: '{word}'")  # Debug print

            hey = "get active buddy"
            if m.difflib.get_close_matches(word.strip().lower(), [hey.lower()], n=1, cutoff=0.7):
             print("Trigger word detected!")  # Debug print
            speak("hello buddy what can i do for you")
            with m.sr.Microphone() as source:
                print("listening for command...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)
        except Exception as e:
            print("echoMind error",e )


if __name__ == "__main__":
    main()
