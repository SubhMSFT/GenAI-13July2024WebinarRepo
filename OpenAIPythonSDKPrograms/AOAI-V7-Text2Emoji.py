import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://g42-aoai.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# An example of Text 2 Emoji translation.
response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with text, and your task is translate the text into emojis. Do not use regular text. Do your best to use emojis only."},
        {"role": "user", "content": "Artificial intelligence is a technology with great promise." },
        
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")
