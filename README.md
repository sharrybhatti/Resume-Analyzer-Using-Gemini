🎓 Resume Analyzer with Gemini 

Welcome to the Resume Analyzer project! This application leverages the power of Google Gemini API to provide detailed analysis and insights from resume documents. Whether you’re a recruiter or a job seeker, this tool helps you extract and organize important resume information effortlessly.
🚀 Features

    Upload and Analyze: Seamlessly upload PDF or DOCX resumes and extract key information.
    Detailed Insights: Get insights on education, work experience, roles, responsibilities, and personal information.
    Database Storage: Save extracted data to an SQLite database for future reference.
    Creative UI: Enjoy an interactive and user-friendly interface built with Streamlit.

📜 Table of Contents

    Installation
    File Descriptions
    Usage
    Troubleshooting
    Contributing
    License

Installation
1. Clone the Repository

bash

git clone https://github.com/sharybhatti/resume-analyzer.git
cd resume-analyzer

2. Set Up a Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Required Packages

bash

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the root directory and add your Google Gemini API key:

makefile

GOOGLE_API_KEY=your_google_api_key

📂 File Descriptions
database.py

Contains the SQLAlchemy database models and setup for the SQLite database. Defines tables for:

    Resume
    PersonalInfo
    Education
    WorkExperience
    RolesResponsibilities

backend.py

Handles resume processing and interaction with the Google Gemini API. Key functions:

    process_resume_with_gemini(): Extracts resume sections using Gemini API.
    save_resume(): Stores resume data and extracted information in the database.

app.py

Provides a Streamlit-based user interface for:

    Uploading resumes
    Viewing extracted information by category (Education, Work Experience, etc.)
    Handling errors and displaying results

gemini_integration.py

Manages API integration with Google Gemini:

    Configures API access
    Retrieves and formats responses from Gemini API

💻 Usage
Running the Streamlit Application

bash

streamlit run app.py

Open the URL provided by Streamlit to access the web interface.
Upload and Analyze

    Upload a Resume: Choose a PDF or DOCX file through the file uploader.
    Select a Category: Choose from Education, Work Experience, Roles and Responsibilities, or Personal Information.
    Click "Analyze Resume": View the extracted information for the selected category.

🛠️ Troubleshooting

    FileNotFoundError: Ensure the file path is correct.
    API Errors: Check your API key and refer to the Google Gemini API documentation.

🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes. Adhere to the code style and include tests where applicable.
