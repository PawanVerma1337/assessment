import unittest
from dict_transform import dict_transform

class Dict_Transform_Test(unittest.TestCase):
    
    # Test for all the days of the week with no omissions.    
    def test_dict_transform_full(self):
        input = {
            '2020-01-01': 4, 
            '2020-01-02': 4, 
            '2020-01-03': 6, 
            '2020-01-04': 8, 
            '2020-01-05': 2,
            '2020-01-06': -6, 
            '2020-01-07': 2, 
            '2020-01-08':-2
            }
        output = {
            'Mon': -6,
            'Tue': 2, 
            'Wed': 2, 
            'Thu': 4, 
            'Fri': 6, 
            'Sat': 8, 
            'Sun': 2
            }

        self.assertEqual(dict_transform(input), output, "Should be equal")
    
    # Test for some the days of the week with omissions.
    def test_dict_transform_partial(self):
        input = {
            '2020-01-02':6, 
            '2020-01-04': 12, 
            '2020-01-05': 14,
            '2020-01-06': 2, 
            '2020-01-07': 4 
            }
        output = {
            'Mon': 2, 
            'Tue': 4, 
            'Wed': 5, 
            'Thu': 6, 
            'Fri': 9, 
            'Sat': 12, 
            'Sun': 14
            }

        self.assertEqual(dict_transform(input), output, "Should be equal")

if __name__ == '__main__':
    unittest.main()