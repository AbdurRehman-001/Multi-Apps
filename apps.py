import streamlit as st


st.title("Temperature Converter")

# Dropdown for selecting the unit to convert from
temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
from_unit = st.selectbox("Select the unit you want to convert from", temp_units)

# Input for temperature value
temperature = st.number_input(f"Enter temperature in {from_unit}", value=0.0)

# Dropdown for selecting the unit to convert to
to_unit = st.selectbox("Select the unit you want to convert to", temp_units)

# Function to convert temperatures
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (temp * 9/5) + 32
        elif to_unit == "Kelvin":
            return temp + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (temp - 32) * 5/9
        elif to_unit == "Kelvin":
            return (temp - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return temp - 273.15
        elif to_unit == "Fahrenheit":
            return (temp - 273.15) * 9/5 + 32

# Conversion and output
if temperature:
    converted_temp = convert_temperature(temperature, from_unit, to_unit)
    st.write(f"{temperature} {from_unit} is equal to {converted_temp} {to_unit}.")

from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Title of the app
st.title("Age Calculator")

# Description of the app
st.write("""
This is a simple app to calculate your age based on the date of birth.
Please select your birthdate and the app will calculate your current age.
""")

# Input for the user's birthdate with a broader range
min_date = datetime(1900, 1, 1)  # Set to the minimum year you want to allow
max_date = datetime.today()  # Allow selecting any date up to today

birth_date = st.date_input("Select your birthdate:", min_value=min_date, max_value=max_date)

# If birthdate is selected, calculate age
if birth_date:
    age = calculate_age(birth_date)
    st.write(f"Your age is {age} years old.")

Exchange rates (as an example, these values are for demonstration and should be updated regularly)
exchange_rates = {
    "GBP": 0.0051,  # PKR to GBP
    "USD": 0.0055,  # PKR to USD
    "CNY": 0.038,   # PKR to CNY
    "INR": 0.44     # PKR to INR
}

# Title of the app
st.title("Currency Converter - PKR to Other Currencies")

# User input for amount in PKR
pkr_amount = st.number_input("Enter amount in Pakistani Rupees (PKR):", min_value=0.0)

# Dropdown for selecting the target currency
currency = st.selectbox(
    "Select target currency:",
    ("GBP", "USD", "CNY", "INR")
)

# Conversion logic
if pkr_amount > 0:
    # Get the exchange rate for the selected currency
    exchange_rate = exchange_rates[currency]
    
    # Convert the amount
    converted_amount = pkr_amount * exchange_rate
    
    # Display the result
    st.write(f"{pkr_amount} PKR is equal to {converted_amount:.2f} {currency}")
else:
    st.write("Please enter a valid amount in PKR.")




