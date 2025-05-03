import streamlit as st
import hashlib
import json
from cryptography.fernet import Fernet
import os
import time
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# ==**** Data Information for User ****==
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60

# ==**** Login details ****==
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# ==**** Loading data ****==
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def generate_key(passkey):
    key = pbkdf2_hmac("sha256", passkey.encode(), SALT, 100000, dklen=32)
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 100000).hex()

# ==**** cryptography ****==
def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypt_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return None

stored_data = load_data()

# ==**** Streamlit UI ****==
st.set_page_config(page_title="Secure Data Encryption", page_icon="🔐")
st.title("🔐 Secure Data Encryption System")

st.sidebar.header("📌 Navigation Menu")
menu = ["🏠 Home", "📝 Register", "🔓 Login", "💾 Store Data", "🔍 Retrieve Data"]

if st.session_state.get("authenticated_user"):
    menu.append("🚪 Logout")

choice = st.sidebar.radio("Go to", menu)

if st.session_state.get("authenticated_user"):
    st.sidebar.success(f"👤 Logged in as: {st.session_state.authenticated_user}")

# ==**** Home Page ****==
if choice == "🏠 Home":
    st.subheader("Welcome To My Data Encryption System")
    st.markdown("""
        ✅ Store and retrieve sensitive data securely
        🔑 Encrypt with your personal passkey
        🔒 Only you can decrypt the data
        ❗ 3 wrong password attempts = Lockout for 60 seconds
        """)

# ==**** Register ****==
elif choice == "📝 Register":
    st.subheader("Register New User")
    username = st.text_input("👤 Choose a Username")
    password = st.text_input("🔐 Choose a Password", type="password")

    if st.button("✅ Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ This username already exists. Please choose another.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("🎉 Registration successful! You can now log in.")
        else:
            st.error("❗ Both fields are required.")

# ==**** Login ****==
elif choice == "🔓 Login":
    st.subheader("User Login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⏳ Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("👤 Username")
    password = st.text_input("🔐 Password", type="password")

    if st.button("🔓 Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Welcome {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid Credentials. Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("🚫 Too many failed attempts. Lockout for 60 seconds.")
                st.stop()

# ==**** Store Data ****==
elif choice == "💾 Store Data":
    if not st.session_state.get("authenticated_user"):
        st.warning("⚠️ Please register first. If you're already registered, please log in.")
    else:
        st.subheader("Store Encrypted Data")
        data = st.text_area("📝 Enter Data to Encrypt")
        passkey = st.text_input("🔑 Encryption key (passphrase)", type="password")

        if st.button("🔒 Encrypt And Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("✅ Data encrypted and saved successfully!")
            else:
                st.error("❗ All fields are required.")

# ==**** Retrieve Data ****==
elif choice == "🔍 Retrieve Data":
    if not st.session_state.get("authenticated_user"):
        st.warning("⚠️ Please register first. If you're already registered, please log in.")
    else:
        st.subheader("Retrieve Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("ℹ️ No Data Found!")
        else:
            selected_item = st.selectbox("🔐 Select an Encrypted Entry", user_data)
            passkey = st.text_input("🔑 Enter Passkey To Decrypt", type="password")

            if st.button("🔓 Decrypt Selected Entry"):
                result = decrypt_text(selected_item, passkey)
                if result:
                    st.success(f"🔓 Decrypted Text:\n{result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data.")

# ==**** Logout ****==
elif choice == "🚪 Logout":
    st.session_state.authenticated_user = None
    st.success("👋 You have been logged out successfully!")

# ==**** Footer ****==
st.markdown("---")
st.markdown("📌 **Built with ❤️ using Streamlit** | Developed by SYED SAUD ALI")
