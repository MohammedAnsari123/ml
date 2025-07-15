import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
import pickle as pkl


try:
    with open("model.pkl", "rb") as f:
        model = pkl.load(f)
except FileNotFoundError:
    st.error("model.pkl not found. Please upload the file or check your repository.")



st.sidebar.title("Side Bar")
option = st.sidebar.radio("Analysis", ["Home","Analysis","Visualization","Prediction"])

def home():
    genai.configure(api_key = "AIzaSyD-Iyz1os4Mz3m93k9X7yRFXYPN1BsUHuA")
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = st.text_input("Ask Gemini Something: ")
    button = st.button("Click me")
    if button:
        response = model.generate_content(prompt)
        st.write(response.text)


    # abc = st.text_input("Enter Name: ")
    # if abc:
    #     st.write(f"Hello {abc}")


    # shravani = st.number_input("Enter age: ",1)
    # if shravani:
    #     st.write(f"your age is {shravani}")

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.markdown("Column 1")
    # with col2:
    #     st.markdown("Column 2")
    # with col3:
    #     st.markdown("Column 3")




def analysis():
    file = st.file_uploader("Choose a file", type = ["csv"])
    c = st.button('Analyse')

    if c:
        if file:
            df = pd.read_csv(file)
        else:
            df = pd.read_csv("feeds.csv")
        # st.markdown(df)
        st.write(df)
        st.write(df.describe())


def visualization():
    file = st.file_uploader("Choose a file", type = ["csv"])
    if file:
        df = pd.read_csv(file)
        st.write(df.columns)
        i = st.selectbox(
            'selext', df.columns
            )
        fig, ax = plt.subplots()
        ax.plot(df[i])
        st.pyplot(fig)

        # plt.plot(df[i])
        # plt.show()
        # st.pyplot()

    # # c = st.button('Visualization')
    # # if c:
    # if file:
    #     df = pd.read_csv(file)
    #     st.write(df.columns)
    #         # choice = st.text_input("select One column: ")
    #         # st.write(df[choice])
    # else:
    #     df = pd.read_csv("feeds.csv")
    #     st.write(df.columns)
    #         # choice = st.text_input("select One column: ")
    #         # st.write(df[choice])

    #     cho = st.text_input("select One column: ")
    #     b = st.button("clicke to visualiz")
    #     if b:
    #         st.write(df[cho])
    #         print(cho)



def prediction():
    year = st.number_input("Year: ")
    state = st.number_input("State: ")
    total = st.number_input("Total: ")
    TminusU = st.number_input("T minus U: ")
    type = st.number_input("type: ")
    user_input = [[year, state, total, TminusU, type]]
    b = st.button("Predict")

    if b:
        st.write(model.predict(user_input))

    # st.write(dt.predict(user_input))


if option == "Home":
    home()
elif option == "Analysis":
    analysis()
elif option == "Visualization":
    visualization()
elif option == "Prediction":
    prediction()






