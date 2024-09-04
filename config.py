import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('API_KEY')
print(f'HELLO {os.getenv("MY_NAME")}')