import streamlit as st # for the web interface
import random  # for randomizing the questions
import time # for the timer

# Title of the Application
st.title("Quiz Applicattion")
 
# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What type of programming language is Python?",
        "options": ["Compiled", "Interpreted", "Assembly", "Machine"],
        "correct_answer": "Interpreted"
    },
    {
        "question": "Which brackets are used to define a list in Python?",
        "options": ["{}", "[]", "()", "<>"] ,
        "correct_answer": "[]"
    },
    {
        "question": "What is the correct way to declare a variable in Python?",
        "options": ["int x = 10;", "x : int = 10", "x = 10", "declare x = 10"],
        "correct_answer": "x = 10"
    },
    {
        "question": "What is the purpose of the print() function in Python?",
        "options": ["To display output on the screen", "To create a variable", "To store data", "To print a file"],
        "correct_answer": "To display output on the screen"
    },
    {
        "question": "What is the use of a for loop in Python?",
        "options": ["To check a condition", "For iteration", "To define a function", "To terminate code"],
        "correct_answer": "For iteration"
    },
    {
        "question": "What does the len() function do in Python?",
        "options": ["Finds the length of a string or list", "Runs a loop", "Performs addition", "Sorts data"],
        "correct_answer": "Finds the length of a string or list"
    },
    {
        "question": "What is the difference between == and is operators in Python?",
        "options": [
            "No difference",
            "== compares values, is compares references",
            "is compares values, == compares references",
            "Both perform the same function"
        ],
        "correct_answer": "== compares values, is compares references"
    },
    {
        "question": "What does the input() function return in Python?",
        "options": ["Integer", "String", "Boolean", "None"],
        "correct_answer": "String"
    },
    {
        "question": "What is the correct syntax for defining a dictionary in Python?",
        "options": [
            "{ 'name': 'Ali', 'age': 25 }",
            "[ 'name': 'Ali', 'age': 25 ]",
            "( 'name': 'Ali', 'age': 25 )",
            "dict('name'='Ali', 'age'=25)"
        ],
        "correct_answer": "{ 'name': 'Ali', 'age': 25 }"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["define", "function", "def", "fun"],
        "correct_answer": "def"
    }
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    
# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="correct_answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    if selected_option == question["correct_answer"]:
        st.success("✅ Corrent!")
        st.balloons()
        
    else:
       st.error(f"❌ Incorrect! The correct answer is: {question['correct_answer']} ✅")
       st.snow()

     # Wait for 3 seconds before showing the next question
    time.sleep(2)
    
     # Select a new random question
    st.session_state.current_question = random.choice(questions)
    
    # Rerun the app to display the next question    
    st.rerun()
    
    