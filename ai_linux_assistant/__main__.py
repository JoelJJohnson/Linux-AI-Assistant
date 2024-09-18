#!/usr/bin/env python3

import os
import argparse
import subprocess
import shlex  # Import shlex for command parsing
import logging
import re  # For command validation
from ai_linux_assistant.nlp_module import NLPProcessor
from ai_linux_assistant.confirmation_prompt import ConfirmationPrompt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='assistant.log',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    # Read the API key from api_key.txt
    try:
        with open('api_key.txt', 'r') as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        logging.error("API key file 'api_key.txt' not found.")
        print("Error: API key file 'api_key.txt' not found.")
        print("Please create a file named 'api_key.txt' in the project root directory containing your OpenAI API key.")
        return
    except PermissionError:
        logging.error("Permission denied when accessing 'api_key.txt'.")
        print("Error: Permission denied when accessing 'api_key.txt'.")
        return
    except Exception as e:
        logging.error(f"Error reading API key: {e}")
        print(f"Error reading API key: {e}")
        return

    if not api_key:
        logging.error("OpenAI API key is empty.")
        print("Error: OpenAI API key is empty.")
        return

    # Validate API key format (basic check)
    if not api_key.startswith('sk-'):
        logging.error("Invalid OpenAI API key format.")
        print("Error: Invalid OpenAI API key format.")
        return

    nlp_processor = NLPProcessor()
    confirmation_prompt = ConfirmationPrompt()

    # Add argument parsing here
    parser = argparse.ArgumentParser(
        description="AI-Powered Linux Assistant: Translates natural language commands into executable Linux commands."
    )
    parser.add_argument(
        '-c', '--command',
        type=str,
        help='Provide a natural language command directly without entering interactive mode.'
    )
    parser.add_argument(
        '--no-confirm',
        action='store_true',
        help='Execute the command without asking for confirmation.'
    )
    args = parser.parse_args()

    if args.command:
        user_input = args.command
        command = nlp_processor.process_input(user_input)

        if command is None:
            print("Failed to generate a command.")
            return

        if not is_safe_command(command):
            print("The generated command is potentially unsafe and will not be executed.")
            logging.warning(f"Unsafe command detected: {command}")
            return

        if args.no_confirm:
            execute_command(command)
        else:
            if confirmation_prompt.confirm(command):
                execute_command(command)
            else:
                print("Command execution canceled.")
    else:
        # Interactive mode
        try:
            while True:
                user_input = input("Enter your command (or type 'exit' to quit): ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("Exiting AI Linux Assistant.")
                    break

                if not user_input:
                    print("Please enter a command or type 'exit' to quit.")
                    continue

                logging.info(f"User input: {user_input}")

                command = nlp_processor.process_input(user_input)

                if command is None:
                    print("Failed to generate a command. Please try rephrasing your instruction.")
                    continue

                logging.info(f"Generated command: {command}")

                if not is_safe_command(command):
                    print("The generated command is potentially unsafe and will not be executed.")
                    logging.warning(f"Unsafe command detected: {command}")
                    continue

                if confirmation_prompt.confirm(command):
                    execute_command(command)
                else:
                    print("Command execution canceled.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting.")
            logging.info("Program interrupted by user.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print("An unexpected error occurred. Please check the logs for more details.")

def execute_command(command):
    try:
        # Handle multi-line commands
        commands = command.strip().split('\n')
        for cmd in commands:
            cmd = cmd.strip()
            if not cmd:
                continue
            # Use shlex to safely split the command
            args = shlex.split(cmd)
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command execution failed: {e.stderr}")
        print(f"Error executing command: {e.stderr}")
    except FileNotFoundError:
        logging.error("Command not found.")
        print("Error: Command not found.")
    except Exception as e:
        logging.error(f"Unexpected error during command execution: {e}")
        print("An unexpected error occurred during command execution.")

def is_safe_command(command):
    # Define a list of dangerous commands or patterns
    dangerous_patterns = [
        r'\brm\s+-rf\s+/.*',  # Matches 'rm -rf /' and similar
        r':\s*(){\s*:\s*|\s*};\s*:',  # Matches fork bombs
        # Add more patterns as needed
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, command):
            return False
    return True

if __name__ == '__main__':
    main()
