import streamlit as st
import rag_app

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_openai.chat_models import ChatOpenAI

st.set_page_config(
    page_title="TL;DL",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.container():
    st.title("Too long, didn't listen : Huberman for dummies")
    st.markdown(
        '<h1 style="font-size:18px"> This chat bot has been trained to answer all your questions about the following two Huberman Lab podcasts</h1>',
        unsafe_allow_html=True,
    )

with st.container():
    col1, col2 = st.columns([0.5, 0.5], gap="medium")
    with col1:
        st.image('endurance.png', caption='On Feb 1st, 2023 with Dr. Andy Galpin - duration: 3h49')
    with col2:
        st.image('nutrition.png', caption='On Feb 22, 2023 with Dr. Andy Galpin - duration: 3h05')

# session_state so that the model and the embeddings are only done once (and not everytime the button is pushed)
if "chain" not in st.session_state:
    documents = rag_app.transcript_to_document('huber_galpin.txt', size=1000, overlap=20)
    vstore = rag_app.create_vectore_store(documents)
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
    st.session_state.chain = rag_app.chat_bot_chain(vstore, model)

with st.container():
    question = st.text_input('Question about the topics covered in the podcasts')
    if st.button('Ask!'):
        st.write(rag_app.chat_bot(question, st.session_state.chain))
