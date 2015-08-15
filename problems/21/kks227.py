def d(n):
    result = 0
    for i in range(1, n):
        if n%i==0:
            result += i
    return result

result = 0
s = set(range(1, 10001))
prev = curr = 0
while len(s):
    if prev:
        s.remove(curr)
        temp = d(curr)
        if temp == prev:
            result += prev + curr
            prev = curr = 0
        elif temp not in s:
            prev = curr = 0
        else:
            prev = curr
            curr = temp
    else:
        for prev in s:
            break
        s.remove(prev)
        curr = d(prev)
        if curr not in s:
            prev = curr = 0

print(result)