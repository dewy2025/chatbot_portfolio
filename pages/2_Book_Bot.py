# 📁 Book_Bot.py 리팩토링
import streamlit as st
from openai import OpenAI

st.title("📚 BookSoul – Your Bookmate, Your Soulmate 💛")
st.write("""
당신의 감정이나 고민을 들려주면, 딱 맞는 책을 추천해드려요.
예) '지치고 무기력할 때 읽을 책', '창의력을 높여줄 책'
""")

client = OpenAI(api_key="YOUR_SECRET_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("당신의 감정이나 상황을 들려주세요."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 따뜻한 책 추천 큐레이터입니다. 책 제목, 저자, 간단한 줄거리와 추천 이유를 2~3문장으로 정리해 주세요."},
            *st.session_state.messages
        ],
        stream=True,
        temperature=1.1,
    )

    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
