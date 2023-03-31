#!/bin/env python3

import openai
import argparse
import os
import json
from colorama import Fore, Style


def status(msg: str):
    """Print status message in bold and light gray"""
    print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}{msg}{Style.RESET_ALL}")


def main():
    # Load or create config file
    config_file_path = os.path.expanduser("~/.chatgpt_config.json")
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            config = json.load(f)
    else:
        status(
            f"Config file not found at {config_file_path}. Creating one now..."
        )

        config = {
            "model": "gpt-3.5-turbo",
            "max_tokens": 1024,
            "temperature": 0.7,
            "api_key": None,
            "system_message": "You are ChatGPT, a large language model \
trained by OpenAI. Carefully heed the user's instructions.",
        }
        with open(config_file_path, "w") as f:
            json.dump(config, f)

    # Set up CLI argument parser
    parser = argparse.ArgumentParser(description="Chat with GPT")
    parser.add_argument(
        "--model",
        type=str,
        default=config["model"],
        help=f"The name of the GPT model to use (Default: {config['model']})",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=config["max_tokens"],
        help=f"The maximum number of tokens to generate in the response \
(Default: {config['max_tokens']}))",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=config["temperature"],
        help=f"The temperature to use for sampling from the GPT model \
(Default: {config['temperature']}))",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=config["api_key"],
        help=f"The OpenAI API key to use (Default: {config['api_key']})",
    )
    parser.add_argument(
        "--system-message",
        type=str,
        default=config["system_message"],
        help=f"The message added to the Chat before the first message \
(Default: {config['system_message']})",
    )
    args = parser.parse_args()

    # Set up OpenAI API credentials
    openai.api_key = args.api_key

    # Use command-line arguments if present, otherwise use config file values
    model = args.model
    max_tokens = args.max_tokens
    temperature = args.temperature
    system_message = args.system_message

    chat_history = [{"role": "system", "content": system_message}]

    # Main loop
    try:
        while True:
            # Get user input
            user_input = input("> ")

            if user_input == "clear" or user_input == "c":
                chat_history = [{"role": "system", "content": system_message}]
                status("Chat history cleared.")
            elif user_input == "exit":
                break
            elif user_input == "history" or user_input == "h":
                for item in chat_history:
                    print(
                        f"{Style.BRIGHT}{item['role'].upper()}\
{Style.RESET_ALL}: {item['content']}"
                    )
            elif user_input == "help" or user_input == "?":
                status("Commands:")
                print(f"{'help (?):':<14} Print this message")
                print(f"{'clear (c):':<14} Clear chat history")
                print(f"{'exit (^D, ^C):':<14} Exit the program")
                print(f"{'history (h):':<14} Print chat history")
            else:
                chat_history.append({"role": "user", "content": user_input})

                # Generate response from OpenAI API
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=chat_history,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    n=1,
                )

                # Format response in Bash
                message = response.choices[0].message
                chat_history.append(message)

                # Print Bash-formatted response
                print(message.content)
    except KeyboardInterrupt:
        print()
    except EOFError:
        print()
    finally:
        status("Exiting...")
