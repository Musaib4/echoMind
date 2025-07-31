import modules as m

# Configure your API key (replace with your own API key)
m.genai.configure(api_key="AIzaSyBG5coNlIpXBWNSuhC6CUBMKhVj5ij-pwI")

sp = m.spotipy.Spotify(auth_manager=m.SpotifyClientCredentials(
    client_id="b40c81d52d3347f7a9ad782da24e314a",
    client_secret="28323f0fc3294cfc81bcff00dbf07c0a"
))
newsapi = "e77c27defa24493db5209a2b7c86c674"

recognizer = m.sr.Recognizer()
def speak(text):
    engine = m.pyttsx3.init()
    engine.say(text)    
    engine.runAndWait()

speak("initializing musaib....")

def processCommand(c):
    if "google" in c.lower():
        m.webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "facebook" in c.lower():
        m.webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    elif "youtube" in c.lower():
        m.webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "github" in c.lower():
        m.webbrowser.open("https://github.com/")
        speak("Opening GitHub")

    elif "spotify" in c.lower():
        m.webbrowser.open("https://spotify.com")
        speak("Opening Spotify")

    elif c.lower().startswith("play"):
        song_query = c.lower().split(" ", 1)[1]

        # Search top 5 results
        results = sp.search(q=song_query, type="track", limit=5)

        if results['tracks']['items']:
            track_items = results['tracks']['items']
            track_names = [track['name'].lower() for track in track_items]

            # Use difflib to find closest match
            close_match = m.difflib.get_close_matches(song_query.lower(), track_names, n=1, cutoff=0.4)

            if close_match:
                for track in track_items:
                    if track['name'].lower() == close_match[0]:
                        song_url = track['external_urls']['spotify']
                        song_name = track['name']
                        speak(f"Playing closest match: {song_name} from Spotify")
                        m.webbrowser.open(song_url)
                        break
            else:
                speak("Couldn't find a close match. Please try again.")
        else:
            speak("Sorry, I couldn't find that song on Spotify.")

    elif "news" in c.lower():
        # Define possible news categories
        categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

        # Try to detect a category in the user's command
        selected_category = None
        for cat in categories:
            if cat in c.lower():
                selected_category = cat
                break

        # If no category found, default to general
        if not selected_category:
            selected_category = "general"

        # Add API key to URL
        url ="https://newsapi.org/v2/top-headlines?country=us&apiKey=e77c27defa24493db5209a2b7c86c674"



        try:
            r = m.requests.get(url)
            # print(f"Status Code: {r.status_code}")
            # print(f"Response: {r.text}")

            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak(f"Here are the top {selected_category} news headlines from us:")
                    for article in articles[:5]:  # Top 5 only
                        title = article.get('title', 'No title')
                        speak(title)
                else:
                    speak(f"Sorry, I couldn't find any {selected_category} news right now.")
            else:
                speak("Failed to get the news. Please try again.")
        except Exception as e:
            print("Error while fetching news:", e)
            speak("Something went wrong while fetching the news.")
    else:

        # Use the correct model name: "gemini-pro"
        model = m.genai.GenerativeModel("gemini-1.5-flash")

        # Request content
        response = model.generate_content(c)

        # Print the result
        speak(response.text)

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
            print("musaib ai error",e )