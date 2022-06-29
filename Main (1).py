from io import StringIO
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import datetime
import time
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
loaded_model = LsaSummarizer()


def sumy_summarizer(input_text):
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    return text_summary


st.title("Text summarization Web App")
with st.sidebar:
    selectTitle = option_menu("Menu", ["Home", 'Summarize By Pasting Article','Summarize By File Upload'], 
        icons=['house', 'gear','cast'], menu_icon="cast", default_index=0)

with st.container():

    if selectTitle =='Home':
        img = Image.open('D:\DeploySourceCode\home.jpg')
        st.image(img)
    else:
        st.header(selectTitle)

    if selectTitle == 'Summarize By Pasting Article':         
         text = st.text_area('Please enter your article :', height=60)
         btnSummarize = st.button("Summarize")
         if btnSummarize:
            if text == '':
                st.write("Please enter your article for Summarization")
            else:
                summary_result = sumy_summarizer(text)
                with st.spinner('Summarize text in progress ...'):
                    time.sleep(1)
                    st.write("Result Summary :")
                    st.write(summary_result)

    if selectTitle == 'Summarize By File Upload':  
        uploaded_file = st.file_uploader("Choose a file")
        btnSummarize1 = st.button("Summarize")
        if btnSummarize1:
            if uploaded_file is not None:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))     
                summary_result = sumy_summarizer(stringio.read())
                with st.spinner('Summarize text in progress ...'):
                    time.sleep(1)
                    st.write("Result Summary :")
                    st.write(summary_result)           
         
    

