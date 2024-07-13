import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="<<USE_LLM_ENDPOINT_HERE>>",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# An example of few shot prompt engineering
response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer their tax related questions. "},
        {"role": "user", "content": "When do I need to file my taxes by?"},
        {"role": "assistant", "content": "In 2023, you will need to file your taxes by April 18th. The date falls after the usual April 15th deadline because April 15th falls on a Saturday in 2023. For more details, see https://www.irs.gov/filing/individuals/when-to-file."},
        {"role": "user", "content": "How can I check the status of my tax refund?"},
        {"role": "assistant", "content": "You can check the status of your tax refund by visiting https://www.irs.gov/refunds"},
        {"role": "user", "content": "Could you provide me with some information on Tax Information on Donated Property?"}
    ]
)

#print(response)
print("\n" + response.choices[0].message.content + "\n")
