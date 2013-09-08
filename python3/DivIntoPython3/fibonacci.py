''''This simple program compute
	the famous fibonacci number
	'''

def fib(max):
	a, b = 0, 1
	while a < max:
	#	yield a
		a, b = b, a + b
	return b

if __name__ == '__main__':
	number=input ('please input the number: ')
	print('The fibonacci of ', number, 'is:')
	print(fib(int(number)))
