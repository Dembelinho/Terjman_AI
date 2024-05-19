from openai_langchain_tarjman import *
from streamlit_configs import *

st.markdown("""
<style>
input {
  unicode-bidi:bidi-override;
  direction: RTL;
}
</style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    initialize_session_storage()
    st.header("🇲🇦 🇲🇦 🇲🇦 AI B'DARIJA 🇲🇦 🇲🇦 🇲🇦")
    option = st.selectbox(label="Khtar l mode li bghiti",options=["Tconecta M3aya", "Tswira", "Video"])
    container=st.container(height=600, border=True)
    with container:
        read_from_session_state()
    if query := st.chat_input("merhba bik swel libghiti 🇲🇦 🇲🇦 🇲🇦?"):
        with container:
            with st.chat_message("user"):
                st.write(query)
            save_msg("user", query)
            with st.chat_message("assistant"):
                with st.spinner(""):
                    if(option=="Tconecta M3aya"):
                        response = get_darija_answer(query)[0]
                        st.write(response)
                    elif(option=="Tswira"):
                        response=get_darija_image(query)
                        st.image(response,width=500)
                save_msg("assistant", response)
        