import streamlit as st 
from openai import OpenAI
# Chuyển khóa API cho đối tượng OpenAI client
client = OpenAI(api_key="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")

def generate_response(prompt):
    response = client.completions.create(
        model="davinci-002", 
        prompt=prompt,
        max_tokens=150,
        temperature=0.3
    )
    return response.choices[0].text

st.title("AI Chatbot: Trợ lý của AI Coding")
def get_text():
    input_text = st.text_input("User: ")
    return input_text 

user_input = get_text()
if user_input:
    st.text_area("Chatbot:", value=generate_response(user_input), height=600, max_chars=None)
else:
    st.text_area("Chatbot:", value="Xin mời nhập câu hỏi!!!", height=600, max_chars=None)
