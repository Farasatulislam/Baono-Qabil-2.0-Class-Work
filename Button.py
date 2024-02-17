import streamlit as st

i1 = st.button("button 1")
st.write("value:", i1)

i2 = st.checkbox("reset button")

import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

    
import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_ Sir.Ghufran Kamal_ is :blue[cool] :sunglasses:')
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# image example
import streamlit as st
from PIL import Image

# Title
st.title("Display Image Example")

# Load image
image = Image.open("images.png")

# Display image
st.image(image, caption='Example Image', use_column_width=True)


import streamlit as st

# Define functions for each page
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page_about():
    st.title("About Page")
    st.write("Welcome to the About Page!")

def page_contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page!")

# Define a function to display navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", options=["Home", "About", "Contact"])

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Contact":
        page_contact()

# Run the main function to start the app
if __name__ == "__main__":
    main()
