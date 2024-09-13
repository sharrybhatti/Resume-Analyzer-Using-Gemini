import google.generativeai as genai
import os

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        # Generate content based on the prompt and question
        response = model.generate_content([prompt, question])
        return response.text
    except Exception as e:
        raise ValueError(f"Error generating content: {e}")

def extract_info(text):
    try:
        # Define prompts for each section
        prompts = {
            "education": "Extract education details from the text:",
            "work_experience": "Extract work experience details from the text:",
            "roles_responsibilities": "Extract roles and responsibilities from the text:",
            "personal_info": "Extract personal information from the text:"
        }

        results = {}
        for key, prompt in prompts.items():
            # Use the get_gemini_response function to get information for each section
            response = get_gemini_response("Please summarize:", prompt + text)
            results[key] = response or "No response"

        return results
    except Exception as e:
        raise ValueError(f"Error extracting information: {e}")

