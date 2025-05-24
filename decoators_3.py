def Mo(a):
        def inner(m):
                sum=0
                for x in range (101):
                        if x % 2!=0:
                                sum+=x
                print("sum of odd number from 1 to 101:",sum)
        inner(a)
Mo(101)
