
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key='AIzaSyAStFRUod6oIkU5EC9wKEYTJM31r-yDomU')



def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Food recipe App")

st.header("Food recipe App")
st.write("upload the food image and you'll get the recipe :)")
input=''
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Teach me the Recipe")

input_prompt="""
You are an expert cook and you know to make every dish in the world. detect the food item from the image. then give a detailed recipie in the given format(give ingredieants and steps in bullet style:
Food recognized : <name of food> 
Origin : <nationality/region>

Ingredients needed  : 1. <ingredient one> 
                      2. <ingredient two> 
                      ....
Steps to prepare   step 1 : <step 1> 
                   step 2 : <step 2> 
                      ...

Your <food name> is ready

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Recipe is ")
    st.write(response)


