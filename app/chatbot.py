from gtts import gTTS
import pygame
import tempfile
import streamlit as st
import time
from openai import OpenAI
from openai import ChatCompletion
import speech_recognition as sr


recognizer = sr.Recognizer()

def text_to_speech(text):
    tts = gTTS(text)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)

    pygame.mixer.init()

    pygame.mixer.music.load(temp_audio.name)
    pygame.mixer.music.play()

    duration = pygame.mixer.Sound(temp_audio.name).get_length()

    pygame.time.wait(int(duration * 1000))
    pygame.mixer.quit()




def choose_class_subject():
    st.title("Choose Class and Subject")

st.set_page_config(
    page_title="Welcome to Shadow Teacher",
    page_icon="📚"
)

st.title("Welcome to Shadow Teacher")

if st.button("Get Started"):
    choose_class_subject()








class_label = st.subheader("Select Class:")
classes = ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
selected_class = st.selectbox("", classes)

subject_label = st.subheader("Select Subject:")
subjects = ["English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science"]
selected_subject = st.selectbox("", subjects)

if st.button("Start Chat"):
    st.text(f"Selected Class: {selected_class}")
    st.text(f"Selected Subject: {selected_subject}")








#OpenAI.api_key = ""

client = OpenAI(api_key="")

messages = [{"role": "system", "content": "You are a teacher who teaches all subjects, you are developed by the students of DLFPS for teaching dyslexic and autistic students who have a learning disability, so while answering any questions, keep in mind that there is a possibility that the user wouldn't understand your response easily, so prefer repetition and elaborating your answer using simple words. Your name is Shadow Teacher"}]

#messages = []

def send_message(user_message):
    if user_message.lower() == "quit()":
        st.stop()
    messages.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    text_to_speech(reply)

    return reply



st.title("Shadow Teacher Chatbot")

user_input = st.text_input("You:", "Type your message here")

voice_input = st.checkbox("Voice Input")


if st.button("Send"):
    if voice_input:
        with sr.Microphone() as source:
            st.write("Listening...")
            try:
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio)
                st.write(f"Voice Input: {user_input}")
            except sr.UnknownValueError:
                st.write("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                st.write(f"Could not request results from Google Web Speech API; {e}")

    response = send_message(user_input)
    st.text(f"Shadow Teacher: {response}")
    

if st.button("Quit"):
    st.stop()


    
