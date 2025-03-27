import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

