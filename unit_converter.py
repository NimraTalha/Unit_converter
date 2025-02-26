import streamlit as st

# Conversion data
conversion_rates = {
    "Kilometers to Miles": 0.621371,
    "Miles to Kilometers": 1.60934,
    "Kilograms to Pounds": 2.20462,
    "Pounds to Kilograms": 0.453592,
    "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
    "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
}

# Streamlit UI
st.title("Unit Converter")

# Dropdown for unit selection
conversion_type = st.selectbox("Select Conversion", list(conversion_rates.keys()))

# Input field for user value
input_value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# Perform conversion
if st.button("Convert"):
    conversion = conversion_rates[conversion_type]
    result = conversion(input_value) if callable(conversion) else input_value * conversion
    
    st.success(f"Converted Value: {result:.4f}")

