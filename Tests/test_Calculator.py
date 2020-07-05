import unittest
from pprint import pprint
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)
        print("self Successful")

    def test_add(self):
        testData = CsvReader('src/csvFiles/Unit Test Addition.csv').data
        for row in testData:
            self.assertEqual(self.calculator.add(int(row["Value 1"]), int(row["Value 2"])), int(row["Result"]))
            self.assertEqual(self.calculator.result, int(row["Result"]))
        print("Add Successful")

    def test_subtract(self):
        testData1 = CsvReader('src/csvFiles/Unit Test Subtraction.csv').data
        for row in testData1:
            self.assertEqual(self.calculator.subtract(int(row["Value 2"]), int(row["Value 1"])), int(row["Result"]))
            self.assertEqual(self.calculator.result, int(row["Result"]))
        print("subtraction Successful")

    def test_multiply(self):
        testData1 = CsvReader('src/csvFiles/Unit Test Multiplication.csv').data
        for row in testData1:
            self.assertEqual(self.calculator.multiply(int(row["Value 2"]), int(row["Value 1"])), int(row["Result"]))
            self.assertEqual(self.calculator.result, int(row["Result"]))
        print("multiply Successful")

    def test_divide(self):
        testData1 = CsvReader('src/csvFiles/Unit Test Division.csv').data
        for row in testData1:
            self.assertEqual(self.calculator.divide(float(row["Value 2"]), float(row["Value 1"])), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))
        print("Division Successful")

    def test_square(self):
        testData1 = CsvReader('src/csvFiles/Unit Test Square.csv').data
        for row in testData1:
            self.assertEqual(self.calculator.square(int(row["Value 1"])), int(row["Result"]))
            self.assertEqual(self.calculator.result, int(row["Result"]))
        print("square Successful")

    def test_radical(self):
        testData1 = CsvReader('src/csvFiles/Unit Test Square Root.csv').data
        for row in testData1:
            self.assertEqual(self.calculator.radical(float(row["Value 1"])), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))
        print("radical Successful")


if __name__ == '__main__':
    unittest.main()
