import os
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# GEMINI PRO RESPONSE
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header = "ATS Tracking System"       
st.title("Resume Analyzer: ATS Score and JD Match Analyzer")
jd = st.text_area("Paste the Job Description", key="input")
uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="Please upload the PDF")

submit1 = st.button("Percentage Match")
submit2 = st.button("Tell me about the Resume")
input_prompt1 = """
You are a skilled ATS (Application Tracking System) scanner with a deep understanding of data science, Full Stack, Web Development. DEVOPS, Big Data Engineering, Data Analyst and deep ATS Functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage match if the resume matches the job description. First the output should come and then the keywords which are missing in the resume.
The output should come in this format.
Percentage Match: "%"
Missing Keywords: []
"""

input_prompt2 = """
You are an exprienced HR with Tech Experience in the field of any one job role from Data Science, Full Stack, Web Development. DEVOPS, Big Data Engineering, Data Analyst. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of applicant in relation to specified job role.
"""
if submit1:
    if uploaded_file is not None:
        st.success("PDF Uploaded Successfully!")
        text = input_pdf_text =(uploaded_file)
        response = get_gemini_response(input_prompt1)
        st.subheader(response)
    else:
        st.error("Upload your Resume first!")

if submit2:
    if uploaded_file is not None:
        st.success("PDF Uploaded Successfully!")
        text = input_pdf_text =(uploaded_file)
        response = get_gemini_response(input_prompt2)
        st.subheader(response)
    else:
        st.error("Upload your Resume first!")