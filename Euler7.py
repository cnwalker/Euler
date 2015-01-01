from math import sqrt

def isPrime(num):
    #Returns true if input value is a prime number
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeAt(n):
    #Returns the nth prime number
    pNum = 1; x = 1
    while pNum <= n:
        if isPrime(x):
            pNum += 1
        x += 1
    return x - 1
