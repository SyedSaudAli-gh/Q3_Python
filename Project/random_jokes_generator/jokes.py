import streamlit as st
import requests


def get_random_joke():
    """Fetch a random joke from the Joke API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
        
    except:
        return "Why did the programmer quit his job? \n Because he didn't get arrays!"
    
    
def main():
    st.title("Random Jokes Generator (English)")
    st.write("Click the button below to generate a random joke")
    
    if st.button("Generate Jokes for English"):
        joke = get_random_joke()
        st.success(joke)
        
        
def get_pakistani_joke():
    """Fetch a random Pakistani joke from the Joke API"""
    try:
        response = requests.get("https://jokes-fast-api.vercel.app/pakistani_joke")
        
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        
    except:
        return "After that, the program continued, it ended.? \n The program was hit!"
        
        
def main_pakistani():
    st.title("Random Jokes Generator (Pakistani)")
    st.write("Click the button below to generate a random Pakistani joke")
    
    if st.button("Generate Jokes for Pakistani"):
        joke = get_pakistani_joke()
        st.success(joke)
        
        
    st.divider()
    
    st.markdown(
        """
        <div style= "text-align: center;">
            <p>Joke from Official joke API & custom API from FastAPI</p>
            <p>Built with ❤️ by <a href="https://github.com/SyedSaudAli-gh">Syed Saud Ali</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
        
        
        
        
        
if __name__ == "__main__":
    main()
    main_pakistani()
        
        
        
    
        