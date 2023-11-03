import unittest
from addOneUT import addOne

#def addOne(num):
#	return num + 1


class test_addOne(unittest.TestCase):

	def test_addOnePass(self):
		self.assertEqual(addOneUT.addOne(2), 3)

	@unittest.expectedFailure
	def test_addOneFail(self):
		self.assertEqual(addOneUT.addone(2), 4)

if __name__ == '__main__':
	unittest.main()