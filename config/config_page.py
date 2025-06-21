import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get base directory
RESUME_FILE = os.path.join(BASE_DIR, "/home/kamesh/Videos/QA_Kamesh_sulakshane_jan.pdf")  # Example file path

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")