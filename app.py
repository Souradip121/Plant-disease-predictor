import streamlit as st
from PIL import Image
import openai
import base64
import requests
import io

# Set up the OpenAI API key
api_key = ""

# Function to encode the image to base64
def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to get the plant disease diagnosis
def get_disease_diagnosis(image):
    base64_image = encode_image(image)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "You are a plant disease diagnosis AI. You will diagnose the disease of the plant leaf in the image. Analyze the image and provide the diagnosis. And tell me what I should do to treat the disease. Also mention the medicine and dosage. IF YOU CANT DIAGNOSE THE DISEASE DONT PROVIDE ANY CURE OR SUGGESTIONS "},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

# Streamlit app
st.title("Plant Disease Diagnosis")
st.write("Upload an image of a plant leaf to get a disease diagnosis.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("Analyzing the image...")
    
    # Get diagnosis from GPT API
    diagnosis = get_disease_diagnosis(image)
    
    st.write("Diagnosis:")
    st.write(diagnosis)
