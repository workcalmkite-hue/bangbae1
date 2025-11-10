import streamlit as st
from datetime import date

st.title("📘 방과후 수업 후기 기록")
st.caption("오늘 진행한 방과후 수업을 간단하게 정리해두는 공간이에요.")

# 📝 방과후 수업 후기 입력 폼
with st.form("after_school_review"):
    col1, col2 = st.columns(2)

    with col1:
        review_date = st.date_input("날짜", value=date.today())
        program_name = st.text_input("프로그램명", placeholder="예: 3D 프린팅 방과후, 코딩 기초반")

    with col2:
        target_class = st.text_input("대상 학년/반", placeholder="예: 1학년 전체, 2-3반")
        session_no = st.text_input("차시 (선택)", placeholder="예: 3/12차시")

    st.markdown("### ✨ 오늘 수업 한 줄 요약")
    one_line = st.text_input(
        "오늘 수업을 한 줄로 표현해보면?",
        placeholder="예: 아이들이 처음으로 3D 프린터를 직접 만져본 날!"
    )

    st.markdown("### 🔍 수업 돌아보기")

    col3, col4 = st.columns(2)

    with col3:
        good_points = st.text_area(
            "👍 잘된 점",
            placeholder="계획대로 잘 흘러간 부분, 학생들이 적극적으로 참여한 활동 등"
        )
        student_reaction = st.text_area(
            "😊 학생 반응 / 인상깊었던 장면",
            height=120,
            placeholder="아이들 반응, 기억에 남는 한마디, 웃겼던 상황 등"
        )

    with col4:
        bad_points = st.text_area(
            "👀 아쉬운 점 / 예상 밖 상황",
            height=120,
            placeholder="시간 부족, 준비물 문제, 난이도 조절 등"
        )
        next_time_idea = st.text_area(
            "🔁 다음 시간에 이렇게 해보고 싶다",
            height=120,
            placeholder="활동 순서 조정, 설명 방식 바꾸기, 난이도 조절 아이디어 등"
        )

    mood = st.slider("오늘 나의 컨디션 / 만족도", 1, 10, 7)

    submitted = st.form_submit_button("✏️ 후기 정리하기")

# ✅ 제출 후 정리해서 보여주기
if submitted:
    st.success("후기가 아래에 정리되었어요. 복사해서 다른 문서에 붙여넣어도 좋아요 😊")

    st.markdown("---")
    st.markdown("### 📄 정리된 후기")

    session_no_display = session_no if session_no.strip() != "" else "-"

    review_md = f"""
**날짜**: {review_date.strftime('%Y-%m-%d')}
**프로그램명**: {program_name if program_name else "-"}
**대상 학년/반**: {target_class if target_class else "-"}
**차시**: {session_no_display}
**오늘 한 줄 요약**: {one_line if one_line else "-"}

---

#### 👍 잘된 점
{good_points if good_points else "-"}

#### 😊 학생 반응 / 인상깊은 장면
{student_reaction if student_reaction else "-"}

#### 👀 아쉬운 점 / 예상 밖 상황
{bad_points if bad_points else "-"}

#### 🔁 다음 시간에 이렇게 해보고 싶다
{next_time_idea if next_time_idea else "-"}

#### 😌 오늘 나의 컨디션 / 만족도
{mood} / 10
"""

    # 마크다운 형태로 보여주기 (그대로 복붙용)
    st.code(review_md, language="markdown")

    # txt 파일로 다운로드
    st.download_button(
        "📥 이 후기를 .txt 파일로 다운로드",
        data=review_md.encode("utf-8"),
        file_name=f"방과후후기_{review_date.strftime('%Y%m%d')}.txt",
        mime="text/plain",
    )
