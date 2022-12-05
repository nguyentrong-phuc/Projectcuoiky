import streamlit as st
import pandas as pd
from googletrans import Translator
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
from langdetect import detect




language_code='vi_VI'
target_lang= 'ja'

    st.radio(
        "Input type",
        ["Mic", "Text", "Audio File"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        vertical=st.session_state.vẻtical,
    )

while True:
  # Recognize speech
  r = sr.Recognizer()
  with sr.Microphone() as mic:
    print('-----------------------------')
    print('listening...')
    r.adjust_for_ambient_noise(mic,duration=0.5)
    audio = r.listen(mic)
    translator = Translator()

    '''# Detect language
    #detection = translator.detect(audio)
    language_code=detect(audio)
    print('LANGUAGE CODE:', language_code)'''

  try:
    # Speech to text
    text = r.recognize_google(audio,language=language_code)
    print("You said :", text)

    # Translate
    #translator = Translator()
    translation = translator.translate(text, dest=target_lang)#  , isrc='vi'
    trans = translation.text
    print(trans)

    #convert translated text to speech
    speak = gTTS(text=trans, lang=target_lang, slow=False)
    speak.save('trans.mp3')
    playsound('trans.mp3')
    os.remove('trans.mp3')

  except sr.UnknownValueError:
    print("I could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".format(e))














