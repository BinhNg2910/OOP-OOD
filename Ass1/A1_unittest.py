import unittest
from A1 import *

answerSearchTitle = {"projects" : [p1], 
                     "organizations" : [o1],
                     "companies" : [com1],
                     "categories" : [cate1, cate2]}

# system.printSearchResult(answerSearchTitle)

class TestFunction(unittest.TestCase):
    def testSearchByProjectTitle(self):
        searchAnswer = system.searchByTitle("p1")
        self.assertEqual(searchAnswer, answerSearchTitle)
    def testSearchByOrganization(self):
        searchAnswer = system.searchByOrganization("o1", "role1")
        self.assertEqual(searchAnswer, answerSearchTitle)

if __name__ == '__main__':
    unittest.main()