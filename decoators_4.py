def Mo(a):
        def inner(m):
                sum=0
                for x in range (101):
                        if x%4==0 and x%3==0:
                                sum+=x
                print("sum of 4 and 3 multiples :",sum)
        inner(a)
Mo(101)      
