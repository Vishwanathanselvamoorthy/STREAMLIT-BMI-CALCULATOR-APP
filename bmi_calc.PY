import streamlit as st

def calculate_bmi(height, weight):
    # BMI formula: weight (kg) / (height (m))^2
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Streamlit UI
st.title("BMI Calculator")

# User input for height and weight
height = st.number_input("Enter your height (cm):", min_value=1, value=170)
weight = st.number_input("Enter your weight (kg):", min_value=1, value=70)

# Calculate BMI
bmi = calculate_bmi(height, weight)

# Classify BMI into health categories
health_category = classify_bmi(bmi)

# Display results
st.write(f"Your BMI is: {bmi:.2f}")
st.write(f"Health Category: {health_category}")
