

def readfile(filename, adjacentDigits):
    f = open(filename, 'rU')
    number = f.read().replace('\n', '')

    consNum = list(number[0:adjacentDigits])
    #print(consNum)
    product = 1
    maxProduct = 0
    maxList = consNum

    for num in number[adjacentDigits:]:
        for i in consNum:
            product *= int(i)

        if (product > maxProduct):
            maxList = consNum[:]
            maxProduct = product

        #print(product, maxList)

        product = 1
        del consNum[0]
        consNum.append(num)

    #run the condition last time for the last 13 digits
    for i in consNum:
        product *= int(i)

    #print(product, maxList)
    if product > maxProduct:
        maxProduct, maxList = product, consNum

    return maxProduct, maxList

p, l = readfile("eulerp8text.txt",13)
print("Max Product: {}, Numbers: {}".format(p, l))
