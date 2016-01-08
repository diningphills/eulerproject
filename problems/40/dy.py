# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = to_list(n/10)
    result.append(n%10)
    return result

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number

total_list = [0]

for i in range(1, 1000000):
  total_list = total_list + to_list(i)

print len(total_list)
print total_list[1] * total_list[10] * total_list[100] * total_list[1000] * total_list[10000] * total_list[100000] * total_list[1000000]