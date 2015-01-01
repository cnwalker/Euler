def evenFibonacci(fib1, fib2, count, maxVal):
    if fib2 >= maxVal:
        return count
    if fib2 % 2 == 0:
        count += fib2
    return evenFibonacci(fib2, fib1 + fib2, count, maxVal) 
    
