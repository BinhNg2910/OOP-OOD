import unittest
from A1 import *

answerSearchTitle = {"projects" : [p1], 
                     "organizations" : [o1, o1_2],
                     "companies" : [com1],
                     "categories" : [cate1, cate2]}
answerSearchTitle_1 = {"projects" : [p2], 
                     "organizations" : [o2],
                     "companies" : [com2],
                     "categories" : [cate3, cate4]}
answerSearchTitle_2 = {"projects" : [p3], 
                     "organizations" : [o31, o32],
                     "companies" : [com1],
                     "categories" : [cate5, cate6]}
answerSearchLocation = {"projects" : [p1, p3], 
                     "organizations" : [o1, o1_2, o32],
                     "companies" : [com1],
                     "categories" : [cate1, cate2, cate6]}
answerSearchOrganization = {"projects" : [p1, p3], 
                     "organizations" : [o1],
                     "companies" : [com1],
                     "categories" : [cate1, cate2, cate6]}
answerSearchCompany = {"projects" : [p1, p3], 
                     "organizations" : [o1, o1_2, o32],
                     "companies" : [com1],
                     "categories" : [cate1, cate2, cate6]}
answerSearchCategory = {"projects" : [p1, p3], 
                     "organizations" : [o1, o1_2, o32],
                     "companies" : [com1],
                     "categories" : [cate1]}

class TestFunction(unittest.TestCase):
    def testSearchByProjectTitle(self):
        searchAnswer = system.searchByTitle("p1")
        self.assertEqual(searchAnswer, answerSearchTitle)
    def testSearchByProjectTitle_1(self):
        searchAnswer = system.searchByTitle("p2")
        self.assertEqual(searchAnswer, answerSearchTitle_1)
    def testSearchByProjectTitle_2(self):
        searchAnswer = system.searchByTitle("p3")
        self.assertEqual(searchAnswer, answerSearchTitle_2)
    def testSearchByLocation(self):
        searchAnswer = system.searchByLocation("l1")
        self.assertEqual(searchAnswer, answerSearchLocation)
    def testSearchByOrganization(self):
        searchAnswer = system.searchByOrganization("o1", "role1")
        self.assertEqual(searchAnswer, answerSearchOrganization)
    def testSearchByCompany(self):
        searchAnswer = system.searchByCompany("com1")
        self.assertEqual(searchAnswer, answerSearchCompany)
    def testSearchByCategory(self):
        searchAnswer = system.searchByCategory("c1", "a1")
        self.assertEqual(searchAnswer, answerSearchCategory)

if __name__ == '__main__':
    unittest.main()