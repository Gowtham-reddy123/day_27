def Mo(a):
    def inner(m):
        sum = 0
        for x in range(m+1):
            if x % 5== 0 and x % 4==0:
                sum += x
        print("sum of odd number from 1 to 101:", sum)
        return a(m)
    return inner

@Mo

def a(m):
    print(" ")
a(100)


     
                                                                                                                                                                        
