from pathlib import Path 

class FileParser:
    def parse_file(self, file_path):
        """
        parse_file --> Generator function that gives a list of lines
        when this function is called

        :param: Takes the Input of the file name
        :yields: multiple lines from the input file
        :rtype: List[Line1,line2,...]
        """
        file_contents = list()
        file_check = Path(file_path).exists()
        if file_check:
            with open(file_path, "r") as input_file:
                for line in input_file.readlines():
                    file_contents.append(line.strip())
            return file_contents
        else:
            raise FileNotFoundError("Given File not Found")
    
    
