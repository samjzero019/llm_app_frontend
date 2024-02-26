"""
A simple web application to implement a chatbot. This app uses Streamlit 
for the UI and the Python requests package to talk to an API endpoint that
implements text generation and Retrieval Augmented Generation (RAG) using LLMs
and Amazon OpenSearch as the vector database.
"""
import boto3
import streamlit as st
import requests as req
from typing import List, Tuple, Dict


# global constants
STREAMLIT_SESSION_VARS: List[Tuple] = [("generated", []), ("past", []), ("input", ""), ("stored_session", [])]
HTTP_OK: int = 200


api: str = "__API_GW_ENDPOINT__"
# api: str = "https://ohyalq02l9.execute-api.us-east-1.amazonaws.com/test"


####################
# Streamlit code
####################

# Page title
st.set_page_config(page_title='Virtual assistant for knowledge base 👩‍💻', layout='wide')

# keep track of conversations by using streamlit_session
_ = [st.session_state.setdefault(k, v) for k,v in STREAMLIT_SESSION_VARS]

# Define function to get user input
def get_user_input() -> str:
    """
    Returns the text entered by the user
    """
    print(st.session_state)    
    input_text = st.text_input("You: ",
                               st.session_state["input"],
                               key="input",
                               placeholder="Ask me a question and I will consult the knowledge base to answer...", 
                               label_visibility='hidden')
    return input_text




# streamlit app layout sidebar + main panel
# and a text area for response and history
st.title("👩‍💻 Virtual assistant for a knowledge base")
st.subheader(f" Powered by :blue[` AWS Bedrock's Titan Large Model`] for text generation")

# get user input
user_input: str = get_user_input()

# based on the selected mode type call the appropriate API endpoint
if user_input:
    # headers for request and response encoding, same for both endpoints
    headers: Dict = {"accept": "application/json", "Content-Type": "application/json"}
    output: str = None     
    # ==logic ==  
    data = {"question": user_input, "verbose": True}
    resp = req.post(api, headers=headers, json=data)
    print("Response from request", resp)
    if resp.status_code != HTTP_OK:
        output = resp.text
    else:
        resp = resp.json()
        print("Response", resp)
        output = f"{resp['body']} \n"
    
    # logic 
    st.session_state.past.append(user_input)  
    st.session_state.generated.append(output) 


# download the chat history
download_str: List = []
with st.expander("Conversation", expanded=True):
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.info(st.session_state["past"][i],icon="❓") 
        st.success(st.session_state["generated"][i], icon="👩‍💻")
        download_str.append(st.session_state["past"][i])
        download_str.append(st.session_state["generated"][i])
    
    download_str = '\n'.join(download_str)
    if download_str:
        st.download_button('Download', download_str)
