import os
from dotenv import load_dotenv
import openai
import mysql.connector

load_dotenv()

print(os.getenv("database"))