def permutation(numList):
    if len(numList) == 1:
        return numList

    resultList = []
    for n in numList:
        recursiveList = list(numList)
        recursiveList.remove(n)
        for other in permutation(recursiveList):
            resultList.append(n + other)

    return resultList


numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

result = permutation(numList)

print(result)
print(result[999999])
# 3!