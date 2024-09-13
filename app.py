import streamlit as st
from backend import process_resume_with_gemini, save_resume
import PyPDF2
import docx2txt
from io import BytesIO

# Function to read PDF files
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX files
def extract_text_from_docx(file):
    return docx2txt.process(file)

# Set up Streamlit app with custom configuration
st.set_page_config(page_title="Resume Analyzer", page_icon=":page_facing_up:", layout="wide")

# Title and description
st.title("Resume Analyzer")
st.write("Upload your resume and select the category you want to view. Analyze the resume and get specific details in the selected category.")

# File uploader in the sidebar
st.sidebar.header("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Choose a resume file", type=["pdf", "docx"])

# Process uploaded file
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        resume_text = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_file)

    st.write("Select the category to view:")
    category = st.selectbox("Categories", ["Education", "Work Experience", "Roles and Responsibilities", "Personal Information"])

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            try:
                # Process resume with Gemini
                results = process_resume_with_gemini(resume_text)
                
                # Ensure results is a dictionary
                if not isinstance(results, dict):
                    st.write("Error processing resume: Invalid response format")
                else:
                    # Display selected category content
                    if category == "Education":
                        st.subheader("Education Details")
                        st.write(results.get('education', 'No information found'))
                    elif category == "Work Experience":
                        st.subheader("Work Experience")
                        st.write(results.get('work_experience', 'No information found'))
                    elif category == "Roles and Responsibilities":
                        st.subheader("Roles and Responsibilities")
                        st.write(results.get('roles_responsibilities', 'No information found'))
                    elif category == "Personal Information":
                        st.subheader("Personal Information")
                        st.write(results.get('personal_info', 'No information found'))

                    # Save in database
                    personal_info = {
                        'name': results.get('personal_info', {}).get('name', ''),
                        'email': results.get('personal_info', {}).get('email', ''),
                        'phone': results.get('personal_info', {}).get('phone', ''),
                        'address': results.get('personal_info', {}).get('address', '')
                    }
                    save_resume(uploaded_file.name, resume_text, personal_info)

            except Exception as e:
                st.error(f"An error occurred: {e}")

