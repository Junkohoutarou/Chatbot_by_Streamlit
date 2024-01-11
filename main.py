import openai 
import streamlit as st 
import config 

openai.api_key = config.API_KEY 

def generate_response(prompt):
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=1024,
                                          temperature=0.3) 
    message = completion.choices[0].text 
    return message 

st.title("""
         AI Chabot: Trợ lý của AI Coding
         Em sẽ trả lời mọi câu hỏi của anh!!!
         """)

def get_text():
    input_text = st.text_input("Ông chủ: ",)
    return input_text 

user_input = get_text()

if user_input:
    st.text_area("Cô hầu:", value=generate_response(user_input), height=600, max_chars=None)
else:
    st.text_area("Cô hầu:", value="Xin mời ông chủ nhập vào!!!", height=600, max_chars=None)