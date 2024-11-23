import streamlit as st

st.title("GPA Calculator for PSG TECH")

num_courses = st.number_input("Enter the number of subjects:", min_value=0, step=1)

grades = []
credits = []

st.subheader("Enter grade points and credits for each course:")
for i in range(int(num_courses)):
    grade = st.number_input(f"Grade Points for Course {i + 1}:", min_value=0, max_value=10, step=1, key=f"grade_{i}")
    credit = st.number_input(f"Credit Hours for Course {i + 1}:", min_value=0, step=1, key=f"credit_{i}")
    grades.append(grade)
    credits.append(credit)
    

if st.button("Calculate GPA"):
    try:
        total_credits = sum(credits)
        weighted_sum = sum(grade * credit for grade, credit in zip(grades, credits))
        gpa = weighted_sum / total_credits if total_credits > 0 else 0
        st.write(f"Total Credits: {total_credits}")
        st.success(f"Your GPA is: {gpa:.2f}")
        
    except Exception as e:
        st.error("Something went wrong. Please check your inputs.")
