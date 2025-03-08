import streamlit as st
import random 
import string

def password_generator(length, use_digits, use_special_chars):
    characters = string.ascii_letters # includes all letters of (a-z) and (A-Z)
    if use_digits:
        characters += string.digits # Add number (0-9) to the characters
    
    if use_special_chars:
        characters += string.punctuation # Add special characters to the characters variable
        
    return "".join(random.choice(characters) for i in range(length))


st.title("Password Generator App 🖥️")

length = st.slider("Select the Length of Password", min_value=6, max_value=30, value=10)

use_digits = st.checkbox("Use Digits")
use_special_chars = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special_chars)
    st.success(f"Generated Password: {password}")