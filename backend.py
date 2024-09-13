from gemini_integration import extract_info
from database import Resume, PersonalInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def process_resume_with_gemini(resume_text):
    try:
        # Extract information from the resume
        results = extract_info(resume_text)

        # Ensure the results are structured as a dictionary
        if not isinstance(results, dict):
            raise ValueError("The response from extract_info should be a dictionary.")

        return results
    except Exception as e:
        raise ValueError(f"Error processing resume with Gemini: {e}")

def save_resume(filename, resume_text, personal_info):
    try:
        # Setup the database connection
        engine = create_engine('sqlite:///resume_analyzer.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Create a new Resume entry
        resume = Resume(filename=filename, content=resume_text)
        
        # Add the resume to the session
        session.add(resume)
        session.commit()

        # Create and add PersonalInfo entry if available
        if personal_info:
            personal_info_entry = PersonalInfo(
                resume_id=resume.id,
                name=personal_info.get('name', ''),
                email=personal_info.get('email', ''),
                phone=personal_info.get('phone', ''),
                address=personal_info.get('address', '')
            )
            session.add(personal_info_entry)
            session.commit()

        # Commit and close the session
        session.close()
    except Exception as e:
        raise ValueError(f"Error saving resume: {e}")
