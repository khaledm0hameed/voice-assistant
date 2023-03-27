import speech_recognition as sr
import subprocess

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the source of input
with sr.Microphone() as source:
    print("Speak something...")
    # Listen for audio and convert it to text
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        if "open Visual Studio Code" in text:
            subprocess.run(["code"])
            print("Visual Studio Code has been opened")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")
