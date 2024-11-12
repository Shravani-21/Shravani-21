import streamlit as st # type: ignore
import PyPDF2 # type: ignore
from PyPDF2 import PdfReader # type: ignore
import google.generativeai as genai # type: ignore

def retrieve_text_from_pdf(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    # PDF Path
    pdf = "C:\\Users\\aksha\\OneDrive\\Documents\\INNOMATICS\\Rag\\Rag.pdf"
    model = "gemini-1.5-pro-latest"
    with open(r"C:\Users\aksha\OneDrive\Documents\INNOMATICS\Rag\key.txt", "r") as file:
        key = file.read()
    genai.configure(api_key=key)
    st.title("""The RAG System""")
    question = st.text_input("Enter your question here:🤔")

    if st.button("Generate"):
        if question:
            text = retrieve_text_from_pdf(pdf)
            context = text + "\n\n" + question
            ai = genai.GenerativeModel(model_name=model)
            response = ai.generate_content(context)  
            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")
if __name__ == "__main__":
    main()