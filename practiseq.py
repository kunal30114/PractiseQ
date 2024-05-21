import streamlit as st
import requests

# Define the Vext API endpoint and the necessary headers
VEXT_API_URL = "https://payload.vextapp.com/hook/PPLCQAINBH/catch/your_channel_token"
API_KEY = "70e3f1w3.oXjSmGFQj0WlPDn1fTwUgCqfwFA1Eqfk"
HEADERS = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}



def get_vext_data(topic):
    payload = {"payload": topic}
    try:
        response = requests.post(VEXT_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.ConnectionError as conn_err:
        return {"error": f"Connection error occurred: {conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        return {"error": f"Timeout error occurred: {timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"An error occurred: {req_err}"}

st.title("PRACTICE QUESTIONS")

topic = st.text_input('Enter topic')

if st.button("Enter"):
    if topic:
        with st.spinner('Fetching data ...'):
            data = get_vext_data(topic)
            if "error" in data:
                st.error(data["error"])
            else:
                questions = data.get("text", "No questions found")
                st.markdown(questions)
    else:
        st.warning("Please enter a topic.")
