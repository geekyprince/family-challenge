from family_challenge.Family import Family
import unittest


class TestFamily(unittest.TestCase):
    def setUp(self):
        self.lines_of_data = 31

    def test_is_correctly_loaded(self):
        family = Family()
        self.assertEqual(len(family.family_dict), self.lines_of_data)


if __name__ == "__main__":
    unittest.main()
