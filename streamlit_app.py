import streamlit as st
import openai
import os

st.title("Welcome to Rishabh's GPT2 App")

prompt = st.text_input("Please enter your prompt?", "Enter your prompt here")
max_tokens = st.number_input("Enter the number of tokens for the response", min_value=1, max_value=500, value=100)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
openai.api_key = my_secret_key

### OpenAI stuff
if prompt:
  response1 = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": "You are a creative assistant"},
            {"role": "user", "content": prompt}
    ],
    max_tokens=max_tokens,
    temperature=0.8
  )

  response2 = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": "You are a predictable assistant."},
            {"role": "user", "content": prompt}
    ],
    max_tokens=max_tokens,
    temperature=0.2
  )

### Display
st.subheader("Response 1:")
st.write(response1.choices[0].message['content'])

st.subheader("Response 2:")
st.write(response2.choices[0].message['content'])
