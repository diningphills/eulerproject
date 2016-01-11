def U(n):
	return sum([ (-n) ** i for i in range(11)])
equations = ['1']

op = [ U(i) for i in range(1, 11)]
print (op)
def alpha(equation, current_x):
	x = current_x
	_op = op[current_x - 1]
	terms = equation.split('+')
	for term in terms[1:]:
		_op -= eval(term)
	_op /= eval(terms[0])
	return _op

def nextEquation():
	equation = equations[-1]
	terms = []

	for i in range(1,len(equations)+1):
		terms.append('(x-')
		terms.append(str(i))
		terms.append(')*')
	equations.append('+'.join([''.join(terms)[:-1],equation]))
	#input("New terms")
	#print(equations[-1])
	a = alpha(equations[-1], len(equations))
	equations[-1] = '*'.join([str(a), equations[-1]])
	#print (equations)

for i in range(9):
	nextEquation()
bot = []
for i in range(10):
	x = i + 2
	bot.append(eval(equations[i]))
print (bot)
print (sum(bot))
print (len(equations))
