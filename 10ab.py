from aocd import submit
#Ronan Lee, Jack Esposito
#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day10.txt')
#os.system('aocd 10 2020 >> day10.txt')
#--------------------------------------------------------------

# ---- simple cubic O(n^3) time complexity / constant O(1) space complexity algorithm ----
DP = {}
lines = [0]
lines.extend(sorted([int(line.strip()) for line in open('day10.txt')]))
lines.append(max(lines)+3)
def dp(i):
	if i == len(lines)-1:
		return 1
	if i in DP:
		return DP[i]

	ans = 0
	for j in range(i+1, len(lines)):
		if lines[j] - lines[i] <= 3:
			ans += dp(j)
	
	DP[i] = ans
	return ans

def solve(lines):
	nums = set(lines)
	ways = [0 for i in range(len(lines))]
	diffs = [0, 0, 0]
	cur = 0
	while len(nums) > 0:
		p = 0
		for i in (1,2,3):
			if cur+i in nums:
				p += 1
				nums.remove(cur+i)
				diffs[i-1] += 1
				cur = cur+i
				break
				
	parta = diffs[0], (diffs[2] + 1)
	return sum(ways)

	partb = diffs 

	
	preamble_size = 25
	nums = set()
	for i in range(len(lines)):
		found = False
		if len(nums) < preamble_size:
			nums.add(int(lines[i]))
		else:
			for n in lines[i-25:i]:
				for m in lines[i-25:i]:
					n, m = int(n), int(m)
					if n != m and n + m == int(lines[i]):
						found = True
			if not found:
				return int(lines[i])
	return 0
	
	flag = [i for i in range(len(lines)) if lines[i].split()[0] in {"nop", "jmp"}]
	for f in flag:
		acc = 0
		cpu = 0
		all_inst = set()
		while cpu not in all_inst:
			if cpu == len(lines):
				return acc
			all_inst.add(cpu)
			inst = lines[cpu].split()
			print(inst)
			if inst[0] == "nop" and cpu == f:
				cpu += int(inst[1])
				cpu -= 1
			if inst[0] == "acc":
				acc += int(inst[1])
			if inst[0] == "jmp":
				if cpu != f:
					cpu += int(inst[1])
					cpu -= 1
			cpu += 1

	d = dict()
	for line in lines:
		this_bag, other_bags = line.split(" contain ")
		d[this_bag] = [bag for bag in other_bags.split(", ")]
	return number_of(["shiny gold bag"], d, lines, 0)
	return len(unique_colors("shiny gold bag", d, lines, set()))

if __name__ == '__main__':
	# read in input (get_data() returns string)
	#lines = [int(line.strip()) for line in open('day10.txt')]
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	print(dp(0))
	#submit(solve(lines))