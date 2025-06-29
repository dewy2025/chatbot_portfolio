import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Chatbot Portfolio", page_icon="📁")  # 폴더 이모지로 변경

# --- 상단 메인 타이틀 영역 ---
st.markdown(
    """
    <div style='text-align: center; line-height: 2.2;'>
        <h1 style='color: navy; margin-bottom: 32px;'> 💻 올인원PASS AI 프로젝트</h1>
        <h2 style='margin-bottom: 32px;'>📁 Chatbot Portfolio</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 프로젝트 개요 ---
st.markdown(
    """
    <div style='text-align: center; line-height: 2.2; margin-bottom: 32px;'>
        <h4 style='color: gray; margin-bottom: 24px;'>📌 프로젝트 개요</h4>
        <p>ICT 올인원PASS! 인공지능 프로젝트 마스터 과정 실습 결과물을<br>
        한 곳에 정리한 포트폴리오입니다. 다양한 AI 챗봇과 유용한 앱을 체험해보세요!</p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 챗봇 소개(버튼+링크) ---
st.markdown("<div style='text-align: center;'><h3 style='margin-bottom:32px;'>🧩 챗봇 소개</h3></div>", unsafe_allow_html=True)
bot_info = [
    {"name": "TF_Bot", "desc": "고민 상담 또는 따뜻한 위로를 제공하는 챗봇", "url": "https://your-tf-bot-url.com"},
    {"name": "Book_Bot", "desc": "감정과 상황에 맞는 책을 추천하는 챗봇", "url": "https://your-book-bot-url.com"},
    {"name": "Image_GenBot", "desc": "원하는 주제의 AI 이미지 생성 챗봇", "url": "https://your-image-genbot-url.com"},
    {"name": "URL_ShortenBot", "desc": "긴 링크를 짧고 간편하게 변환해주는 챗봇", "url": "https://your-url-shortenbot-url.com"},
    {"name": "Diet_Bot", "desc": "식단 입력 후 칼로리·영양소 분석 및 건강 조언", "url": "https://your-diet-bot-url.com"},
]

for bot in bot_info:
    col1, col2 = st.columns([2, 6])
    with col1:
        # 버튼을 HTML로 넓게 커스텀
        button_html = f"""
        <style>
        .wide-btn {{
            width: 100%;
            padding: 0.75em 0;
            font-size: 1.1em;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            background-color: #f0f2f6;
            cursor: pointer;
            margin-bottom: 8px;
        }}
        .wide-btn:hover {{
            background-color: #e0e4ea;
        }}
        </style>
        <form action="{bot['url']}" method="get" target="_blank">
            <button class="wide-btn" type="submit">{bot['name']}</button>
        </form>
        """
        st.markdown(button_html, unsafe_allow_html=True)
    with col2:
        st.markdown(
            f"<div style='display: flex; align-items: center; height: 100%; text-align: left; font-size:1.05em;'>{bot['desc']}</div>",
            unsafe_allow_html=True
        )
st.markdown("<hr>", unsafe_allow_html=True)

# --- 하단 정보 ---
st.info("왼쪽 사이드바 메뉴 버튼을 클릭해 원하는 챗봇 또는 앱을 바로 체험해보세요!", icon="👉")

st.markdown(
    """
    <div style='text-align: center;'>
        <hr>
        <p><b>제작자:</b> Ryu MiRan</p>
        <p><b>문의:</b> mydewy2025@gmail.com</p>
    </div>
    """,
    unsafe_allow_html=True
)
