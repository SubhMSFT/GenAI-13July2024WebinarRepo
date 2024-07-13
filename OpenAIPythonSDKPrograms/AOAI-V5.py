import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://g42-aoai.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# An example of priming the output
response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You're an AI Assistant helping people find information."},
        #{"role": "user", "content": "John Smith is married to Lucy Smith. They have five kids, and he works as a software engineer at Microsoft. What search queries should I do to fact-check this? ## One possible search query is:"},
        {"role": "user", "content": "He works in Redmond. What are the top 5 places to visit in Redmond, WA? ## Here is a bulleted list of key points:\n-" },
        
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")
