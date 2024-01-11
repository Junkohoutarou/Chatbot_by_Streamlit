import streamlit as st 
import config 
import openai 
openai.api_key = config.API_KEY 

def generate_response(prompt):
    completion = openai.Completion.create(engine="gpt-3.5-turbo-16k",
                                          prompt=prompt,
                                          max_tokens=1024,
                                          temperature=0.3) 
    message = completion.choices[0].text 
    return message 

st.title("""
         AI Chabot: Trợ lý của AI Coding
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
