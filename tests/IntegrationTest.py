from family_challenge.FileReader import FileReader
import os
import unittest


class IntegrationTest(unittest.TestCase):
    def setUp(self):

        self.join = lambda dir, name: "".join([dir, name])
        self.expected_output_file_directory = "".join(
            [os.getcwd(), "/outputs/"]
        )
        self.expected_output_file_list = os.listdir(
            self.expected_output_file_directory
        )
        self.actual_output_file_directory = "".join(
            [os.getcwd(), "/actual_outputs/"]
        )
        self.actual_output_file_list = os.listdir(
            self.actual_output_file_directory
        )
        self.file_reader = FileReader()

    def test_actual_output_with_expected_output(self):
        for expected_op_file, actual_op_file in zip(
            self.expected_output_file_list, self.actual_output_file_list,
        ):
            expected_op_contents = self.file_reader.read_file(
                self.join(
                    self.expected_output_file_directory, expected_op_file
                )
            )
            actual_op_contents = self.file_reader.read_file(
                self.join(
                    self.actual_output_file_directory, actual_op_file
                )
            )
            actual_output = " ".join(actual_op_contents)
            expected_output = " ".join(expected_op_contents)
            self.assertEqual(set(actual_output.split(" ")), set(expected_output.split(" ")))


if __name__ == "__main__":
    unittest.main()
