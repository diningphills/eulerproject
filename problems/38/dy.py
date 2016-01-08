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

def isPandigital(n):
  n_list = to_list(n)

  if len(n_list)!=9: return False
  n_set = set(n_list)
  if set([1,2,3,4,5,6,7,8,9]) != n_set: return False
  else: return True


def makePalindrome(n):
  result = []
  for i in range(1, 10):
    result = result + to_list(n*i)
    if len(result)>9: return False
    elif len(result)==9:
      if isPandigital(to_number(result)): return to_number(result)
      else: return False
    else: continue

print makePalindrome(912345678)

answer = set()

for i in range(1, 10000):
  result = makePalindrome(i)
  if not result: continue
  else:
    answer.add(result)

print answer
print max(answer)