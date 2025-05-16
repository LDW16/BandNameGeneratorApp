import streamlit as st

st.title("🎸 Band Name Generator")

st.write("Welcome to the Band Name Generator!\n")

city_grew_up = st.text_input("In what city did you grow up?")
pet_name = st.text_input("What is your pet's name?")

if city_grew_up and pet_name:
    band_name = city_grew_up + " " + pet_name
    st.success(f"Your Band Name is... **{band_name}** 🤘")