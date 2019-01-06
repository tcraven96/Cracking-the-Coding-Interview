# Implement an algorithm to determine if each string has all unique characters.
# What if you cannot use additional data structures?
import unittest

# Goes through string, replaces element found once with "" so that duplicates are not replaced. 
# Will return if duplicate characters are found in the string.
def unique(s):
	for elem in s:
		s = s.replace(elem, "", 1)
		if elem in s: return False
	return True

# Unit Testing
class UniqueTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_dog_unique(self):
        """Is dog successfully determined to be unique?"""
        self.assertTrue(unique("dog"))
		
	def test_is_doggo_not_unique(self):
		"""Is doggo correctly determined not to be prime?"""
		self.assertFalse(unique("doggo"), msg='Doggo is not unique!')




