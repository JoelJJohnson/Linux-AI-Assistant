# tests/test_nlp_module.py

import unittest
from ai_linux_assistant.nlp_module import NLPProcessor

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.nlp_processor = NLPProcessor()

    def test_process_input(self):
        user_input = "List all files in the current directory."
        command = self.nlp_processor.process_input(user_input)
        self.assertIsInstance(command, str)
        self.assertNotEqual(command, '')

if __name__ == '__main__':
    unittest.main()
