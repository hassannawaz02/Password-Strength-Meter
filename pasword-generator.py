import streamlit as st
import random
import string

# --- Password Generation Logic ---
def password_generator(length, use_digits, use_special):
    characters = string.ascii_letters  # a-zA-Z

    if use_digits:
        characters += string.digits     # 0-9

    if use_special:
        characters += string.punctuation  # !@#$%^&*() etc.

    if not characters:
        return "❌ Please select at least one character set"

    return ''.join(random.choice(characters) for _ in range(length))

# --- Streamlit UI ---
st.set_page_config(page_title="Password Generator 🔐", page_icon="🔐")

st.markdown("## 🔐 Friendly Password Generator")
st.write("✨ Create strong passwords with just a few clicks!")

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    length = st.slider("🔢 Password Length", min_value=6, max_value=32, value=12)
with col2:
    st.markdown("### Options")
    use_digits = st.checkbox("🔢 Use Numbers (e.g., 123)")
    use_special = st.checkbox("🔣 Use Special Characters (e.g., @#$%)")

# --- Generate Button ---
if st.button("🎲 Generate Password"):
    password = password_generator(length, use_digits, use_special)
    
    if "❌" in password:
        st.warning(password)
    else:
        st.success("🎉 Here's your secure password:")
        st.code(password, language="")

st.markdown("---")
st.markdown("<div style='text-align: center;'>👨‍💻 Made with ❤️ by <strong>Hassan Nawaz</strong></div>", unsafe_allow_html=True)
