import speech_recognition as sr
import requests
from gtts import gTTS
import playsound
import re
import os
import threading
import sys
import time

# Global flag to control the main loop
running = True

# Function to capture audio and convert to text
def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the API request.")
            return None

# Function to clean the text by removing unwanted special characters
def clean_text(text):
    # Keep only alphanumeric characters, spaces, periods, and commas
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,]', ' ', text)
    return cleaned_text

# Function to send text to the API and get a response
def send_to_api(text):
    api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    api_key = "put-your-api-key-from-google-cloud"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {"maxOutputTokens": 100}
    }

    try:
        response = requests.post(f"{api_url}?key={api_key}", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return None

# Function to convert text to speech using gTTS
def speak_text(text):
    tts = gTTS(text=text, lang='en', slow=False)
    filename = "output.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Function to listen for the 'q' key press in a separate thread
def listen_for_quit():
    global running
    while running:
        if input() == 'q':
            running = False
            print("Exiting program.")
            speak_text("Goodbye!")
            sys.exit()

def main():
    global running
    
    # Start the keyboard listener thread
    quit_thread = threading.Thread(target=listen_for_quit, daemon=True)
    quit_thread.start()

    print("Press 'q' and Enter to quit the program.")
    
    while running:
        print("Please speak now...")
        text = capture_audio()
        if text:
            cleaned_text = clean_text(text)
            print(f"Cleaned Text: {cleaned_text}")
            api_response = send_to_api(cleaned_text)
            if api_response:
                try:
                    answer = api_response['candidates'][0]['content']['parts'][0]['text']
                    answer_cleaned = clean_text(answer)
                    print(f"API Response: {answer_cleaned}")
                    speak_text(answer_cleaned)
                except KeyError:
                    speak_text("Error in API response format.")
            else:
                speak_text("Sorry, I could not get a response from the API.")
        else:
            speak_text("Sorry, I could not understand your speech.")
        
        # Wait for a short while before listening again to avoid too rapid re-execution
        time.sleep(1)

if __name__ == "__main__":
    main()
