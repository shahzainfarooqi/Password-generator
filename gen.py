import streamlit as st
import random
import string


st.title("🔐 Password Generator")


st.sidebar.title("⚙️ Settings")


length = st.sidebar.slider("Password length", min_value=4, max_value=50, value=12)
include_uppercase = st.sidebar.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_numbers = st.sidebar.checkbox("Include Numbers (0-9)", value=True)
include_symbols = st.sidebar.checkbox("Include Symbols (!@#$%)", value=True)


if st.button("🚀 Generate Password"):
    characters = list(string.ascii_lowercase)

    if include_uppercase:
        characters += list(string.ascii_uppercase)
    if include_numbers:
        characters += list(string.digits)
    if include_symbols:
        characters += list(string.punctuation)

    if not characters:
        st.error("⚠️ You must select at least one character type!")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success("🔑 Your Generated Password:")
        st.code(password, language="text")


st.markdown("---")
st.caption("Made with ❤️ using Streamlit")