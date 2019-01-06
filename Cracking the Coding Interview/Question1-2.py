# Given two strings, write a method to decide if one is a permutation of the other.
import unittest

# Sorts both strings based on python's built-in sort function. Then checks if strings are permutations of each other.
def perm(s1, s2):
	s1 = sorted(s1)
	s2 = sorted(s2)
	if (s1 == s2): return True
	return False

# Unit Testing
class UniqueTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_are_strings_perm(self):
        """Is dog successfully determined to be unique?"""
        self.assertTrue(perm("dog", "god"))
		
	def test_are_strings_not_perm(self):
		"""Is doggo correctly determined not to be prime?"""
		self.assertFalse(perm("dog", "doggos"), msg='These are not permutations of one another!')