''''This simple program compute
	the famous fibonacci number
	'''

def fib(max)
	a, b = 0, 1
	while a < max:
		yield a
		a, b = b, a + b

if __name__ = '__main__'
	number = input ('please input the number: ')
	fib(number)
