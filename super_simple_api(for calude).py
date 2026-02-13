# Import required libraries
import os
from dotenv import load_dotenv
from anthropic import Anthropic


#Load environment variables from .env file
load_dotenv()


#  Create Claude client using API key
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


# Send a message to Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Explain product management in one sentence."}
    ]
)


# Print Claude's response
print(response.content[0].text)