# import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak_medicines(medicines_dict):
#     if not medicines_dict:
#         engine.say("Could not identify any medicine. Please try again.")
#         engine.runAndWait()
#         return

#     names = list(medicines_dict.keys())
#     if len(names) == 1:
#         message = f"Detected medicine: {names[0]}"
#     else:
#         message = "Detected medicines: " + ", ".join(names)

#     engine.say(message)
#     engine.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice.id, "-", voice.name)



import os
import pyttsx3

def build_message(medicines_dict):
    if not medicines_dict:
        return "Could not identify any medicine. Please try again."
    names = list(medicines_dict.keys())
    if len(names) == 1:
        return f"Detected medicine: {names[0]}"
    return "Detected medicines: " + ", ".join(names)

def speak_online(message):
    from gtts import gTTS
    from playsound import playsound
    tts = gTTS(text=message, lang='en', tld='co.in')
    tts.save("output.mp3")
    try:
        playsound("output.mp3")
    finally:
        os.remove("output.mp3")

def speak_offline(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(message)
    engine.runAndWait()

def speak_medicines(medicines_dict):
    message = build_message(medicines_dict)
    try:
        speak_online(message)
    except Exception:
        speak_offline(message)