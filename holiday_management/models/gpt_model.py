from dotenv import load_dotenv
import os

from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.5-flash-lite"

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY,
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": "gemini-2.0-flash",
        "structured_output": True,
        "multiple_system_messages": False,
    },
)
