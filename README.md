# Linux-AI-Assistant
This is a ChatGPT powered AI assistant designed to convert natural language into linux commands to help biginners and professionals to work on linux systems with ease.

## Overview

AI Linux Assistant is a Python-based tool that uses OpenAI's API to assist users in converting natural language instructions into equivalent Linux commands. This is useful for both beginners learning Linux commands and advanced users looking to automate common tasks via natural language.

## Features

- Converts English instructions to Linux commands using OpenAI's API.
- Handles common OpenAI API errors like authentication issues, rate limits, and invalid requests.
- Designed to be run directly from the terminal with the `linuxAI` command.
- Easy setup and secure API key management through `api_key.txt`.

## Prerequisites

- **Python 3.6+**
- **OpenAI API Key**: You will need an API key from OpenAI to interact with their API. Sign up at [OpenAI](https://platform.openai.com/account/api-keys) to get your API key.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai_linux_assistant.git
   cd ai_linux_assistant
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   .venv\Scripts\activate     # On Windows
   ```

3. **Install required dependencies**:
   The project dependencies are listed in the `requirements.txt` file. To install them, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the OpenAI API key**:
   Open the file called `api_key.txt` in the project directory, and add your OpenAI API key to it:
   ```txt
   your-api-key-here
   ```

## Usage

1. **Running the Assistant via Python**:
   You can run the AI Linux Assistant directly by executing the main script:
   ```bash
   python main.py
   ```

   The assistant will prompt you to input an English instruction and will return the equivalent Linux command.

   **Example**:
   ```bash
   Enter your instruction: List all files in the current directory.
   Linux Command: ls
   ```

2. **Running the Assistant as a Command (`linuxAI`)**:
   You can set up the project to run from the terminal with the command `linuxAI`.

   ### Steps:
   1. Ensure your `main.py` contains the proper shebang:
      ```python
      #!/usr/bin/env python3
      ```
   
   2. Rename `main.py` to `linuxAI` or create a new script with this name.
   
   3. Make the script executable:
      ```bash
      chmod +x linuxAI
      ```
   
   4. Move the script to a directory in your `PATH`:
      ```bash
      sudo mv linuxAI /usr/local/bin/
      ```

   5. Now, you can simply run:
      ```bash
      linuxAI
      ```
![Screenshot 2024-09-18 152221](https://github.com/user-attachments/assets/47d4aba6-0e5a-4b28-b3f6-33c78121c77c)

## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear explanation of the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Built using [OpenAI](https://openai.com)'s API.
- Developed by [Joel Johnson](https://github.com/JoelJJohnson).

---

