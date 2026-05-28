from openai import OpenAI

from  dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1"
)

def analyse_patient(patient, appointment):
    prompt = f"""
    Analyze this patient .
    name :{patient['name']}
    oxygen : {patient['oxygen']}
    BP : {patient['BP']}
    tempertuer: {patient['temperature']}
    appointment doctor:
    {appointment['Doctor']}
    give: 
    1. urgency level
    2. recommedation
    """
    
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role":"user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


