from aocd import submit
from copy import deepcopy
#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day11.txt')
#os.system('aocd 11 2020 >> day11.txt')
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

def solve(lines):
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
					if 0 <= i+d[0] < len(lines) and 0 <= j+d[1] < len(lines[i]):
						if prev_state[i+d[0]][j+d[1]] == '#':
							count += 1
				if count == 0 and prev_state[i][j] == 'L':
					next_state[i][j] = '#'
					changes += 1
				elif count > 3 and prev_state[i][j] == '#':
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



if __name__ == '__main__':
	# read in input (get_data() returns string)
	lines = [[x for x in line.strip()] for line in open('day11.txt')]
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	#print(dp(0))
	print(solveb(lines))