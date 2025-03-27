import streamlit as st
import openai

# Set your API key here
openai.api_key = "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"

st.set_page_config(page_title="Wudless Chatbot", page_icon="🤖")

st.title("🛋️ Wudless Interior Chatbot")
st.write("I'm here to collect your project details and help you get started!")

# Function to send messages to GPT
def get_gpt_response(prompt):
    messages = [{"role": "system", "content": "You are a friendly assistant helping customers share project details."},
                {"role": "user", "content": prompt}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response['choices'][0]['message']['content']

# Chat interaction
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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
