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

# Generate responses
if st.button("Generate Response"):
    # Response with high creativity (high temperature)
    response_creative = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.8  # High creativity
    )
    st.write("Creative Response:")
    st.write(response_creative['choices'][0]['message']['content'].strip())

    # Response with low creativity (low temperature)
    response_predictable = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.2  # Low creativity, more predictable
    )
    st.write("Predictable Response:")
    st.write(response_predictable['choices'][0]['message']['content'].strip())
