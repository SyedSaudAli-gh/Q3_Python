import streamlit as st
import string

# store password in a session State list
if "password_stored" not in st.session_state:
    st.session_state.password_stored = []
    
# This function to check password strength
def password_strength(password):
    has_digit = any(char.isdigit() for char in password)
    has_special_charecter = any(char in string.punctuation for char in password)
    
    if len(password) < 8:
        return "🤏🏻 Week"
    elif len(password) < 12 or not (has_digit and has_special_charecter):
        return "☝🏻 Medium"
    return "💪🏻 Storng"


st.title("Password Strength Meter 🛡️")

# password input field
password = st.text_input("Enter Your Password", type="password")


# Check password strength button
if st.button("Check Strength"):
    if password:
        if password in st.session_state.password_stored:
            st.warning("This password is already used! Please try another one.")
        else:
            strength = password_strength(password)
            st.session_state.password_stored.append(password)
            st.success(f"Password Strength: {strength}")
    else:
        st.error("Please Enter a Password")
    
# Display stored passwords
st.subheader("Stored Passwords")
if st.session_state.password_stored:
    for pw in st.session_state.password_stored:
        st.write(f"🔑 {pw}")
        
else:
    st.warning("No Passwords Stored Yet!")
