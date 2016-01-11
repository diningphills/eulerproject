# factorial
def factorial(n):
  if n==0 or n==1:  return 1
  else:             return n*factorial(n-1)

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number

# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = to_list(n/10)
    result.append(n%10)
    return result

answer = set()

for n in range(0, 2540161):
  n_list = to_list(n)
  calculate = 0
  for num in n_list:
    calculate += factorial(num)

  if calculate == n: answer.add(n)

print answer
print sum(answer)