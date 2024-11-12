from openai import OpenAI
import streamlit as st

f=open(r"C:\Users\aksha\OneDrive\Documents\INNOMATICS\backened_sessions\GENAI_APPS\genai_app1\keys\openai_key.txt")
key=f.read()
client=OpenAI(api_key=key)

st.title("Python code Debugger🐍")
st.subheader("Review your Python Code")

prompt=st.text_area("Enter python code",height=200)

if st.button("Generate")==True:
    st.balloons()
    response=client.chat.completions.create( model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "Fix bugs and suggest improvements for the Python code"},
                {"role": "user", "content": prompt}
            ]
        )
    st.write(response.choices[0].message.content)