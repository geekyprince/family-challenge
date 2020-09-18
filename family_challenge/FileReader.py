from pathlib import Path 

class FileReader:
    def read_file(self, file_path):
        """
        read_file --> Generator function that gives a list of lines
        when this function is called

        :param: Takes the Input of the file name
        :raises: FileNotFoundError if file not found on provided path
        :rtype: List[Line1,line2,...]
        """
        file_data = list()
        file_exists = Path(file_path).exists()
        if file_exists:
            with open(file_path, "r") as input_file:
                for line in input_file.readlines():
                    file_data.append(line.strip())
            return file_data
        else:
            raise FileNotFoundError("File not found")
    
    
