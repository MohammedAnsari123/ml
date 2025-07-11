import streamlit as st

st.title("Web Site")

st.header("Shravani")

st.subheader("subheader")

st.write("Write This")
st.write("<h1>"" HELLO ""</h1>")

a = st.checkbox("Attendence")
st.checkbox("Student")
st.checkbox("Marks")

if a:
    st.write("You Attended the Event")

st.slider("Audio", 1, 100 ,100)


st.sidebar.title("Sidebar Title")
st.sidebar.button("Click me")
st.sidebar.selectbox("Choose option", ["Option 1", "Option 2"])

b = st.sidebar.radio("Chose Your Language", options = ["Python", "HTML", "CSS"])
if b == "Python":
    st.write("Welcome to Python")
    st.code("print('Hello')", language = "python")

st.selectbox("Choose option", ["Blue", "Red", "Yellow", "Pink"])

st.text(9)
st.markdown(9)
st.write(9)

st.write

st.html("Rane")

st.button("button")

st.hello

abc = st.text_input("Enter Name: ")
if abc:
    st.write(f"Hello {abc}")


shravani = st.number_input("Enter age: ",1)
if shravani:
    st.write(f"your age is {shravani}")
