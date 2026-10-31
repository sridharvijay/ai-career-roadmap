"""D6: call Gemini directly (no ADK) and print the response."""
import sys

from dotenv import load_dotenv
from google import genai

load_dotenv("time_agent/.env")  # provides GOOGLE_API_KEY

client = genai.Client()  # picks up GOOGLE_API_KEY from the environment
prompt = " ".join(sys.argv[1:]) or "Explain what a token is in 2 sentences."

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)
print(response.text)
print(f"\n[tokens] in={response.usage_metadata.prompt_token_count} "
      f"out={response.usage_metadata.candidates_token_count}")
