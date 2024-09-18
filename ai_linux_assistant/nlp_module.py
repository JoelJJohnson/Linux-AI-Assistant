# ai_linux_assistant/nlp_module.py

import openai
import re
import logging
from openai.error import OpenAIError

class NLPProcessor:
    def __init__(self):
        # Load the API key from the api_key.txt file
        try:
            with open('api_key.txt', 'r') as file:
                api_key = file.read().strip()
            openai.api_key = api_key
        except FileNotFoundError:
            raise Exception("API key file 'api_key.txt' not found. Please make sure it exists.")
        except Exception as e:
            raise Exception(f"Error reading API key: {str(e)}")

    def process_input(self, user_input):
        prompt = (
            "Translate the following English instruction into an equivalent Linux command. "
            "Provide only the command without any code block markers, backticks, or explanations.\n"
            f"Instruction: {user_input}\nLinux Command:"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0,
            )
        except OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            print("An error occurred while processing your request. Please try again later.")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("An unexpected error occurred. Please try again later.")
            return None

        # Validate response
        if not response or not response.choices or not response.choices[0].message:
            logging.error("Invalid response structure from OpenAI API.")
            print("Received an invalid response from the AI service.")
            return None

        command = response.choices[0].message['content'].strip()

        # Remove code block markers using regex
        command = re.sub(r'```(?:bash)?\s*', '', command)  # Remove starting code block markers
        command = re.sub(r'\s*```', '', command)           # Remove ending code block markers
        command = command.strip('`').strip()               # Remove any remaining backticks and whitespace

        return command
