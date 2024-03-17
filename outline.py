## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)


# Navbar
st.set_page_config(
    page_title="Blog Outline",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# title of our app
st.title('✍️ Farhan BlogGPT')

# create a subheader
st.subheader("AI Blog Outlines Generator 🤖")

# sidebar for the user input

with st.sidebar:
    st.title("Input Settings")
    st.subheader("Enter Details for the Outlines")
    
    # Blog Title
    blog_title = st.text_input("Blog Title ")

    # Primary Keyword
    primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
            f"""
            Please ignore all previous instructions. Using the MECE Framework Develop a comprehensive English markdown outline for a long-form article for the topic {blog_title}, featuring at least 20 engaging headings and subheadings that are detailed, mutually exclusive, collectively exhaustive and cover the entire topic. Conclude with a conclusion heading and pertinent FAQs.
            
            Follow these instructions:
     
            1. Keep in mind these are the Primary Keyword "{primary_keyword}" and Secondary Keyword "{secondary_keyword}" we are trying to rank for so include it and variations of these keywords in the H2,H3 and throughout the article aviode from keyword stuffing only incorported 2 times each keyword in h2 and h3.
            2. Create an indept blog post outlines with every single question or topic a person would have for this blog post topic. 
            3.Include information specific to topic you are writing about but also general information about the blog post topic that would be useful for readers.
            4. Write in a simple, easy to read tone. 
            5. We are trying to rank for the Primary Keyword "{primary_keyword}" , Secondary Keyword "{secondary_keyword}" and  so follow all seo practices to do so.
            6. Use a conversational tone using simple language, avoiding jargon and complex terms.
            7. Please be natural, write like a human.
            8. Headlines are more likely to be clicked on in search results if they have about 6 words.
            9. Headlines that are lists and how-to get more engagement on average than other types of headlines.
            10. Headline will be more compelling and attract more clicks if you add more emotional and power words.
	        11. 20 engaging headings and subheadings 
	        12. Strictly say that Secondary keyowrd also add in h3 and h4 only one time.
	        13. Only incorpoted the primary keyword 2 times in outlines. This strict order follow it.
		    14. Identify the key sections of the article and create H3 headings for each section that are both descriptive and engaging. 
		    15. Use H4 subheadings as needed to break down each section into smaller, more specific topics.
            """
    ]

    # Submit Button
    submit_button = st.button("Generate")

    # Clear All Button
    clear_button = st.button("Clear All")

if submit_button:
    # Display the spinner
        # Generate the response
        response = model.generate_content(prompt_parts)

        # Display the blog output
        st.write(response.text)



 # Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer" style="background-color: #333; padding: 10px; display: flex; justify-content: center; align-items: center; width: 100%;">
    <p style="font-size: 14px; font-style: italic; color: #fff; margin-bottom: 0px; opacity: 0.9; line-height: 1.2; display: flex; align-items: center; justify-content: center;">Developed by: <span style="font-size: 16px; font-weight: 500; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span></p>
    <div style="display: flex; align-items: center;">
        <a href="https://www.linkedin.com/in/farhan-akbar-ai/" style="margin: 0px 5px;"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="height: 20px; width: auto; background-color: #333;"/></a>
        <a href="mailto:rasolehri@gmail.com" style="margin: 0px 5px;"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email&logoColor=white" alt="Email" style="height: 20px; width: auto; background-color: #333;"/></a>
    </div>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
        
        
        


