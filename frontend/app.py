import streamlit as st
import requests

BACKEND_PATH = "https://country-club.onrender.com"

def main():
    st.title('Country Club')

    endpoint = st.sidebar.selectbox(
        "What do you want to get?",
        ['user','facility', 'booking']
    )
    with st.sidebar:
        limit = st.slider(
            label="Choose limit",
            min_value=5,
            max_value=50,
            value=10,
            step=5
        )

    execute_button = st.button(
        label='Retrieve data 🔎'
    )

    if execute_button:
        url = f"{BACKEND_PATH}/{endpoint}/all?limit={limit}"
        responce = requests.get(url)

        st.write(responce.json())

if __name__ == "__main__":
    main()
