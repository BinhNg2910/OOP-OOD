import unittest
from A2 import *

class TestFunction(unittest.TestCase):
    def testSearchByProjectTitle1(self):
        output = system.searchByTitle_OutputFile("p1")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample1_searchByTitle.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)
    def testSearchByProjectTitle2(self):
        output = system.searchByTitle_OutputFile("p7")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample2_searchByTitle.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)

    def testSearchByLocation(self):
        output = system.searchByLocation_OutputFile("l1")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample_searchByLocation.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)

    def testSearchByOrganization(self):
        output = system.searchByOrganization_OutputFile("name1", "role1")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample_searchByOrganization.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)

    def testSearchByCompany(self):
        output = system.searchByCompany_OutputFile("com2")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample_searchByCompany.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)

    def testSearchByCategory(self):
        output = system.searchByCategory_OutputFile("cate11", "a11")
        system.exportOutputFile("output.txt", output)
        expected_output_file = 'sample_searchByCategory.txt'
        actual_output_file = 'output.txt'
        with open(expected_output_file, 'r') as file:
            expected_output = file.read()
        with open(actual_output_file, 'r') as file:
            actual_output = file.read()        
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()