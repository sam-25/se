import unittest
from program import factorial

class TestFactorial(unittest.TestCase):
	def test_Factorial1(self):
		result1=factorial(1)
		self.assertEquals(result1,1)
	def test_Factorial2(self):
		result2=factorial(2)
		self.assertEquals(result2,2)
	def test_Factorial3(self):
		result3=factorial(3)
		self.assertEquals(result3,6)
	def test_Factorial4(self):
		result4=factorial(4)
		self.assertEquals(result4,24)
	def test_Factorial5(self):
		result5=factorial(5)
		self.assertEquals(result5,120)
	def test_Factorial6(self):
		result6=factorial(6)
		self.assertEquals(result6,720)

if __name__ == '__main__':
	unittest.main()
