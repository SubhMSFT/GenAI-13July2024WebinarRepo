import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="<<USE_LLM_ENDPOINT_HERE>>",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# An example of one shot prompt engineering
response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You're an AI assistant that helps people find information. Answer in a consistent style."},
        {"role": "user", "content": "Teach me about patience."},
        {"role": "assistant", "content": "The river that carves the deepest valley flows from a modest spring; " +
                                         "the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread."},
        {"role": "user", "content": "Teach me about gratitude."}
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")                 # You can run the output 3 times and answers will be consistent but different each time.

