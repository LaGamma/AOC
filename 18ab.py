def compute(lines, precedence=None):
	summate = 0
	for line in lines:
		operands = []
		operators = []
		for c in line:
			#print(c, operators, operands)
			if c == ' ':
				continue
			elif c == '(':
				operators.append(c)
			elif c == ')':
				op = operators.pop()
				while op != '(':
					n1 = operands.pop()
					n2 = operands.pop()
					if op == '+':
						operands.append(n1 + n2)
					elif op == '*':
						operands.append(n1 * n2)
					op = operators.pop()
			elif c == '+':
				if precedence is None:
					while len(operators) > 0 and operators[-1] not in ('(',')'):
						op = operators.pop()
						n1 = operands.pop()
						n2 = operands.pop()
						if op == '+':
							operands.append(n1 + n2)
						elif op == '*':
							operands.append(n1 * n2)
				elif precedence == '*':
					while len(operators) > 0 and operators[-1] == '*':
						op = operators.pop()
						n1 = operands.pop()
						n2 = operands.pop()
						operands.append(n1 * n2)
				operators.append(c)
			elif c == '*':
				if precedence is None:
					while len(operators) > 0 and operators[-1] not in ('(',')'):
						op = operators.pop()
						n1 = operands.pop()
						n2 = operands.pop()
						if op == '+':
							operands.append(n1 + n2)
						elif op == '*':
							operands.append(n1 * n2)
				elif precedence == '+':
					while len(operators) > 0 and operators[-1] == '+':
						op = operators.pop()
						n1 = operands.pop()
						n2 = operands.pop()
						operands.append(n1 + n2)
				operators.append(c)
			else:
				operands.append(int(c))
		
		while len(operators) > 0:
			op = operators.pop()
			n1 = operands.pop()
			n2 = operands.pop()
			if op == '+':
				operands.append(n1 + n2)
			elif op == '*':
				operands.append(n1 * n2)
				
		summate += operands[-1]
	return summate

if __name__ == '__main__':
	# read in input
	lines = [line.strip() for line in open('day18.txt')]
	assert compute(['1 + 2 * 3 + 4 * 5 + 6']) == 71
	assert compute(['1 + (2 * 3) + (4 * (5 + 6))']) == 51
	assert compute(['2 * 3 + (4 * 5)']) == 26
	assert compute(['5 + (8 * 3 + 9 + 3 * 4 * 3)']) == 437
	assert compute(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']) == 12240
	assert compute(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 13632
	print(compute(lines))
	assert compute(['1 + 2 * 3 + 4 * 5 + 6'], precedence='+') == 231
	assert compute(['1 + (2 * 3) + (4 * (5 + 6))'], precedence='+') == 51
	assert compute(['2 * 3 + (4 * 5)'], precedence='+') == 46
	assert compute(['5 + (8 * 3 + 9 + 3 * 4 * 3)'], precedence='+') == 1445
	assert compute(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'], precedence='+') == 669060
	assert compute(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'], precedence='+') == 23340
	print(compute(lines, precedence='+'))