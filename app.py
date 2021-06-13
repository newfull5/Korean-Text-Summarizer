import streamlit
import streamlit as st
from pororo import Pororo

summa = Pororo(task='text_summarization', lang='ko')


def summaizer(text):
    global summa
    output = summa(text)
    return output


def write_header():
    st.title('Korean Text Summarizer')
    st.markdown('''
        - Paste any article in the text area below and click on the 'Summarize!' button to get the summarized textual data.  
        - This application is using KakaoBrais' Pororo library for text summarization.
    ''')


def write_textbox():
    input_text = st.text_area(label='Paste your copied text here...', key=1, height=200)
    button = st.button(label='Summarize!')

    if button:
        with st.spinner(text='This may take a moment...'):
            output = summaizer(input_text)
        st.text_area(label='Summary:', key=2, height=200, value=output)

    else:
        st.text_area(label='', key=2, height=200)


if __name__ == '__main__':
    st.set_page_config(page_title='English-HindUrdu Translator', page_icon='☮️', layout='wide')
    write_header()
    write_textbox()
