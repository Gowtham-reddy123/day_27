def Mo(a):
        def inner(m):
                sum=0
                for x in range (1,m+1):
                        if x%5==0:
                                sum+=x
                print("sum of 5 multiples :",sum)
        inner(a)
Mo(12)
Mo(3)
Mo(4)      
