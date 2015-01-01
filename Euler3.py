import time
from math import sqrt

def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def greatestPrimeFactor(num):
    for i in range(1, num):
        if num % i == 0:
            curVal = int(num/i)
            if isPrime(curVal):
                return curVal
