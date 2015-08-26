import math
import string

def is_trinum(k):
	''' 
		1/2*n*(n+1) = k
		이 이차방정식을 만족시키는 n(자연수)가 존재하면 k는 삼각수이다.
	
		n에 대해 정리하면 판별식 D = 8*k + 1 이 된다. 
		방정식을 만족하는 자연수 n이 존재하려면 8k+1 은 홀수의 제곱이어야 한다.
		그런데 8k+1은 무조건 홀수이므로 8k+1이 제곱수라면 k는 삼각수이다.
	'''
	
	check = math.sqrt(8*k + 1)

	if int(check) != check :
		return False
	else :
		return True


def read_words(filename):
	f = open(filename, 'r')
	words = f.readline().split(",")
	f.close()
	return words


def how_many_points(word):
	# word is actually "word"

	length = len(word)
	point = 0

	for i in range(0, length):
		if word[i] == '\"' :
			continue
		else :
			point += ord(word[i]) - 64

	return point

	

words = read_words("words.txt")
cnt = 0

for word in words:
	if is_trinum(how_many_points(word)) is True:
		cnt += 1

print(cnt)