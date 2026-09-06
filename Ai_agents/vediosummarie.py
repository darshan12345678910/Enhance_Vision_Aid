import streamlit as st 
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import google.generativeai as genai

import time
from pathlib import Path

import tempfile

from dotenv import load_dotenv
load_dotenv()

import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

img_path = "F:\Enhanced_Vision_Aid\Testing-images\istockphoto-656497862-612x612.jpg"
file_ref = client.files.upload(file=img_path)
print(f'{file_ref=}')

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=["What can you tell me about these instruments?",
              file_ref])

print(response.text)
