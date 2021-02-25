from aocd import submit
from copy import deepcopy
import math
#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day13.txt')
#os.system('aocd 13 2020 >> day13.txt')
#--------------------------------------------------------------

# ---- simple cubic O(n^3) time complexity / constant O(1) space complexity algorithm ----
#DP = {}
#lines = [0]
#lines.extend(sorted([int(line.strip()) for line in open('day10.txt')]))
#lines.append(max(lines)+3)

def solveb(lines):
	next_state, prev_state = None, None
	generations = 0
	changes = 1
	while changes != 0:
		changes = 0
		prev_state = deepcopy(lines)
		next_state = deepcopy(lines)
		for i in range(len(lines)):
			for j in range(len(lines[i])):
				if prev_state[i][j] == '.':
					continue
				count = 0
				for d in ((0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)):
					look = [k for k in d]
					while (0 <= i+look[0] < len(lines) and 0 <= j+look[1] < len(lines[i])):
						if prev_state[i+look[0]][j+look[1]] in ('#', 'L'):
							if prev_state[i+look[0]][j+look[1]] == '#':
								count += 1
							break
						look[0] += d[0]
						look[1] += d[1]
				if count == 0 and prev_state[i][j] == 'L':
					next_state[i][j] = '#'
					changes += 1
				elif count > 4 and prev_state[i][j] == '#':
					next_state[i][j] = 'L'
					changes += 1
		generations += 1
		lines = next_state
		print(changes)

	c = 0
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == '#':
				c += 1
	return c

def solve(arrival, times):

	arrival = 939
	times = [7,13,59,31,19]
	print(arrival, times)

	#start = 100000000000001 # 3448275862069 * 29
	start = times[0]*150000
	while True:
		t = 1
		for i in range(1,times[0]):
			checks = [(start + i) % x for x in times]
			#print(checks)
			if checks[t] == 0:
				if t == len(times) - 1:
					print(start)
					break
				if checks[t] == 0:
					t += 1
				if t < len(times) - 1 and 0 in checks[:t] + checks[t+1:]:
					break
		start += times[0]



	#p1
	diff = 99999999
	best = None
	for x in times:
		target = x * 1500
		while target < arrival:
			target += x
		if target - arrival < diff:
			diff = target - arrival
			best = x

	return diff * best

if __name__ == '__main__':
	lines = open('day13.txt').read().split('\n')
	def p(zz):
		z, i = zz
		return int(z), int(i)
	
	x = int(lines[0])
	v = list(map(p, filter(lambda z : z[1] != 'x', enumerate(lines[1].split(',')))))
	print(v)

	for i, z in v:
		#print(z, i)
		i = -i
		while i < 0:
			i += z
		print('x = {} mod {}'.format(i, z))
	exit()
	#feed this data to online CRT solver

	
	# read in input (get_data() returns string)
	lines = [line.strip() for line in open('day13.txt')]
	arrival = int(lines[0])
	times = [int(t) for t in lines[1].split(',') if t != 'x']
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	#print(dp(0))
	print(solve(arrival, times))