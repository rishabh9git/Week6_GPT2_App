import streamlit as st
import openai
import os

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

# Title of the app
st.title("Rishabh's GPT-2 Interactive App")

# User input: prompt
prompt = st.text_input("Enter a prompt:")

# User input: number of tokens
max_tokens = st.number_input("Enter the number of tokens for the response:", min_value=10, max_value=500, value=100)

### OpenAI stuff
if prompt:
  response1 = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": "You are a highly creative AI."},
            {"role": "user", "content": prompt}
    ],
    max_tokens=max_tokens,
    temperature=0.9
  )

  response2 = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": "You are a highly predictable AI."},
            {"role": "user", "content": prompt}
    ],
    max_tokens=max_tokens,
    temperature=0.1
  )

### Display
st.subheader("Response 1:")
st.write(response1.choices[0].message['content'])

st.subheader("Response 2:")
st.write(response2.choices[0].message['content'])
