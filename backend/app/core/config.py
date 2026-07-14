import os

from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Application settings
APP_NAME = os.getenv("APP_NAME", "AI Trace Explorer")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"