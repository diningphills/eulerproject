def isPalindrome(list):
  for i in range(0, len(list)/2):
    if list[i] != list[-(i+1)]: return False
  return True

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


def int2binList(i):
  if i == 0: return "0"
  s = []
  while i:
    if i & 1 == 1:
      s.append(1)
    else:
      s.append(0)
    i /= 2
  s.reverse()
  return s

def isListPalindrome(n_list):
  for i in range(0, len(n_list)/2):
    if n_list[i] != n_list[-(i+1)]: return False
  return True


print int2binList(102)

answer = set()

for i in range(1, 1000001):
  if isListPalindrome(to_list(i)) and isListPalindrome(int2binList(i)):
    answer.add(i)

print answer
print sum(answer)
