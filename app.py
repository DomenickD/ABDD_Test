"""This is a test file for the ABDD project."""

import streamlit as st

st.title("ABDD Test")

st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a write text")
st.markdown("This is a markdown text")
st.latex(r"y = \frac{a}{b}")
st.success("This is a success message")
st.warning("This is a warning message")
st.info("This is an info message")

# Add a simplec alculator
def main():
    st.title("Simple Calculator")

    # Get user input for the two numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Choose the operation from a dropdown
    operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        # Perform the calculation based on the chosen operation
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Division by zero!")
                return
        else:
            result = "Unknown operation"

        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()