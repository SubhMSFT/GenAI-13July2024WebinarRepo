using Microsoft.SemanticKernel;                     // meta-package includes Core packages & OpenAI connectors
using Microsoft.SemanticKernel.ChatCompletion;
using System.Text;

// DO not embed key in code 
// For Az Prod, either use Az Key Vault, or, preferably DefaultAzureCredential() class
// Provides a default TokenCredential auth flow for applications deployed in Az
string apikey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY")!;

// Creating an instance of the conversation:
Kernel kernel = Kernel.CreateBuilder()
        .AddAzureOpenAIChatCompletion("my-gpt-35-turbo", "<< USE LLM ENDPOINT HERE FROM AZURE AI STUDIO >>", apikey)
        .Build();

// Example1: Invoke the kernel with a prompt and display the result
Console.WriteLine(await kernel.InvokePromptAsync("What color is the sky?"));
Console.WriteLine();

// Example2:
Console.WriteLine(await kernel.InvokePromptAsync("Where is UPES-CSA based?"));
Console.WriteLine();

// Example3:
Console.WriteLine(await kernel.InvokePromptAsync("what are a few things a guy can do if his girlfriend is angry?"));
Console.WriteLine();

while (true)
{
    Console.Write("Question: ");
    Console.WriteLine(await kernel.InvokePromptAsync(Console.ReadLine()));
    Console.WriteLine();
}

// Use below code for 2nd Iteration as showcased in Webinar Demo
/*
var chatService = kernel.GetRequiredService<IChatCompletionService>();
ChatHistory chat = new();

while (true)
{
    Console.Write("Qunestion: ");
    chat.AddUserMessage(Console.ReadLine());

    // Need a response back 
    var response = await chatService.GetChatMessageContentAsync(chat);
    Console.WriteLine(response);

    // Add back the response into my chat history
    chat.Add(response);
}
*/
