import unittest #took at a from aimport

#import lab1
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

#tests for max_list_iter
    def test_max_list_iter_noneParameter(self):
        """when none is passed in, raises ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_emptyList(self):
        """when empty list, return None"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter_singleElement(self):
        """when len = 1, return list[0]"""
        tlist = [127]
        self.assertEqual(max_list_iter(tlist), 127)

    def test_max_list_iter_maxIsLast(self):
        """when last index has max, return list[len(tlist)-1]"""
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_maxIsFirst(self):
        """when first index has max, return list[0]"""
        tlist = [4, 3, 2]
        self.assertEqual(max_list_iter(tlist), 4)

    def test_max_list_iter_allSame(self):
        """when all elements are identical, return list[0]"""
        tlist = [4, 4, 4]
        self.assertEqual(max_list_iter(tlist), 4)

    def test_max_list_iter_random(self):
        """return max"""
        tlist = [3, 2, 4, 3]
        self.assertEqual(max_list_iter(tlist), 4)

#tests for reverse_rec
    def test_max_list_iter_noneParameter(self):
        """when none is passed in, raises ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec_random(self):
        """when list random, return rev"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_elementsIdentical(self):
        """when all elements are identical"""
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])

    def test_reverse_rec_oneElement(self):
        """when one element, return identical list"""
        self.assertEqual(reverse_rec([1]),[1])

    def test_reverse_rec_evenNo(self):
        """even number of index"""
        self.assertEqual(reverse_rec([1,2,3,4]),[4,3,2,1])

    def test_reverse_rec_string(self):
        """when elements are string, return string"""
        self.assertEqual(reverse_rec(["Please","Mr.","Robot","Do","Not","Eat","My","Husband"]),["Husband","My","Eat","Not","Do","Robot","Mr.","Please"])

    #write for multi element

#tests for bin_search... #array must already be sorted
    def test_bin_search_random(self):
        """"return index"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(4, low, high, list_val), 4 )

    def test_bin_search_lastIndex(self):
        """"return list_val[len(list_val)-1]"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(10, low, high, list_val), 8 )

    def test_bin_search_firstIndex(self):
        """"return list_val[0]"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(0, low, high, list_val), 0 )

    def test_bin_search_allSame(self):  #instructor says don't think about duplicates
        """"each element is identical, returns mid"""
        list_val =[9,9,9,9,9,9]
        low = 0
        high = 5
        self.assertEqual(bin_search(9, low, high, list_val), 2 )

    def test_bin_search_notInList(self):
        """"not in list, returns None"""
        list_val =[0,1,2,3]
        low = 0
        high = 3
        self.assertEqual(bin_search(5, low, high, list_val), None )

if __name__ == "__main__":
        unittest.main()

    
