def is_it_true(anything):
	'''this function test the bool
		
		variable of python3
	'''
	if anything:
		print(anything, "yes, it's true")
	else:
		print(anything, "no, it's false")

if __name__ == '__main__':
	is_it_true(1)
	is_it_true(0)
	is_it_true(2)
	is_it_true(-1)
	
	is_it_true([])
	is_it_true(['a', 'c'])
	is_it_true([False])

