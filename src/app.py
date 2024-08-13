from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
import time
import random


# Initialize the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# app config
st.set_page_config(page_title="Fun bot", page_icon="🤖")
st.title("Fun bot 🤖")

# initialization of memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history= []

# Create the model
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel('gemini-1.5-pro',
                            generation_config=generation_config,
                            safety_settings=safety_settings,
                            system_instruction="You are a helpful assistant. Answer the following questions considering the history of the conversation:",
                            )
# Start the chat session
chat = model.start_chat(history= st.session_state.chat_history)

if st.button("Clear it!!"):
        st.session_state.chat_history = []
        st.rerun()

# user input
user_query = st.chat_input("What do you want to know?")
if user_query is not None and user_query != "":
    prompt = user_query.replace('\n', ' \n')
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        try:
            full_response = ""
            for chunk in chat.send_message(prompt, stream=True):
                word_count = 0
                random_int = random.randint(5,10)
                for word in chunk.text:
                    full_response+=word
                    word_count+=1
                    if word_count == random_int:
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "_")
                        word_count = 0
                        random_int = random.randint(5,10)
            message_placeholder.markdown(full_response)
        except genai.types.generation_types.BlockedPromptException as e:
            st.exception(e)
        except Exception as e:
            st.exception(e)
        st.session_state.chat_history = chat.history

# # conversation
# for message in st.session_state['chat_history']:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.markdown(message.content)

#     else:
#         with st.chat_message("AI"):
#             st.markdown(message.content)
