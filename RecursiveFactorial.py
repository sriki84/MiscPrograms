def iterative_factorial(n):
    res = 1
    for i in range(2,n+1):
        print(i)
        res *= i
    return res

print(iterative_factorial(5))

def recursive_fact(n):
    if(n==1):
        return n
    else:
        temp = recursive_fact(n-1)
        print(temp,n)
        return temp*n

print(recursive_fact(0))
