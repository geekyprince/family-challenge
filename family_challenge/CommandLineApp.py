from family_challenge.FileReader import FileReader
import sys

class CommandLineApp:
    def __init__(self):
        """
        __init__ --> Gets the filePath from Command Line.
        Initializes an instance of the file parser to
        get the file contents
        """
        self.file_path = sys.argv[1]
        self.file_reader = FileReader()

    def get_file_data(self):
        """
        get_file_contents --> Uses an instance of FileReader Class,
        to get the File's content

        :return: Contents of the File
        :rtype: List
        """
        return self.file_reader.read_file(self.file_path)
