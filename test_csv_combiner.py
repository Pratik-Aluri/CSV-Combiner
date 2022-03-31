import unittest
from csv-combiner import *

class Combiner_Tests(unittest.TestCase):
    
    def setUp(self):
        print("setUp called")
        self.csv = 'random.csv'
        self.path = '~/Desktop/PMG/random.csv'

    def test_csv(self):
        print('Test if file is a CSV')
        self.assertEqual(self.csv.endswith('.csv'), "Not a csv file")
    
    def test_name(self):
        print('Testing the basename of file')
        self.assertEqual(get_name(self.path), 'random.csv', "Wrong file name")
        

if __name__ == "__main__":
    unittest.main()
