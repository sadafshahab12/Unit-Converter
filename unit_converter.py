import streamlit as st

def convert_unit(value , from_unit , to_unit):
    conversions= {
        # Length
        "Meters to Feet": value * 3.28084,
        "Feet to Meters": value / 3.28084,
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value / 0.621371,

        # Weight
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value / 2.20462,

        # Temperature
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9,

        # Time
        "Hours to Minutes": value * 60,
        "Minutes to Hours": value / 60,
        "Minutes to Seconds": value * 60,
        "Seconds to Minutes": value / 60,
    }
    return conversions.get(f"{from_unit} to {to_unit}", "Invalid Conversion")
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter")
st.write("Convert length, weight, temperature, and time easily!")

categories = {
    "Length" : ["Meters", "Feet", "Kilometers", "Miles"],
    "Weight": ["Kilograms", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Time": ["Hours", "Minutes", "Seconds"]
}

category = st.selectbox("Select Category:", list(categories.keys()))

from_unit = st.selectbox("Convert From:" , categories[category])
to_unit = st.selectbox("Convert To:" , [u for u in categories[category] if u != from_unit])

value = st.number_input("Enter Value:" , min_value=0.0 , format="%.2f")

if st.button("Convert"):
    result = convert_unit(value , from_unit, to_unit)

    if isinstance(result, (int , float)):
        st.success(f"{value:.2f}{from_unit} = {result:.2f}{to_unit}")
    else:
        st.error("Conversion not supported") 
st.write("💡 Tip: Select a category first to see available units!")