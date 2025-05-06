import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# prompt = "You are a helpful assistant. Keep the answers short and precise and at the end of answer ask user whether he has any questions."
prompt = """You're a friendly and helpful assistant. Only respond to questions asked in English. If someone asks in another language, say: "Oops! I can only understand and respond to questions in English." Keep your answers short and clear. End each reply by asking if they have any other questions."""



# Variables of speech-to-text - stt.py
FS = 16000  
SILENCE_THRESHOLD = 300 
SILENCE_DURATION = 3  
CHUNK_DURATION = 0.5  


