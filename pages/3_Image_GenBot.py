import streamlit as st
from openai import OpenAI
import requests

st.title("🖼️ AI 이미지 생성기")
st.write("텍스트를 입력하면, 해당 내용을 바탕으로 이미지를 생성합니다.")

# 사용 방법 안내
with st.expander("ℹ️ 사용 방법 보기", expanded=True):
    st.markdown("""
    1. **왼쪽 사이드 바에 OpenAI API키를 입력하세요.**
    2. **생성하기 원하는 이미지 프롬프트를 입력하세요.**
    3. **원하는 이미지 스타일과 크기를 선택한 후 생성하기 버튼을 눌러주세요.**
    """)

st.sidebar.title("🔑 설정")
openai_api_key = st.sidebar.text_input("OpenAI API 키 입력", type="password")

if not openai_api_key:
    st.sidebar.warning("OpenAI API 키를 입력하세요.")
    st.stop()

# OpenAI 클라이언트 설정
client = OpenAI(api_key=openai_api_key)
# 사용자 입력
prompt = st.text_input("📝 이미지 설명을 입력하세요", value="A cute dog")  
# 스타일 선택과 사이즈 선택을 같은 행에 배치
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox(
        "🎨 이미지 스타일",
        (
            "자동", "사진", "디즈니 스타일", "픽사 3D 스타일", "유화", "고흐 스타일", 
            "픽토그램", "연필 스 드로잉", "아트포스터", "미니멀리즘", 
            "앤디워홀", "구스타프 클림트", "무하", "헤이즐 블룸", 
            "리얼", "만화", "수채화"
        )
    )
with col2:
    # 비율로 이미지 크기 선택
    ratio = st.selectbox(
        "🖼️ 이미지 비율",
        ("정사각형 (1:1)", "세로 (9:16)", "가로 (16:9)"),
        index=0  # 기본값 1:1
    )

# 비율에 따라 OpenAI 지원 사이즈로 변환
ratio_to_size = {
    "정사각형 (1:1)": "1024x1024",
    "세로 (9:16)": "1024x1792",
    "가로 (16:9)": "1792x1024"
}
size = ratio_to_size[ratio]

# 스타일에 따라 프롬프트에 스타일 정보 추가
style_dict = {
    "자동": "",
    "사진": "in a photo style",
    "디즈니 스타일": "in a disney style",
    "픽사 3D 스타일": "in a pixar 3d style",
    "유화": "as an oil painting",
    "고흐 스타일": "in the style of Vincent van Gogh",
    "픽토그램": "as a pictogram",
    "연필 스 드로잉": "as a pencil sketch drawing",
    "아트포스터": "as an art poster",
    "미니멀리즘": "in a minimalism style",
    "앤디워홀": "in the style of Andy Warhol",
    "구스타프 클림트": "in the style of Gustav Klimt",
    "무하": "in the style of Alphonse Mucha",
    "헤이즐 블룸": "in the style of Hazel Bloom",
    "리얼": "in a realistic style",
    "만화": "in a cartoon style",
    "수채화": "in a watercolor painting style"
}
styled_prompt = f"{prompt}, {style_dict[style]}" if style_dict[style] else prompt

# 이미지 생성 버튼
if st.button("이미지 생성하기"):
    with st.spinner("이미지를 생성 중입니다..."):
        try:
            # 첫 번째 이미지 생성
            response1 = client.images.generate(
                prompt=styled_prompt,
                model="dall-e-3",
                size=size,
                n=1
            )
            image_url1 = response1.data[0].url

            # 두 번째 이미지 생성
            response2 = client.images.generate(
                prompt=styled_prompt,
                model="dall-e-3",
                size=size,
                n=1
            )
            image_url2 = response2.data[0].url

            # 사진 2장을 같은 행에 나란히 보여주기
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(image_url1, caption="생성된 이미지1", use_column_width=True)
                st.write(f"**프롬프트:** {styled_prompt}")
                st.download_button(
                    label="이미지1 다운로드",
                    data=requests.get(image_url1).content,
                    file_name="image1.png",
                    mime="image/png"
                )
            with img_col2:
                st.image(image_url2, caption="생성된 이미지2", use_column_width=True)
                st.write(f"**프롬프트:** {styled_prompt}")
                st.download_button(
                    label="이미지2 다운로드",
                    data=requests.get(image_url2).content,
                    file_name="image2.png",
                    mime="image/png"
                )
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {e}")