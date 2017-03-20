from list_zeros import push_zeros
import unittest

class TestListZeros(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(push_zeros([]), [])

    def test_list_single_element(self):
        self.assertEqual(push_zeros([1]), [1])
        self.assertEqual(push_zeros([0]), [0])

    def test_list_two_elements(self):
        self.assertEqual(push_zeros([1, 1]), [1, 1])
        self.assertEqual(push_zeros([1, 0]), [1, 0])
        self.assertEqual(push_zeros([0, 1]), [1, 0])

    def test_list_three_elements(self):
        self.assertEqual(push_zeros([1, 1, 1]), [1, 1, 1])
        self.assertEqual(push_zeros([0, 1, 2]), [1, 2, 0])
        self.assertEqual(push_zeros([1, 0, 2]), [1, 2, 0])
        self.assertEqual(push_zeros([0, 0, 1]), [1, 0, 0])

    def test_list_four_elements(self):
        self.assertEqual(push_zeros([0, 1, 0, 2]), [1, 2, 0, 0])
