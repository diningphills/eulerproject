# Test until 6 digit

def getDigits(n):
    digitList = []

    while True:
        digitList.append(n%10)
        if n < 10:
            break
        else:
            n = n/10

    return digitList

resultNumbers = []

for n in range(2, 1000000):
    digitList = getDigits(n)
    localSum = 0
    for d in digitList:
        localSum += pow(d,5)

    if localSum == n:
        resultNumbers.append(n)

print(resultNumbers)
print(sum(resultNumbers))