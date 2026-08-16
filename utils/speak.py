import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_medicines(medicines_dict):
    if not medicines_dict:
        engine.say("Could not identify any medicine. Please try again.")
        engine.runAndWait()
        return

    names = list(medicines_dict.keys())
    if len(names) == 1:
        message = f"Detected medicine: {names[0]}"
    else:
        message = "Detected medicines: " + ", ".join(names)

    engine.say(message)
    engine.runAndWait()