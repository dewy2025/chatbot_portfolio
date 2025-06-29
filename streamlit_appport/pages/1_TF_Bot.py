# 📁 TF_Bot.py 리팩토링
import streamlit as st
from openai import OpenAI

# --- 설정 ---
st.markdown(
    "<h1 style='color:navy; font-size:2.2em; text-align:center;'>🤖 T-BOT for Advice, F-BOT for Warmth</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='font-size:1.3em; text-align:center; margin-bottom: 1.5em;'>
        고민이 있으신가요? <b>TF-Bot</b>에게 물어보세요.<br>
        <b>T-BOT</b>은 <span style='color:navy;'>이성적인 조언</span>을,<br>
        <b>F-BOT</b>은 <span style='color:crimson;'>따뜻한 위로</span>를 드려요.
    </div>
    """,
    unsafe_allow_html=True
)

client = OpenAI(api_key="YOUR_SECRET_API_KEY")  # 비밀 키 직접 코드에 숨기기 권장

# --- 챗봇 선택 ---
st.markdown(
    "<div style='font-size:1.15em; margin-bottom:0.7em; text-align:center;'><b>누구에게 말 걸고 싶으신가요?</b></div>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    bot_type = st.radio(
        "",  # 라벨은 위에서 따로 처리
        ["🧠 T-BOT", "💖 F-BOT"],
        key="bot_select",
        horizontal=True
    )

# --- 시스템 역할 ---
if "T-BOT" in bot_type:
    system_prompt = "당신은 실용적이고 논리적인 조언을 제공하는 T-BOT입니다."
else:
    system_prompt = "당신은 공감과 위로를 건네는 F-BOT입니다."

# --- 세션 초기화 ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 대화 출력 ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 사용자 입력 ---
if prompt := st.chat_input("어떤 이야기를 나누고 싶으신가요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages,
        stream=True,
        temperature=1.1,
    )

    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
