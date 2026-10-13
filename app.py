import streamlit as st
from rag_query import retrieve_and_answer

st.set_page_config(page_title="AD/AT Personal Codex", page_icon="🧑‍💻")
st.title("🧑‍💻 AD/AT Personal Codex")
st.caption("Runs 100% locally. No cloud. No API keys.")

# Simple chat history (optional)
if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(msg)

# New: send on Enter
q = st.chat_input("Ask a question")  # pressing Enter submits

if q and q.strip():
    st.session_state.history.append(("user", q.strip()))
    with st.spinner("Thinking..."):
        ans = retrieve_and_answer(q.strip())
    st.session_state.history.append(("assistant", ans))
    st.markdown(ans)

st.divider()
