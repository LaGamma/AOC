from aocd import submit

def masked(num, mask):
	for x in range(len(mask)):
		idx = -x - 1
		if mask[idx] == 'X':
			continue
		power = 2 ** x
		if idx < -len(num):
			if mask[idx] == '1':
				num = int(num, 2)
				num += power
				num = str(bin(num))[2:]
		else:
			if num[idx] == '1' and mask[idx] == '0':
				num = int(num, 2)
				num -= power
				num = str(bin(num))[2:]
			elif num[idx] == '0' and mask[idx] == '1':
				num = int(num, 2)
				num += power
				num = str(bin(num))[2:]
	return int(num, 2)

def masked_mems(num, mask):
	num = ["0"]*(len(mask)-len(num)) + num
	options = [0]
	static  = 0
	for x in range(len(mask)):
		idx = -x - 1
		power = 2 ** x
		if mask[idx] == 'X':
			options += [x+power for x in options]
		elif mask[idx] == '1' or num[idx] == '1':
			static += power
	return [x+static for x in options]

def solve(lines):
	mask = None
	mem = dict()
	#lines = ["mask = 000000000000000000000000000000X1001X", "mem[42] = 100", "mask = 00000000000000000000000000000000X0XX", "mem[26] = 1"]
	for line in lines:
		op = line.split(' = ')
		if op[0] == "mask":
			mask = op[1]
		else:
			#num = str(bin(int(op[1])))[2:]
			#mem[op[0][4:-1]] = masked(num, mask)
			num = list(str(bin(int(op[0][4:-1])))[2:])
			for m in masked_mems(num, mask):
				mem[m] = int(op[1])

	summate = 0
	for k in mem:
		summate += mem[k]
	return summate

if __name__ == '__main__':
	# read in input (get_data() returns string)
	lines = [line.strip() for line in open('day14.txt')]
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	#print(dp(0))
	print(solve(lines))