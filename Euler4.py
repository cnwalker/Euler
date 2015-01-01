def isPalindrome(integer):
    #Returns true if given integer is a palindrome
    #Otherwise returns false
    i = 0
    integer = str(integer)
    end = len(integer)
    while i < end:
        if i >= end - (i + 1):
            return True
        if integer[i] != integer[end - (i + 1)]:
            return False
        i += 1

def PalinGen(digits):
    #Returns largest palindromal product of the given number of digits
    minVal = 10**(digits - 1)
    maxVal = int(reduce(lambda x, y: x + y, ['9']*digits)) + 1
    for i in range(minVal, maxVal):
        for p in range(minVal, maxVal):
            if isPalindrome(i * p):
                yield i * p

def getMaxPalindrome(digits):
    return max(PalinGen(digits))
