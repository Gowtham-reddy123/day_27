def Mo(a):
	def inner(m):
		sum=0
		for x in range (101):
			if x % 2==0:
				sum+=x
		print("sum of even number from 0 to m is :",sum)
	inner(a)
Mo(101)

