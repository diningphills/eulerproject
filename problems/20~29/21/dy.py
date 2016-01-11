def getDivisors(n):
    list = []
    for i in range(1, n+1):
        if i > n/2:
            break
        if n%i == 0:
            list.append(i)
    return list

sumsOfDivisor = dict()
totalSum = 0

for i in range(1,10001):
    sumsOfDivisor[i] = sum(getDivisors(i))

for k in sumsOfDivisor.keys():
    # if friend number is exist
    if sumsOfDivisor[k] in sumsOfDivisor:
        if sumsOfDivisor[k] != k and sumsOfDivisor[sumsOfDivisor[k]] == k:
            print("key: " + str(k), "sum[key]: " + str(sumsOfDivisor[k]), "sum[sum[key]]: " + str(sumsOfDivisor[sumsOfDivisor[k]]))
            totalSum += k

print(totalSum)