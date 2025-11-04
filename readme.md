 # Voice-Controlled AI Assistant named as echoMind

A command-line Python Voice Assistant that can:
Speak with you using text-to-speech
Play music on Spotify
Fetch real-time news
Open websites
Chat using Google's Gemini AI
🎙️ Just speak — your assistant listens, thinks, and responds like a pro.


## 🚀 Features
✅ Speech Recognition – Understands voice commands
✅ Text-to-Speech – Speaks responses using pyttsx3
✅ Spotify Integration – Plays songs using the Spotify API
✅ News Headlines – Fetches top news using News API
✅ AI Chat (Gemini) – Connects to Google Gemini for intelligent responses
✅ Custom Commands – Extend with your own logic in command.py



## 📦 Voice Assistant
├── main.py              # Main driver script
├── modules.py           # Handles API logic (news, Spotify, etc.)
├── command.py           # Parses and executes commands
├── requirements.txt     # All dependencies
├── .env                 # API keys and secrets
├── .venv/               # Python virtual environment
├── __pycache__/         # Auto-generated
└── README.md            # This file



## **Built With**
- Python
- SpeechRecognition
- pyttsx3
- Spotipy
- Google Generative AI (Gemini)
- News API
- dotenv

## 📦 Installation

Follow these steps to set up the assistant on your system:

### 1. Clone the Repository

   ~~~bash
git clone https://github.com/Musaib4/echoMind.git
cd echoMind 


### 2. create and activate an virtual env.
python -m venv .venv
# For Windows:
.venv\Scripts\activate
# For macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

### add api keys
GOOGLE_API_KEY=your_google_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
NEWS_API_KEY=your_news_api_key

#  run the project

python main.py

~~~
## 📝 License
This project is open source under the [MIT License](LICENSE).

# 👤 Author
Musaib Khursheed
B.Sc. IT Student | Developer | Problem Solver
 LinkedIn | GitHub | Portfolio

# personal portfolio: https://musaibmisger.sbs