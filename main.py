import streamlit as st
from embedchain import App

import os

# Initialize the EmbedChain app
app = App()

# Add the student handbook link to the EmbedChain app
handbook_link = "https://www.addu.edu.ph/wp-content/uploads/2022/12/Ateneo-Student-Handbook-2019.pdf"
app.add(handbook_link)

api_key = os.environ["OPENAI_API_KEY"]

# Streamlit app
def main():
    st.set_page_config(page_title="QKnight", page_icon="🔷", layout="wide")

    # Application Introduction
    st.title(" 🔷 QKnight 🔷 : Explore the Ateneo Student Handbook!")

    # Introduction Text
    st.markdown("""
    <style>
    .big-font {
        font-size:25px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:20px !important;
    }
    .small-font {
        font-size:16px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Welcome to QKnight, your AI-powered assistant for navigating the Ateneo de Davao University Student Handbook!</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sample Questions Section
    st.markdown('**Sample Questions You Can Ask:**', unsafe_allow_html=True)
    st.markdown('<ul class="small-font">'
                '<li>What grade do I need to maintain to keep my scholarship?</li>'
                '<li>How can I apply for a leave of absence?</li>'
                '<li>What are the requirements to graduate?</li>'
                '</ul>', unsafe_allow_html=True)
    st.markdown("---")
    # Enhanced Text box for the query with styling
    st.write('**Type your query here:**', unsafe_allow_html=True)
    query = st.text_input("", help="Enter search terms to find relevant information in the handbook.")
    
    if st.button("Submit", help="Click to search"):
        # Execute the query and store the response
        response = app.query(query)
        # Display the response
        if response:
            st.success("Response:")
            st.write(response)
        else:
            st.error("No response found for the query.")

    # Adding a footer
    st.markdown("---")  # Adds a horizontal line to separate the main content from the footer
    st.markdown("""
    <style>
    .footer {
        font-size:14px;
        text-align: center;
        color: gray;
    }
    </style>
    <div class="footer">
        <p>QKnight is independently operated and is not officially affiliated with the Ateneo de Davao University. It represents a personal project undertaken by a student and, as such, it is strongly advise for users to verify the accuracy and reliability of the content provided, as it may occasionally output misleading information. </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
