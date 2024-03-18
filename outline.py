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

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ Ai Outline Generator"
    "</h1>",
    unsafe_allow_html=True
)

#st.title('✨ Ai Outline Generator')

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 18px;
    line-height: 0px;
    margin-top: 0;
    margin-bottom: 24px;
    text-align: center;
    display: flex;
    justify-content: center;
}
</style>
<h3 style="color: black;"> 🔥 Generate the best blog Outlines you've ever read with just a few clicks! 💥</h3>
''', unsafe_allow_html=True)

# sidebar for the user input

with st.sidebar:
    st.markdown(
        "<style>h1 {text-align: center;}</style>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<style>h1 {text-align: center; color: black;}</style>",
        unsafe_allow_html=True
    )
    st.title("Input Settings")
    
    st.markdown(
        "<style>"
        "h4 {text-align: left; color: black; margin-top: 4px;}"
        "p {text-align: left; color: black;}"
        "</style>",
        unsafe_allow_html=True
    )
    st.markdown("<h4>Enter Details for the Outlines: </h4>", unsafe_allow_html=True)
    
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
	with st.spinner("Converting desired input to prompt..."):
        	st.markdown('''
            	<style>
                .element-container .element-spinner .spinner {
                    color: #3498db;
                }
            	</style>
        	''', unsafe_allow_html=True)
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
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
        
        
        


