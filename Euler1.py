def euler(limit, fMultNum, sMultNum):
    firstNum = fMultNum
    secondNum = sMultNum
    fSum = fMultNum + sMultNum

    while (firstNum + fMultNum) < limit:
        firstNum = firstNum + fMultNum
        if firstNum%secondNum != 0:
            fSum = fSum + firstNum
        
    while (secondNum  + sMultNum) < limit:
        secondNum = secondNum + sMultNum
        fSum = fSum + secondNum

    return fSum

def recursive(n):
    if n == 20:
        return n
    return recursive(n + 1)

def inFibonacci(a, b, n, maxIter):
    if n == maxIter:
        return a
    c = a
    a = a+b
    return inFibonacci(a, c, n + 1, maxIter)

def fibonacci(maxIter):
    thisNum = inFibonacci(1, 0, 0, maxIter)
    print("This is your number: " + str(thisNum))


    
