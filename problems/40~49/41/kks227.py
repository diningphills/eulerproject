import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

used = [False]*9
success = False
val = list("0000000")

def findPrime(pos):
    global used
    global success
    global val
    if success:
        return
    for i in range(7, 0, -1):
        if used[i]:
            continue
        used[i] = True
        val[pos] = chr(ord('0')+i)
        if pos < 6:
            findPrime(pos+1)
        elif isPrime(int("".join(val))):
            print("".join(val))
            success = True
        if success:
            return
        used[i] = False

findPrime(0)
            