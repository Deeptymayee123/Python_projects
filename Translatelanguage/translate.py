import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Translator",
    page_icon=":robots:",
    layout="wide"
)

st.header("Language Translator")

# Language mapping
Languages = {
    "hi": "Hindi",
    "ru": "Russian",
    "fr": "French",
    "en": "English",
    "jp": "Japanese",
    "it": "Italian",
}

source_lang, target_lang = st.columns(2)
with source_lang:
    src_lang_code = st.selectbox("Translate from", list(Languages.keys()))

with target_lang:
    tgt_lang_code = st.selectbox("Translate to", list(Languages.keys()))

# Model mapping
model_options = {
    "en-hi": "Helsinki-NLP/opus-mt-en-hi",
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",
    "en-ru": "Helsinki-NLP/opus-mt-en-ru",
    "en-jp": "Helsinki-NLP/opus-mt-en-jap",
    "en-it": "Helsinki-NLP/opus-mt-en-it",
}

model_key = f"{src_lang_code}-{tgt_lang_code}"
option_llm = model_options.get(model_key)

query = st.text_area(
    label=f"Your input text ({Languages[src_lang_code]} to {Languages[tgt_lang_code]})",
    placeholder="Enter the text to translate",
    key='question_text'
)

if st.button("Translate"):
    if not option_llm:
        st.error(f"Currently, translation from {Languages[src_lang_code]} to {Languages[tgt_lang_code]} is not supported.")
    elif query and len(query) > 1:
        try:
            with st.spinner(text="In Progress..."):
                # Initializing pipeline inside the button (Note: caching is recommended for speed)
                translator = pipeline("translation", model=option_llm)
                output = translator(query)[0]['translation_text'] 
                
            # Fixed the syntax error here
            calculated_height = min(len(output) * 2, 300) 
            
            st.text_area(
                label='Translation',
                value=output,
                height=max(calculated_height, 150),
            )
        except Exception as e:
            st.error(f"Sorry: cannot translate: {e}")
            
            
# using google translator
#pip install googletrans, we are install google trans in git bash
#from deep_translator import GoogleTranslator
#translated = GoogleTranslator(source='auto',target='tl').translate("आप कैसे हैं?")
#check api in google translater, you can get all language.
#pip install deep-translator
#print(translated)