from aocd import submit
from copy import deepcopy
import math
#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day12.txt')
#os.system('aocd 12 2020 >> day12.txt')
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
	#lines = ['F10', 'N3', 'F7', 'R90', 'F11']
	waypoint = [10, 1]
	position = [0,0]
	angle = 0
	for line in lines:
		op = line[0]
		dist = int(line[1:])

		if op == 'F':
			#position[0] += dist*math.cos(math.radians(angle))
			#position[1] += dist*math.sin(math.radians(angle))
			position[0] += waypoint[0]*dist
			position[1] +=  waypoint[1]*dist
		elif op == 'L':
			#angle = (angle + dist) % 360
			if dist == 180:
				waypoint[0] *= -1
				waypoint[1] *= -1
			elif dist == 90:
				waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
			elif dist == 270:
				waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
		elif op == 'R':
			#angle = (angle - dist) % 360
			if dist == 180:
				waypoint[0] *= -1
				waypoint[1] *= -1
			elif dist == 90:
				waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
			elif dist == 270:
				waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
		elif op == 'N':
			#position[1] += dist
			waypoint[1] += dist
		elif op == 'S':
			#position[1] -= dist
			waypoint[1] -= dist
		elif op == 'E':
			#position[0] += dist
			waypoint[0] += dist
		elif op == 'W':
			#position[0] -= dist
			waypoint[0] -= dist
		print(position, waypoint)
	return round(abs(position[0])) + round(abs(position[1]))

if __name__ == '__main__':
	# read in input (get_data() returns string)
	lines = [line.strip() for line in open('day12.txt')]
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	#print(dp(0))
	print(solve(lines))