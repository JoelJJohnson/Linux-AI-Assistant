# ai_linux_assistant/confirmation_prompt.py

import shlex

class ConfirmationPrompt:
    def confirm(self, command):
        # Basic safety check to prevent execution of dangerous commands
        dangerous_commands = [] # List the commands you do not want to be executed in '' separated by , in the square brackets

        tokens = shlex.split(command)
        if any(dc in tokens for dc in dangerous_commands):
            print("Dangerous command detected. Execution aborted.")
            return False

        while True:
            user_input = input(f"The command to execute is:\n\n{command}\n\nDo you want to proceed? (yes/no): ").lower()
            if user_input in ['yes', 'y']:
                return True
            elif user_input in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'.")
