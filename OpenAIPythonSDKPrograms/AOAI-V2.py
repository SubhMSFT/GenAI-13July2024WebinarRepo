import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://g42-aoai.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You're an AI assistant that helps people find information. If the user asks you a question you don't know the answer to, say so."},
        {"role": "user", "content": "Who is Syd Barrett?"},
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")