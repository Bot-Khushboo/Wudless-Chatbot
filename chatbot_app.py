import streamlit as st
from openai import OpenAI

# Secure API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# UI
st.set_page_config(page_title="Wudless Chatbot", page_icon="🤖")
st.title("🛋️ Wudless Interior Chatbot")
st.write("I'm here to collect your project details and help you get started!")

# Function to get response
def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly assistant helping customers share project details."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask anything or start sharing your project details...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_response = get_gpt_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧍‍♂️ You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
