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
ow_logo = """
<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16 31.5C11.859 31.5 7.96826 29.8884 5.03994 26.9601C2.11163 24.0317 0.5 20.141 0.5 16C0.5 11.859 2.11163 7.96826 5.03994 5.03994C7.96826 2.11163 11.859 0.5 16 0.5C20.141 0.5 24.0317 2.11163 26.9601 5.03994C29.8884 7.96826 31.5 11.859 31.5 16C31.5 20.141 29.8884 24.0317 26.9601 26.9601C24.0317 29.8884 20.141 31.5 16 31.5Z" fill="#13343E" stroke="#13343E"/>
<path d="M15.9999 30.1668C12.215 30.1668 8.65914 28.6939 5.98266 26.0174C3.30619 23.3409 1.83325 19.785 1.83325 16.0002C1.83325 12.2153 3.30619 8.65938 5.98266 5.98291C8.65914 3.30643 12.215 1.8335 15.9999 1.8335C19.7848 1.8335 23.3407 3.30643 26.0172 5.98291C28.6936 8.65938 30.1666 12.2153 30.1666 16.0002C30.1666 19.785 28.6936 23.3409 26.0172 26.0174C23.3407 28.6939 19.7848 30.1668 15.9999 30.1668Z" fill="#13343E" stroke="white"/>
<path d="M22.3301 23.8985L16.3386 19.1476C16.1682 19.0123 15.9286 19.0129 15.7583 19.1476L9.78775 23.8966C9.58402 24.0587 9.28893 24.0232 9.12903 23.8174L8.28942 22.7397C8.1289 22.5339 8.16409 22.2358 8.36782 22.0743L15.2119 16.6306C15.7015 16.2408 16.3917 16.2402 16.8819 16.6294L23.7475 22.0743C23.9513 22.2358 23.9871 22.5339 23.8272 22.7397L22.9888 23.8186C22.8289 24.0244 22.5338 24.0606 22.3301 23.8991V23.8985Z" fill="#FAFAFA"/>
<path d="M8.00062 18.7496L8.00494 8L10.3009 8.00125L10.2978 14.9161L15.2145 10.9535C15.7071 10.5563 16.4066 10.5563 16.8993 10.9535L21.8184 14.9167L21.8153 8.00125L24.1113 8L24.1156 18.749C24.1156 19.1462 23.6612 19.3676 23.3538 19.12L16.3492 13.4768C16.1782 13.3389 15.9349 13.3389 15.7639 13.4768L8.76182 19.12C8.45438 19.3676 8 19.1469 8 18.7496H8.00062Z" fill="#FAFAFA"/>
</svg>
"""
st.title("💬 Ask Steve")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"],avatar=ow_logo if (msg["role"] == "assistant") else msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    history = '' #'\n'.join([f'{msg["role"]}: {msg["content"].strip()}' for msg in st.session_state.messages])
    #print(history)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = consume_url(prompt, history) #openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    #print(response)
    msg =  {"role": "assistant", "content": response['body']['message']}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg['content'])
