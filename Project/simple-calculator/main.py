import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")
    
    col1 , col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number")
        
    with col2:
        num2 = st.number_input("Enter second number")
        
    operation = st.selectbox("Select operation", ["+", "-", "x", "/"])
    
    if st.button("Calculate"):
        try:
            if operation == "+":
                result = num1 + num2
                symbol = "+"
            elif operation == "-":
                result = num1 - num2
                symbol = "-"
            elif operation == "x":
                result = num1 * num2
                symbol = "x"
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                    symbol = "/"
                else:
                    st.error("Cannot divide by zero")
                    return
            
            st.success(f"{num1} {symbol} {num2} = {result}")
            
        except Exception as e:
            st.error(f"An error accured {e}")
    
if __name__ == "__main__":
    main()
