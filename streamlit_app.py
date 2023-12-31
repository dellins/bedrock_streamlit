import requests
import json
import streamlit as st


def consume_url(message, history):
    url = "https://y9s346bpuj.execute-api.us-east-1.amazonaws.com/default/bedrock_opensearch_demo"
    body = {
        "message": message,
        "history": history
    }
    headers = {'Content-Type': 'application/json', 'x-api-key': 'LF1LAK6AKF9Zk1gJMRWKZ5ERJ2oMraAf6V58owSt'}
    response = requests.post(url, headers=headers, data=json.dumps(body))
    
    if response.status_code == 200:
        data = response.json()

        # Process the data as needed
        print(data)

        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
ow_logo = "https://raw.githubusercontent.com/dellins/bedrock_streamlit/master/Blue_Logo.svg"
user_logo = "https://raw.githubusercontent.com/dellins/bedrock_streamlit/master/Avatar.svg"


st.title("💬 Supply Chain Assistant")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"],avatar=ow_logo if (msg["role"] == "assistant") else user_logo).write(msg["content"])

if prompt := st.chat_input():
    history = '' #'\n'.join([f'{msg["role"]}: {msg["content"].strip()}' for msg in st.session_state.messages])
    #print(history)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar=user_logo).write(prompt)
    
    response = consume_url(prompt, history) #openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    #print(response)
    msg =  {"role": "assistant", "content": response['body']['message']}
    st.session_state.messages.append(msg)
    st.chat_message("assistant", avatar=ow_logo).write(msg['content'])
