# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:12:42 2023

@author: drez_
"""
## Import libraries
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image


## uploading images
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()

##profile picture
pic_of_drez = current_dir / "drez_pic_jpg.JPG"
profile_pic = Image.open(pic_of_drez)

##other pictures





## Option to call later on ---> hides fullscreen option on image once called later on ###
hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''



### Config (Tab at top of window) ###
st.set_page_config(page_title="Drezdan Dale's Portfolio", page_icon=":chart_with_upwards_trend:", layout = "wide")



### Navbar menu at top of page ###
selected = option_menu(
            menu_title = None,  # required
            options = ["Home", "About Me", "Leadership Profile", "Leadership Journey"],  # required
            icons = ["house", "book", "envelope", ""],  # optional
            menu_icon = "cast",  # optional
            default_index = 0,  # optional
            orientation = "horizontal",
            styles = {
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#06691d"},
            },
        ) 




### Home Tab ###
if selected == "Home":
    st.markdown("<h1 style = 'text-align: center; color: #06691d;'>Welcome to my Website!</h1>", unsafe_allow_html = True)
    st.markdown("<h1 style = 'text-align: center; color: black;'>I am Drezdan Dale, and I created this website for my Leadership Capstone Class</h1>", unsafe_allow_html = True)
    col1, col2 = st.columns([2,1])
    col1.write("I am a Data Science major who loves to code, so instead of using Wix or another free tool \
             to build a website, I decided to make my own website using Streamlit in Python! \
             However, this is my first website that I have ever created, so it was definitely a learning experience. Speaking of learning experiences, throughout my \
                 time at John Carroll University, I was a Leadership Scholar."
             )
    col2.image(profile_pic, width = 667) # try --> use_column_width = True
    st.markdown(hide_img_fs, unsafe_allow_html = True)
    
    
    #### Contact Form ###
    with st.container():
        st.write("---")
        st.header("Have Questions or Want to Connect?")
        st.write("Fill out the form below to send me an email!")
        contact_form = """
        <form action="https://formsubmit.co/ddale23@jcu.edu" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Enter your name" required>
            <input type="email" name="email" placeholder="Enter your email" required>
            <textarea name="message" placeholder="Enter your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

    ### Use local CSS to edit Contact Form Style ###
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    ### Load in CSS style for Contact Form ###
    #local_css("C:/Users/drez_/Desktop/Resumes/style_css.css")
    local_css(current_dir / "style_css.css")
    




### About Me Tab ###
if selected == "About Me":
    st.title(f"You have selected {selected}")




### Leadership Profile Tab ###
if selected == "Leadership Profile":
    st.title(f"You have selected {selected}")




### Leadership Journey Tab ###
if selected == "Leadership Journey":
    st.title(f"You have selected {selected}")





























