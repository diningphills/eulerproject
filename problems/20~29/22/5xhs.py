def read_names(filename):
	f = open(filename, 'r')
	names = f.readline().split(",")
	f.close()
	return names


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




#먼저 모든 이름을 알파벳 순으로 정렬합니다.
#각 이름에 대해서, 그 이름을 이루는 알파벳에 해당하는 숫자(A=1, B=2, ..., Z=26)를 모두 더합니다.
#여기에 이 이름의 순번을 곱합니다.

names = read_names("names.txt")
names.sort()

result = 0
cnt = 1

for name in names :
	result += ( cnt * how_many_points(name) )
	cnt += 1

print(result)

