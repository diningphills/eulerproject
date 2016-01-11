def algorithm(maxA, maxB):
    numbers = dict()

    for a in range(2, maxA+1):
        for b in range(2, maxB+1):
            numbers[pow(a,b)] = 1

    numbersList = numbers.keys()
    numbersList.sort()

    return numbersList


result = algorithm(100, 100)
print(len(result))