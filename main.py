import streamlit as st
import pandas as pd
from googletrans import Translator
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
from langdetect import detect


genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")











