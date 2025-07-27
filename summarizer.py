from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("chat.txt", "r") as fh:
    messages = fh.read()


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Summarize this: {messages}"}
    ]
)

sumamry = response.choices[0].message.content

print("\nSummary:\n")
print(summary)

with open("output.txt", "w", encoding="utf-8")as output:
    output.write(summary)