import random
import streamlit as st
import source_data
import time

# GUI layout
st.set_page_config(layout='wide')
st.title("Random Password Generator")

col_1, col_2, col_3, col_4 = st.columns(4)  # columns to hold sliders

# sliders
number_lower_letters = col_1.slider("Desired number of lowercase characters", min_value=0, max_value=10)
number_upper_letters = col_2.slider("Desired number of uppercase characters", min_value=0, max_value=10)
number_integers = col_3.slider("Desired number of digits", min_value=0, max_value=10)
number_characters = col_4.slider("Desired number of symbols", min_value=0, max_value=10)

# randomly select characters
pass_lower_letter = random.choices(source_data.lowercase_letters, k=number_lower_letters)
pass_upper_letters = random.choices(source_data.uppercase_letters, k=number_upper_letters)
pass_numbers = random.choices(source_data.numbers, k=number_integers)
pass_characters = random.choices(source_data.characters, k=number_characters)

# generate the password
password = pass_lower_letter + pass_upper_letters + pass_numbers + pass_characters
random.shuffle(password)
password = str().join([i for i in password])

# password output GUI
st.subheader("Your password is:")
st.info(password)

# estimate the password strength
strength_counter = 0

if number_lower_letters >= 5:
    strength_counter += 3
elif number_lower_letters >= 3:
    strength_counter += 2
elif number_lower_letters >= 2:
    strength_counter += 1
elif number_lower_letters <= 1:
    strength_counter += 0

if number_upper_letters >= 5:
    strength_counter += 3
elif number_upper_letters >= 3:
    strength_counter += 2
elif number_upper_letters >= 2:
    strength_counter += 1
elif number_upper_letters <= 1:
    strength_counter += 0

if number_integers >= 5:
    strength_counter += 3
elif number_integers >= 3:
    strength_counter += 2
elif number_integers >= 2:
    strength_counter += 1
elif number_integers <= 1:
    strength_counter += 0

if number_characters >= 5:
    strength_counter += 3
elif number_characters >= 3:
    strength_counter += 2
elif number_characters >= 2:
    strength_counter += 1
elif number_characters <= 1:
    strength_counter += 0

if strength_counter >= 8 and len(password) >= 10:
    result = "This is a strong password."
elif strength_counter >= 5 and len(password) >= 8:
    result = "This is an average password."
elif strength_counter < 6:
    result = "This is a weak password."

# show password strength estimation
if len(password) >= 1:
    st.write(result)

# download the password as a txt file
password_download_message = f"""\
Date: {time.strftime("%B %d, %Y")}, {time.strftime("%H:%M:%S")}
________________________________________________________________________________
Password:

{password}
________________________________________________________________________________\n
"""

st.download_button("Download", password_download_message,
                   help="Save the password in a text file")
