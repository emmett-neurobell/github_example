import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

print("Hello, world!")

print(f'Don\'t put this on github - API Key: {API_KEY}')