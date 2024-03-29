# # import unittest
# # from calculation import Calculations

# # class TestCalculation(unittest.TestCase):
# #     def testSum(self):
# #         cal = Calculations(8, 2)
# #         self.assertEqual(cal.getSum(), 14)

# # if __name__ == '__main__':
# #     unittest.main()

result = {"projects" : [1, 2, 3], 
            "organizations" : [5], 
            "companies" : [11],
            "categories" : []}
test = [4,4,4]
result["projects"] += test
print(result)
