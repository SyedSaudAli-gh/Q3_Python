import  streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)
st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting money...! 💸")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You made ${amount}! 💰")
    
# Fetching Side Hustles API
def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apikey=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"] 
        else:
            return ("No side hustle idea!")
    except:
        return ("Something went wrong")
    
    
st.subheader("Side Hustles Ideas")
if st.button("Generate Hustle Idea!"):
    idea = fetch_side_hustles()
    st.success(idea)
    
    
# Fetching Money Quote API
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?apikey=1234567890")
        if response.status_code == 200:
            money_quote = response.json()
            return money_quote["money_quote"]
        else:
            return ("Money is the root of all evil!")
    except:
        return("Something went wrong")
    
    
st.subheader("Money Making Motivation")
if st.button("Generate Money Quote!"):
    quote = fetch_money_quote()
    st.info(quote)