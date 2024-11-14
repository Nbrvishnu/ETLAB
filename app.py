from openai import images
import streamlit as st
from transformers import pipeline
from PIL import Image  # Replace with an image library of your choice
from cv2 import VideoCapture  # Replace with a video library of your choice

api_key = st.secrets["openai"]["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"]

st.title("Content Generation Hub")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Generate Image", "Generate Article", "Generate Video"])

if page == "Home":
    st.write("Welcome to the Content Generation Hub!")

elif page == "Generate Image":
    st.header("Image Generation")
    prompt = st.text_input("Enter a prompt for the image")
    if st.button("Generate Image"):
        image = images(prompt)
        st.image(image, caption="Generated Image")

elif page == "Generate Article":
    st.header("Article Generation")
    prompt = st.text_input("Enter a topic for the article")
    if st.button("Generate Article"):
        generator = pipeline('text-generation')
        article = generator(prompt, max_length=500, num_return_sequences=1)[0]["generated_text"]
        st.write(article)

elif page == "Generate Video":
    st.header("Video Generation")
    prompt = st.text_input("Enter a prompt for the video")
    if st.button("Generate Video"):
        video = VideoCapture(prompt)
        st.video(video)

st.sidebar.write("Developed with Streamlit")
