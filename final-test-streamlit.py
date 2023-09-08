import streamlit as st

data = {}

st.set_page_config(
    page_title="Mean-Calculator🐟",
    layout="wide"
)

st.title("Student Degree Mean Calculator 📊")

subject = st.text_input("Enter Subject Name 📝:")
degrees_input = st.text_input(f"Enter {subject} Degrees (comma-separated) 🎯:")

if st.button("Add Subject 🚀") and subject and degrees_input:
    degrees = [float(x.strip()) for x in degrees_input.split(",") if x.strip()]
    data[subject] = degrees
    st.success(f"Added {subject} with degrees: {', '.join(map(str, degrees))} 🎉")

st.divider()

if data:
    st.header("Subjects and Mean Degrees 📈:")
    for subject, degrees in data.items():
        mean = sum(degrees) / len(degrees)
        st.write(f"- {subject}: {mean:.2f}")

st.sidebar.info("Don't forget to add more subjects! 👆")
st.markdown("Made by 🐟Mohamed Naeem🐟") 
