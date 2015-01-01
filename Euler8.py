def getProduct(numString):
    #Returns the product of all the digits in a string of numbers
    if '0' in numString:
        return 0
    else:
        curProd = 1
        for cell in numString:
            curProd = (curProd * int(cell))
        return curProd

def parseNumbers(masterString, interval):
    #Prints the consecutive digits with the greatest sum, over
    #the given interval
    curMax = 0
    curBest = ''
    for i in range(0, len(masterString) - 1):
        if len(masterString) < interval:
            print('Product: ' + str(curMax) + '\n' + 'Numbers: ' + curBest)
            return 
        
        outProd = getProduct(masterString[:interval])

        if outProd > curMax:
            curMax = outProd
            curBest = masterString[:interval]

        masterString = masterString[1:]

def Euler(num):
    #Performs parseNumbers over the Euler example num for problem 8
    numset = open('EulerNumbers.txt', 'r')
    numStr = ''.join(numset.read().split())
    parseNumbers(numStr, num)
        
    


