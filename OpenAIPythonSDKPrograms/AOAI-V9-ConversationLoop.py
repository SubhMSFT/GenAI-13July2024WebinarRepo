import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="<<USE_LLM_ENDPOINT_HERE>>",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("Q:")
    conversation.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="my-gpt-35-turbo",
        messages=conversation
    )
    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("\n" + response.choices[0].message.content + "\n")

    # Prompts:
    # how are you today?
    # i need some information on UPES-CSA. Do you know where it is situated?
    # yes. does it offer studies in computer science?
    # does it offer sociology?
    # what about sociolgy in Oxford?
    # I want to eat Samosas. does UPES-CSA offer samosas in their cafeteria?
    # i want you to translate something from English to Russian. can you?
    # i want to create a program in Python which can fetch data and show me movie reviews online.
    # take numbers between 1 to 1000, and create a k-means clustering algorithm, and display on screen using MatplotLib. can you help?
    # thanks. you have been very helpful
