def getFact(number, factor, factNum):
    #Helper function, 
    if number == 0:
        return 0
    if number%factor != 0:
        return factNum
    else:
        factNum += 1
        return getFact(number/factor, factor, factNum)

def getDiv(limit):
    #Returns smallest number divisible by every number
    #Between 0 and the limit
    divisible = False
    LCM = 1
    primeList = []
    PrimeDict = {}
    for i in range(2, limit + 1):
        for x in range(2, limit):
            if i%x == 0 and x != i:
                divisible = True
        if divisible == False:
            primeList.append(i)
        else:
            divisible = False
    for i in range(0, len(primeList)):
        curList = []
        for x in range(1, limit + 1):
            curList.append(getFact(x, primeList[i], 0))
        PrimeDict[primeList[i]] = curList
    for i in range(0, len(PrimeDict)):
        LCM = LCM*(primeList[i]**(max(PrimeDict[primeList[i]])))
    return LCM
                   
