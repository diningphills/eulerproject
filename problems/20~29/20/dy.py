def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

n = factorial(100)

moduler = 10
digitSum = 0

while True:
    digitSum += n%moduler
    n = n/moduler
    if n<moduler:
        digitSum += n
        break

print(digitSum)