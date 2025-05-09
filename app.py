import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.write("Analyze the strength of your password based on security rules and receive feedback.")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Get user input
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password! Your password meets all security criteria.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            for suggestion in feedback:
                st.write(suggestion)
        elif 1 <= score <= 2:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for suggestion in feedback:
                st.write(suggestion)
        else:
            st.error("🚨 Very Weak Password - It is too simple and easily guessable.")
            for suggestion in feedback:
                st.write(suggestion)
