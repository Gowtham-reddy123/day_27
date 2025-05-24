def Mo(a):
	def inner(m):	
		if m%2==0:
			print("the number is even")
		else:
			a(m)
	return inner
@Mo

def A(m):
	print("this is odd ")
A(2)
A(3)
	
