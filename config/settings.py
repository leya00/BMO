import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

WINDOW_WIDTH  = 64
WINDOW_HEIGHT = 128