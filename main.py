import streamlit as st 
import config 

openai.api_key = config.API_KEY 

import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
    const stream = await openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: "Say this is a test" }],
        stream: true,
    });
    for await (const chunk of stream) {
        process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
}
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
