def getDiff(lim):
    #Returns the difference between the square of the sum
    #and the sum of the squares of every number from 0 to
    #the limit
    sumSquare = 0
    squareSum = 0
    for i in range(1, lim + 1):
        sumSquare += i**2
        squareSum += i
    return squareSum**2 - sumSquare

