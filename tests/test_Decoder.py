from family_challenge.Decoder import Decoder
from family_challenge.Family import Family
import unittest


class TestDecoder(unittest.TestCase):
    def setUp(self):
        """
        setUp --> Creates a decoder instance for every test
        """
        self.family = Family()
        self.decoder = Decoder()
        self.data1 = ['Atya', 'Sister-In-Law']
        self.data2 = ['Satya', 'Ketu', 'Male']

    def test_get_relationship(self):
        self.assertEqual(self.decoder.get_relationship(self.data1, self.family.family_dict), {'Satvy', 'Krpi'})

    def test_add_child(self):
        self.assertEqual(self.decoder.add_child(self.data2, self.family), "CHILD_ADDITION_SUCCEEDED")
        

