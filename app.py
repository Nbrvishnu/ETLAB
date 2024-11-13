import streamlit as st
import requests
import openai

# Set your API keys
openai.api_key = "Ysk-proj-ILgJxtl-wdJshPrihQqheMky4Y87N7RdUBpKcx5B4Q2TTe7Xc4nWRYLPuNKOxSCZ9q8_mCHtMAT3BlbkFJhCPPUzCk_3AtMH_8xoZY7quCtP-TfjadaJQJLu9tH3Qya4YY0SYYDfe4sSypu_Qd9QoJgH2AAA"

# Title of the application
st.title("Online Content Generation Platform")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Generate Image", "Generate Article", "Generate Video"])

if page == "Home":
    st.write("Welcome to the Content Generation Platform!")

elif page == "Generate Image":
    st.header("Image Generation")
    prompt = st.text_input("Enter a prompt for the image")
    if st.button("Generate Image"):
        # Generate image using OpenAI's DALL-E or other APIs
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
        image_url = response['data'][0]['url']
        st.image(image_url, caption="Generated Image")

elif page == "Generate Article":
    st.header("Article Generation")
    prompt = st.text_input("Enter a topic for the article")
    if st.button("Generate Article"):
        # Generate article using GPT-3 or another text-generation API
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
        article = response.choices[0].text
        st.write(article)

elif page == "Generate Video":
    st.header("Video Generation")
    prompt = st.text_input("Enter a prompt for the video")
    if st.button("Generate Video"):
        # For demonstration purposes, use a placeholder video link
        # Integrate a video generation API if available
        st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")

# Footer
st.sidebar.write("Developed with Streamlit")
