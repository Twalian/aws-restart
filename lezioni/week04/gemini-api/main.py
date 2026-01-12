from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

response = client.models.generate_content_stream(model="gemini-3-flash-preview", contents="Quante richieste posso farti senza avere un piano a pagamento?")

print(response.text)