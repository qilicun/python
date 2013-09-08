class Fib:

	'''create fibonacci number iterator
	'''
	def __init__(self, max):
		self.max = max
	
	def __iter__(self):

		self.a = 0
		self.b = 1
		return self

	def __next__(self):

		fib = self.a
		if fib > self.max:

			raise StopIteration

		self.a, self.b = self.b, self.a + self.b

		return fib

if __name__ == '__main__':
	
	fib = Fib(int(input('Please input a number: ')))
	fib.__doc__ 
