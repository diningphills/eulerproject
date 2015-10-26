sumOfSquare = 0
squareOfSum = 0

for i in range(1,101):
	sumOfSquare += i**2
	squareOfSum += i

squareOfSum = squareOfSum**2

print("Sum of Square: %d, Square of Sum: %d" %(sumOfSquare, squareOfSum))
result = squareOfSum - sumOfSquare
print("result: %d" %(result))