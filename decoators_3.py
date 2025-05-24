def Mo(a):
        def inner(m):
                sum=0
                for x in range (m+1):
                        if x % 2!=0:
                                sum+=x
                print("sum of odd number from 0 to m is :",sum)
        inner(a)
Mo(12)
Mo(3)
Mo(4)      
