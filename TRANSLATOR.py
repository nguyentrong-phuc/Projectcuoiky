from googletrans import Translator
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import streamlit as st
from pydub import AudioSegment
import time
import pydub
from pathlib import Path
from typing import List
import pandas as pd
from io import StringIO
st.title('Auto_Translator App')
IPtype = st.radio("Input Type",('Microphone', 'Text', 'Audio File'),horizontal=True)

Lang=['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani', 'Bambara', 'Basque', 'Belarusian', 'Bengali', 'Bhojpuri', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dhivehi', 'Dogri', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Filipino (Tagalog)', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Guarani', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Ilocano', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Konkani', 'Korean', 'Krio', 'Kurdish', 'Kurdish (Sorani)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lingala', 'Lithuanian', 'Luganda', 'Luxembourgish', 'Macedonian', 'Maithili', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Meiteilon (Manipuri)', 'Mizo', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Nyanja (Chichewa)', 'Odia (Oriya)', 'Oromo', 'Pashto', 'Persian', 'Polish', 'Portuguese (Portugal, Brazil)', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Sanskrit', 'Scots Gaelic', 'Sepedi', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala (Sinhalese)', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog (Filipino)', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tigrinya', 'Tsonga', 'Turkish', 'Turkmen', 'Twi (Akan)', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
Code=['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'zh', 'zh', 'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mni-Mtei', 'lus', 'mn', 'my', 'ne', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

if IPtype == 'Text':
    col1,col3 = st.columns(2)
    with col1:
        option1 = st.selectbox("Your Language",Lang)
        in_text = st.text_area("Enter text:",height=8,max_chars=None,key=None,help="Enter your text here")
        button = st.button('Translate')
    with col3:
        option3 = st.selectbox("Target Language",Lang)
    Yourlang = Code[Lang.index(option1)]
    Targlang = Code[Lang.index(option3)]

    with col3:
        if button:
                translator = Translator()
                translation = translator.translate(in_text, dest=Targlang)
                trans = translation.text
                st.text_area('Translated', trans, height=8, max_chars=None, key=None)
                speak = gTTS(text=trans, lang=Targlang, slow=False)
                time.sleep(0.5)
                speak.save('trans.mp3')
                time.sleep(0.5)
                playsound('trans.mp3')
                time.sleep(0.5)
                os.remove("trans.mp3")

if IPtype == 'Microphone':
    col1,col3 = st.columns(2)
    with col1:
        option1 = st.selectbox("Your Language",Lang)
    with col3:
        option3 = st.selectbox("Target Language",Lang)
    Yourlang = Code[Lang.index(option1)]
    Targlang = Code[Lang.index(option3)]

    button=st.button('START')
    if button :
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.5)
            audio = r.listen(mic)
        try:
            text = r.recognize_google(audio, language=Yourlang)
            translator = Translator()
            translation = translator.translate(text, dest=Targlang)
            trans = translation.text
            col1, col2 = st.columns(2)
            with col1:
                st.text_area('Text recoded', trans, height=8, max_chars=None, key=None)
            with col2:
                st.text_area('Translated', trans, height=8, max_chars=None, key=None)
            #text to speech
            speak = gTTS(text=trans, lang=Targlang, slow=False)
            speak.save('trans.mp3')
            playsound('trans.mp3')
            os.remove("trans.mp3")
        except sr.UnknownValueError:
            st.write("Cannot receive your voice")
        except sr.RequestError as e:
            st.write("Could not request results from Speech Recognition service; {0}".format(e))

if IPtype == 'Audio File':
    col1,col3 = st.columns(2)
    with col1:
        option1 = st.selectbox("Your Language",Lang)
    with col3:
        option3 = st.selectbox("Target Language",Lang)
    butt1=st.button('Translate')
    Yourlang = Code[Lang.index(option1)]
    Targlang = Code[Lang.index(option3)]

    uploaded_file = st.file_uploader("upload", type=['wav'],accept_multiple_files=False)
    if butt1:
        if uploaded_file is not None:
            audio_bytes = uploaded_file.read()
            st.audio(audio_bytes, format='audio / wav')
        #speech to text
        file_name = uploaded_file.name
        v = sr.Recognizer()
        with sr.AudioFile(uploaded_file.name) as source:
            audio_data = v.record(source)
        in_text = v.recognize_google(audio_data,language=Yourlang)
        #translate
        translator = Translator()
        translation = translator.translate(in_text, dest=Targlang)
        trans = translation.text
        # write
        col1, col2 = st.columns(2)
        with col1:
            st.write('File to text')
            st.success(in_text)
        with col2:
            st.write('Translated')
            st.success(trans)

