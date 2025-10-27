
import streamlit as st
from openai import OpenAI

# --- Setup ---
st.set_page_config(page_title="2-User GPT Chat", page_icon="💬", layout="centered")
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))

# --- UI ---
st.title("💬 Two User GPT Chat Interface")

# Maintain chat state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Sidebar
st.sidebar.title("🧑 Users")
user1 = st.sidebar.text_input("User 1 Name", "Alice")
user2 = st.sidebar.text_input("User 2 Name", "Bob")

# Choose active user
active_user = st.radio("Who's typing?", [user1, user2])

# Input box
user_message = st.chat_input(f"Message from {active_user}")

# --- Process Message ---
if user_message:
    st.session_state.chat.append({"role": "user", "name": active_user, "content": user_message})

    # Build conversation history for GPT
    messages = [
        {"role": "system", "content": "You are a friendly AI mediator helping two users chat smoothly."}
    ]
    for msg in st.session_state.chat:
        messages.append({
            "role": "user",
            "content": f"{msg['name']}: {msg['content']}"
        })

    # Get GPT reply
    with st.spinner("GPT is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
            )
            reply = response.choices[0].message.content
            st.session_state.chat.append({"role": "assistant", "name": "GPT", "content": reply})
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# --- Display Chat ---
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.chat_message("user").markdown(f"**{msg['name']}:** {msg['content']}")
    else:
        st.chat_message("assistant").markdown(f"**GPT:** {msg['content']}")

# Clear chat
if st.button("🗑️ Clear Chat"):
    st.session_state.chat = []
    st.rerun()
