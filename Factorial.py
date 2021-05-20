#Factorial
def factorial(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

if __name__=="__main__":
    fac = factorial(0)
    print(fac)


