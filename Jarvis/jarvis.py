import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

def speak(text):
    
    print(f"Jarvis: {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)  # Bolne ki speed
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Speech error: {e}")

def listen():
    """convert the voice into a text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        print("i didn't hear you, say it again")
        return ""

# Main Program
if __name__ == "__main__":
    speak("Hello! I am Jarvis. How can I help you today?")
    
    while True:
        query = listen()

        if not query:
            continue

        # 1. Time.
        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        # 2. Google 
        elif 'open google' in query or 'google' in query:
            speak("Opening Google")
            time.sleep(1)  # Jarvis ko bolne ka waqt dene ke liye
            webbrowser.open("https://www.google.com")

        # 3. YouTube
        elif 'open youtube' in query or 'youtube' in query:
            speak("Opening YouTube")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com")

        # 4. Program end here
        elif any(word in query for word in ['bye', 'buy', 'by', 'exit', 'stop', 'quit']):
            speak("Goodbye! Have a nice day.")
            time.sleep(1)
            break