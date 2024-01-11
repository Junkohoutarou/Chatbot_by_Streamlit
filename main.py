import streamlit as st 
import config 
import openai

openai.api_key = config.API_KEY 

def generate_response(prompt):
    stream = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
       prompt=prompt,
        max_tokens=1024,
        temperature=0.3)
    return stream['choices'][0]['message']['content']

st.title("""
         AI Chatbot: Trợ lý của AI Coding
         Tôi sẽ trả lời mọi câu hỏi của bạn!!!
         """)

def get_text():
    input_text = st.text_input("User: ",)
    return input_text 

user_input = get_text()

if user_input:
    st.text_area("Chatbot:", value=generate_response(user_input), height=600, max_chars=None)
else:
    st.text_area("Chatbot:", value="Xin mời nhập câu hỏi!!!", height=600, max_chars=None)
