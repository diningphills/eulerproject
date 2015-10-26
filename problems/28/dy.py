def algorithm(n):
    if n%2 == 0:    return False

    iterate = (n-1)/2

    current = 1
    totalSum = current

    print("n: " + str(iterate))
    
    for i in range(1, iterate+1):
        for _ in range(0, 4):
            current = current + 2*i
            totalSum += current

    return totalSum


result = algorithm(1001)
print(result)