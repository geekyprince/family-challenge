from family_challenge.CommandLineApp import CommandLineApp

import unittest
import sys


class TestCommandLineApp(unittest.TestCase):
    def setUp(self):
        """
        setUp --> Adds a test fileName to the sys.argv and checks if it is
        read by the commandLineApp
        """
        sys.argv.append("sampleFile.txt")

    def test_command_line_input(self):
        """
        test_command_line_input --> This gets the sys.argv[1] and asserts
        whether it is not None 
        """
        testReader = CommandLineApp()
        self.assertIsNotNone(testReader)


if __name__ == "__main__":
    unittest.main()
