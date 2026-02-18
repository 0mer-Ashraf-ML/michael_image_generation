import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = os.getenv("MODEL_ID", "gemini-3-pro-image-preview")

# Cost config
COST_PER_4K_IMAGE = 0.24
COST_INPUT_IMAGE = 0.0011
COST_PER_1M_INPUT_TOKENS = 2.00

if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found.")
