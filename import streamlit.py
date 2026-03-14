




st.title("simple cloud AI")
st.caption("Ask me absolutely anything")




system_prompt = "You are a highly intelligent,friendly,and helpful AI assistant. Answer any question the user ask clearly and accurately."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

for msg in st.session_state.maseges:
    if msg['role'] != "system":
        with st.chat_messages(msg['role']):
            st.markdown(msg['content'])

if prompt := st.chat_input("Ask me what ever you want!!!..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_messages("user"):
        st.markdown(prompt)

answer = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    massages=st.session_state.massages
).choices[0].masseges.content

st.session_state.messages.append({"role": "assistant", "content": answer})
with st.chat_massage("assistant"):
    st.markdown(answer)