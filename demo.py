import pandas as pd
import numpy as np
import streamlit as st


st.sidebar.title("About")

st.sidebar.info(
    "This is a demo application written to help you understand Streamlit. The application identifies the animal in the picture. It was built using a standard Convolution Neural Network (CNN).")


animallist = ["image1", "image2", "image3"]
st.sidebar.selectbox("Pick an image.", animallist)
if st.sidebar.button('Predict Animal'):
	st.write('Success')


st.title('Animal Identification')
st.write("Pick an image from the left. You'll be able to view the image and get some basic statistics.")
st.write("When you're ready, submit a prediction on the left.")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
