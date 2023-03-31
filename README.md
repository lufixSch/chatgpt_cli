# ChatGPT Cli

Unofficial command line interface for the use of ChatGPT

## Usage

Enter the chat by executing `chatgpt`. This will open a new chat and generate a `.chatgpt_config.json` in your home directory.

You need to provide an API Key with `chatgpt --api-key <YOUR API KEY>` or add it to the `.chatgpt_config.json`.

**Other Options:**
```
-h, --help            show this help message and exit
--model MODEL         The name of the GPT model to use (Default: gpt-3.5-turbo)
--max-tokens MAX_TOKENS
                      The maximum number of tokens to generate in the response (Default: 1024))
--temperature TEMPERATURE
                      The temperature to use for sampling from the GPT model (Default: 0.7))
--api-key API_KEY     The OpenAI API key to use (Default: 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)
--system-message SYSTEM_MESSAGE
                      The message added to the Chat before the first message (Default: You are ChatGPT, a large language model trained by OpenAI. Carefully heed the user's instructions.)
```

Inside the chat you can talk to ChatGPT as usual. But you can also enter some commands.

**Commands:**
```
help (?):      Print this message
clear (c):     Clear chat history
exit (^D, ^C): Exit the program
history (h):   Print chat history
```