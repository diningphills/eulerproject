import os

def algorithm(nameList, alphabet):
    resultSum = 0
    for idx, name in enumerate(nameList):
        nameSum = 0
        for n in name:
            nameSum += alphabet[n]

        print(idx+1, nameSum)
        resultSum += (idx+1) * nameSum

    return resultSum



alphabet = dict()
alphabet["A"] = 1
alphabet["B"] = 2
alphabet["C"] = 3
alphabet["D"] = 4
alphabet["E"] = 5
alphabet["F"] = 6
alphabet["G"] = 7
alphabet["H"] = 8
alphabet["I"] = 9
alphabet["J"] = 10
alphabet["K"] = 11
alphabet["L"] = 12
alphabet["M"] = 13
alphabet["N"] = 14
alphabet["O"] = 15
alphabet["P"] = 16
alphabet["Q"] = 17
alphabet["R"] = 18
alphabet["S"] = 19
alphabet["T"] = 20
alphabet["U"] = 21
alphabet["V"] = 22
alphabet["W"] = 23
alphabet["X"] = 24
alphabet["Y"] = 25
alphabet["Z"] = 26


f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/22.txt"), "r")
name = list()

while True:
    line = f.readline()
    if not line: break

    name = line.split(",")

name.sort()

print(name)
print(algorithm(name, alphabet))