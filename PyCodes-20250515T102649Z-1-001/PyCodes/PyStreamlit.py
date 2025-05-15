import streamlit as st

#image
st.image(r'streamlit-png-3.jpg')

#title
st.title("Streamlit Tutorial")

#header
st.header("Deployment")

#sub-header
st.subheader("Code")

#markdown
st.markdown("Written in Python.")
st.markdown("### Written in Python.")
st.markdown("## Written in Python.")
st.markdown("# Written in Python.")

st.markdown(":moon: :man:")
st.markdown(":man: :flag-in:")

#information
st.info("This code is about deployment.")

#warning
st.warning("PSEUDO CODE")

#error
st.error("Code not executable.")

#success message
st.success("Code deployed successfully.")

#write 
st.write("Code Language")
st.write(range(50))

#text
st.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

#caption
st.caption("This is caption in streamlit.")

#maths equation
st.latex(r'(a+b)^2')

#widget
st.checkbox('check box')
st.button("click button: submit here")
st.radio('radio ', ['r1', 'r2'])
st.selectbox("select your choice: ", ['Yes', 'NO'])
st.multiselect("select multiple: ", ['selection1', 'sel2', 'sel3','sel4'])

st.select_slider("Rating Slider",['1', '2','3','4','5'])
st.slider("Slide to a number: ", 0, 10)

#number input
st.number_input("pick a number: ", 0, 10)

#text input 
st.text_input("Enter your mail id: ")

#date and time input
st.date_input("today's date: ")
st.time_input("current time: ")

# text area
st.text_area("this is your text area: type here ")

# upload file
st.file_uploader("Choose your file path: ")
st.color_picker('pick color')

#progress bar
st.progress(67)

import time 
#spinner
with st.spinner("Please Wait"):
    time.sleep(1)

#baloons
st.balloons()

#sidebar
st.sidebar.title("this is my sidebar title")
st.sidebar.text_input("this is my sidebar text input")
st.sidebar.button("submit")


# data viz via streamlit and pandas
import pandas as pd
import numpy as np

st.title("Bar Chart")
df = pd.DataFrame(np.random.randn(100,2), columns=['x','y'])
st.bar_chart(df, color=["#fd0", "#04f"])

st.title("Line Chart")
st.line_chart(df, color=["#fd0", "#04f"])

st.title("Area Chart")
st.area_chart(df,color=["#fd0", "#f0f"])


#maps
st.title("World Map")
df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"])
st.map(df2)















































