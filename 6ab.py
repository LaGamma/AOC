# count items in a grouping based on the following criterion:

# Part a: 
#			count the letters that appeared in *at least one line* for each grouping
# Part b: 
#			count the letters that appeared in *all lines* for each grouping

# ---- simple linear O(n) time complexity / constant O(1) space complexity algorithm ----
def solve(lines, part='a'):
	count = 0
	p_count = 0
	d = dict()
	for line in lines:
		if line == '\n':
			if part == 'b':
				# add the # of questions to which everyone in the group said yes
				count += sum(p_count == d[c] for c in d)
			else:
				# add the # of unique questions to which the group said yes
				count += len(d)
			p_count = 0
			d = dict()

		else:
			# add next person's questions in group
			p_count += 1
			for c in line.strip():
				if c in d:
					d[c] += 1
				else:
					d[c] = 1

	# handle last case
	if part == 'b':
		# add the # of questions to which everyone in the group said yes
		count += sum(p_count == d[c] for c in d)
	else:
		# add the # of unique questions to which the group said yes
		count += len(d)
	return count

if __name__ == '__main__':
	# read in input
	lines = [line for line in open('day6.txt')]
	print(f"Part a: total number of questions to which anyone answered \"yes\" == {solve(lines)}")
	print(f"Part b: total number of questions to which everyone answered \"yes\" == {solve(lines, 'b')}")