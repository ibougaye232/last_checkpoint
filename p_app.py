from chatbot import chat
from spr import google_transcriptor
from recorder import recorder2
import streamlit as st

def for_mic():


    audio=None

    #transcription
    if st.button("click to record"):
        #enregistrement du micro
        audio=recorder2()
    st.write(audio)
    #transcription en  texte
    text=google_transcriptor(audio)
    #le texte transcrit
    st.write("the transcription:", text)
    return text

def for_text():
    # Get the user's question
    question = st.text_input("You:")

    # Create a button to submit the question
    return question

def main():
    st.title("Welcome to the vocal_chatbot")
    choice2=st.selectbox("vocal or text:",["vocal","text"])
    if choice2=="vocal":
        quest=for_mic()
        if st.button("submit"):
            st.write("the response is:", chat(quest))
    else:
        quest=for_text()
        if st.button("submit"):
            st.write("the response is:", chat(quest))
main()


