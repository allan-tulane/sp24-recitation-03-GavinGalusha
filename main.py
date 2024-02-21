import time

class BinaryNumber:
	""" done """
	def __init__(self, n):
		self.decimal_val = n			   
		self.binary_vec = list('{0:b}'.format(n)) 

	def __repr__(self):
		return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def multiply(binary_x, binary_y):
	binary_x, binary_y = pad(binary_x, binary_y)



def binary2int(binary_vec): 
	if len(binary_vec) == 0:
		return BinaryNumber(0)
	return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
	return (binary2int(vec[:len(vec)//2]),
			binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
	# append n 0s to this number's binary string
	return binary2int(number.binary_vec + ['0'] * n)

def pad(x,y):
	# pad with leading 0 if x/y have different number of bits
	# e.g., [1,0] vs [1]
	if len(x) < len(y):
		x = ['0'] * (len(y)-len(x)) + x
	elif len(y) < len(x):
		y = ['0'] * (len(x)-len(y)) + y
	# pad with leading 0 if not even number of bits
	if len(x) % 2 != 0:
		x = ['0'] + x
		y = ['0'] + y
	return x,y

def quadratic_multiply(x, y):
	# this just converts the result from a BinaryNumber to a regular int
	return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
	# Convert binary vectors to padded versions for uniform length
	xvec, yvec = pad(x.binary_vec, y.binary_vec)

	# Base case: if both numbers are 0 or 1
	if (binary2int(xvec).decimal_val <= 1) and (binary2int(yvec).decimal_val <= 1):
		return BinaryNumber(binary2int(xvec).decimal_val * binary2int(yvec).decimal_val)

	# Recursive case: split each number and multiply the parts
	x_left, x_right = split_number(xvec)
	y_left, y_right = split_number(yvec)

	# Perform the multiplication recursively and shift bits as necessary
	a = bit_shift(_quadratic_multiply(x_left, y_left), len(xvec))
	b = bit_shift(_quadratic_multiply(x_left, y_right), len(xvec) // 2)
	c = bit_shift(_quadratic_multiply(x_right, y_left), len(xvec) // 2)
	d = _quadratic_multiply(x_right, y_right)  # No need for bit shifting by 0

	# Combine the results and return as a BinaryNumber
	return BinaryNumber(a.decimal_val + b.decimal_val + c.decimal_val + d.decimal_val)

def test_quadratic_multiply():
	start = time.time()
	# multiply two numbers x, y using function f
	print(_quadratic_multiply(BinaryNumber(10), BinaryNumber(7)))
	print(_quadratic_multiply(BinaryNumber(6), BinaryNumber(4)))

	return (time.time() - start)*1000

print(test_quadratic_multiply())
