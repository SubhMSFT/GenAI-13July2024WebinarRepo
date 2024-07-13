import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://g42-aoai.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# An example of English to Russian translation.
response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with English sentences, and your task is translate them from English to Russian."},
        {"role": "user", "content": "I am feeling well today. My name is Subhasish and I live in Redmond." },
        
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")