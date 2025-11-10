import streamlit as st
from datetime import date

st.title("🗓️ 오늘의 한 줄 기록")

st.caption("하루를 짧게 남겨요. 기록은 마음의 근육이 됩니다 💭")

with st.form("daily_log"):
    today = st.date_input("날짜", value=date.today())
    mood = st.select_slider("오늘 기분", ["😢", "😐", "😊", "🤩"])
    note = st.text_area("한 줄 기록", placeholder="오늘 있었던 일을 한 줄로 써봐요!")
    submitted = st.form_submit_button("기록하기")

if submitted:
    st.success("기록 완료!")
    st.write(f"📅 **{today.strftime('%Y-%m-%d')}** | {mood}")
    st.info(note)
