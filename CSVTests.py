import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/csvFiles/Unit Test Addition.csv')

    def test_return_data_as_objects(self):
        numbers = self.csv_reader.return_data_as_objects('number')
        self.assertIsInstance(numbers, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for number in numbers:
            self.assertEqual(number.__name__, test_class.__name__ )


if __name__ == '__main__':
    unittest.main()
