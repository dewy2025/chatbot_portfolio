import streamlit as st
import pandas as pd

# ──────────────────────────────────────────────
# 🍽️ Diet_Bot – 식단 분석 & 상황별 맞춤 메뉴 추천
# ──────────────────────────────────────────────
st.title("🍽️ Diet_Bot – 식단 분석 & 맞춤 추천")
st.write(
    """
    🥗 **입력하신 식단을 기반으로 칼로리, 영양소 구성, 개선 조언을 제공합니다.**  
    🍚 **현재 상태(다이어트, 피로 등)와 식재료를 입력하면 건강에 적합한 메뉴를 추천해 드립니다.**
    """
)

# ──────────────────────────────────────────────
# 예시 식품 데이터베이스
# ──────────────────────────────────────────────
nutrient_db = {
    "바나나": {"칼로리": 89, "탄수화물": 23, "단백질": 1.1, "지방": 0.3},
    "계란": {"칼로리": 68, "탄수화물": 0.6, "단백질": 6.3, "지방": 4.8},
    "방울토마토": {"칼로리": 18, "탄수화물": 3.9, "단백질": 0.9, "지방": 0.2},
    "감자": {"칼로리": 77, "탄수화물": 17, "단백질": 2, "지방": 0.1},
    "두유": {"칼로리": 54, "탄수화물": 6, "단백질": 3.3, "지방": 1.8},
}

# ──────────────────────────────────────────────
# 기능 선택 메뉴 (중복 방지 key 필수)
# ──────────────────────────────────────────────
menu = st.selectbox(
    "⚙️ 기능 선택",
    ["1️⃣ 식단 공유 및 분석", "2️⃣ 상황 기반 메뉴 추천"],
    key="diet_menu_select"
)

# ──────────────────────────────────────────────
# 1️⃣ 식단 공유 및 분석
# ──────────────────────────────────────────────
if menu.startswith("1"):
    st.subheader("🥗 식단 정보 입력")

    gender = st.radio("성별을 선택하세요:", ["여성", "남성"], key="diet_gender_radio")
    age = st.number_input("나이를 입력하세요:", min_value=10, max_value=100, value=30, key="diet_age_input")
    health_conditions = st.multiselect(
        "건강 체크사항을 선택하세요:",
        ["고지혈증", "고혈압", "당뇨", "과체중"],
        key="diet_health_multiselect"
    )

    st.write("✍️ 오늘 먹은 식단을 쉼표로 구분하여 입력하세요.")
    user_input = st.text_input("예시: 바나나, 계란, 감자", key="diet_input_food")

    if st.button("📊 식단 분석하기", key="diet_analyze_button"):
        foods = [food.strip() for food in user_input.split(",")]
        total = {"칼로리": 0, "탄수화물": 0, "단백질": 0, "지방": 0}
        unknown = []

        for food in foods:
            if food in nutrient_db:
                for k in total:
                    total[k] += nutrient_db[food][k]
            else:
                unknown.append(food)

        st.write("### ✅ 식단 분석 결과")
        st.dataframe(pd.DataFrame([total]))

        if unknown:
            st.warning(f"다음 식품은 데이터베이스에 없습니다: {', '.join(unknown)}")

        # 개선 조언
        if total["지방"] > 20:
            st.info("⚠️ 지방 섭취가 많습니다. 저지방 식단을 고려해 보세요.")
        elif total["단백질"] < 20:
            st.info("💡 단백질 보충을 추천합니다. 계란, 두유 등을 고려해보세요.")
        else:
            st.success("👍 균형 잡힌 식단입니다. 잘 하셨어요!")

# ──────────────────────────────────────────────
# 2️⃣ 상황 기반 메뉴 추천
# ──────────────────────────────────────────────
elif menu.startswith("2"):
    st.subheader("🍳 상황을 알려주세요")

    condition = st.text_input("현재 컨디션 또는 상황을 입력하세요. (예: 피로, 스트레스, 운동 후)", key="diet_condition_input")
    ingredients = st.text_input("사용 가능한 식재료를 입력하세요. (쉼표로 구분)", key="diet_ingredient_input")

    if st.button("🍽️ 메뉴 추천 받기", key="diet_recommend_button"):
        available = [ing.strip() for ing in ingredients.split(",") if ing.strip()]
        
        st.write("### 📝 추천 메뉴")

        if "피로" in condition:
            st.success("🥗 추천: 두유, 계란, 바나나, 감자 - 에너지 회복과 부드러운 소화에 도움.")
        elif "스트레스" in condition:
            st.success("☕ 추천: 캐모마일티, 다크초콜릿 소량, 따뜻한 수프.")
        elif "운동" in condition:
            st.success("💪 추천: 삶은 계란, 바나나, 단백질 쉐이크.")
        else:
            st.success("🍽️ 추천: 방울토마토, 계란, 아몬드 등 가벼운 균형식이 좋아요.")

        if available:
            st.info(f"입력하신 식재료: {', '.join(available)}로 다양한 응용이 가능합니다.")
