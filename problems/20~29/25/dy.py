def digitCount(n):
    count = 1
    while n >= 10:
        count += 1
        n = n/10

    return count

def Fibonacci(F, i):
    if i==0 or i==1:
        return 0
    else:
        newValue = F[i-2] + F[i-1]
        F.append(newValue)



F = [1, 1]

i=2

while True:
    Fibonacci(F, i)
    print(F[i], i)
    if digitCount(F[i]) >= 1000:
        print(i)
        break
    else:
        i += 1