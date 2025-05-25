def Mo(a):
    def inner(m):
        sum = 0
        for x in range(m+1):
            if x%4==0 and x%3==0:
                sum += x
        print("sum of 4 multiples and 3 multiples from 1 to m:", sum)
        return a(m)
    return inner

@Mo

def a(m):
    print(" ")
a(100)


     
