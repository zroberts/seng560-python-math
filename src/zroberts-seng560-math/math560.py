# TODO - raise an exception in add/subtract/multiply/divide if a/b are not ints


def addition(a, b):
    return a + b
    
def sumList(items):
    if(type(items) is not list):
        raise Exception("List not provided")
    total = 0
    for i in items:
        total += i
    return total

def subtract(a,b):
    return a - b

def subtractList(items):
    if(type(items) is not list):
        raise Exception("List not provided")
    total = items[0]
    for i in items[1:]:
        total -= i
    return total

def multiply(a, b):
    return a * b

def multiplyList(items):
    if(type(items) is not list):
        raise Exception("List not provided")
    total = items[0]
    for i in items[1:]:
        total *= i
    return total

def divide(a, b):
    return a / b

def squareRoot(x):
    if x is 0 or x is 1:
        return x

    i = 1; result = 1
    while result <= x:
        i += 1
        result = i * i
    return i -1

    # TODO - Find the square root

def exponent(a,expon):
    # TODO - raise to the power of
    total = a; i = 1
    while i < expon:
        total *= a
    return total


def convertToBinary(x):
    # TODO - conver to binary
    if type(x) is not int:
        raise Exception("Int not provided")

    binNum = [0] * x   
    i = 0
    while(x > 0):
        binNum[i] = x % 2
        x = int(x / 2)
        i += 1
    returnString = ""
    for j in range (i - 1, -1 -1):
        returnString += binNum[j]

    return returnString
        

def convertToHex(x):
    # TODO - convert to hex
    if type(x) is not int:
        raise Exception("Int not provided")
    
    hexaNum = ['0'] * 100
    i = 0
    while (x != 0):
        temp = 0
        temp = x % 16
        if(temp < 10):
            hexaNum[i] = chr(temp + 48)
        else:
            hexaNum[i] = chr(temp + 55)
        i = i + 1
        n = int(n /16)

    j = i - 1
    returnString = ""
    while (j >= 0):
        returnString += hexaNum[j]
    
    return returnString

def converToOct(x):
    # TODO - convert value to Octal
    if type(x) is not int:
        raise Exception("Int not provided")
    
    octalNum = [0] * 100

    i = 0
    while x != 0:
        octalNum[i] = x % 8
        x = int (x / 8)
        i += 1
    
    returnString = ""
    for j in range (i -1, -1, -1):
        returnString += octalNum[j]

    return returnString


def convertToInt():
    # TODO - convert value to INT
    return "" 
