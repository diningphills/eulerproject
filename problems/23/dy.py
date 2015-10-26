def getDivisors(n):
    list = []
    for i in range(1, n+1):
        if i > n/2:
            break
        if n%i == 0:
            list.append(i)
    return list

sumOfDivisors = dict()

for i in range(1, 28124):
    sumOfDivisors[i] = sum(getDivisors(i))

overNumbers = list()

for k in sumOfDivisors.keys():
    if sumOfDivisors[k] > k:
        overNumbers.append(k)

sumOfOverNumbers = dict()

for i in range(0, len(overNumbers)):
    for j in range(i, len(overNumbers)):
        if overNumbers[i] + overNumbers[j] <= 28123:
            sumOfOverNumbers[overNumbers[i]+overNumbers[j]] = 1

print(sumOfOverNumbers.keys())

result = sum(range(1,28124)) - sum(sumOfOverNumbers.keys())

print(result)