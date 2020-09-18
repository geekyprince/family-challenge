from family_challenge.FileReader import FileReader
import unittest
import os


"""
Since The FileReader class takes only the absolute path.
For Testing Purposes the input files are in the rootDirectory/inputs folder
To automate the loading of files
"""


class TestFileReader(unittest.TestCase):
    def setUp(self):
        """
        setUp Input Directory for tests is the current directory
        + inputs folder This function setup the file directory
        and gets the file names from it
        """
        self.input_file_directory = "".join([os.getcwd(), "/inputs/"])
        self.input_file_list = os.listdir(self.input_file_directory)
        self.read_file = FileReader().read_file

    def test_input_files_are_not_empty(self):
        for file_name in self.input_file_list:
            input_file_path = "".join(
                [self.input_file_directory + file_name]
            )
            self.assertIsNotNone(self.read_file(input_file_path))

    def test_bad_input_file_path(self):
        for name in ["x", "y", "z"]:
            input_file_path = "".join(
                [os.getcwd(), "/inputs/", name, ".txt"]
            )
            self.assertRaises(
                FileNotFoundError, self.read_file, input_file_path
            )


if __name__ == "__main__":
    unittest.main()
