
import speech_recognition as sr
import streamlit as st

def recorder2():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("SPEAK")
            audio = r.listen(source)

        # Sauvegarde du fichier audio
        with open("record2.wav", "wb") as fichier:
            fichier.write(audio.get_wav_data())

        return "record2.wav"
    except sr.UnknownValueError:
        return "Don't understand"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"