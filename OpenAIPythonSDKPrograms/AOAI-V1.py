import os                                                       # interact with underlying OS
from openai import AzureOpenAI                                  # import Azure OpenAI libs

# create an instance of Azure OpenAI: 3 things needed
client = AzureOpenAI(
    
    # retrieve endpoint from model deployment in Azure AI Studio
    azure_endpoint="<<USE_LLM_ENDPOINT_HERE>>",
    
    # using environment variable for Demo purposes: *not* recommended for Prod
    # guidance here: either use Azure Key Vault or preferably DefaultAzureCredential() class
    # provides a def TokenCredential auth flow for applications for Prod in Az
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    
    # use API version property corresponding to specific method you're calling in API.
    # guidance here: use non-preview versions for Prod in Az
    api_version="2024-02-15-preview"
)

response=client.chat.completions.create(
    model="my-gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You're an AI assistant that helps people find information. If the user asks you a question you don't know the answer to, say so."},
        {"role": "user", "content": "What is the EmployeeID of an employee called Subhasish Ghosh who works at Microsoft?"}
    ],
    
    ## Azure OpenAI LLM hyperparameters
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0    
)

print(response)

print("\n")
print(f'Let us capture Tokens usage stats.')
print(f'Number of tokens in your prompt, that are input to your model. {response.usage.prompt_tokens} prompt tokens used.')
print(f'Number of tokens that model generates in response to your input. {response.usage.completion_tokens} completion token used.')
print(f'{response.usage.total_tokens} total tokens used.')
         
print("\n" + response.choices[0].message.content + "\n")
