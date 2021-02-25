from aocd import submit

#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day7.txt')
#os.system('aocd 7 2020 >> day7.txt')
#--------------------------------------------------------------

def unique_colors(target_bag, d, lines, seen):
	count = 0
	for line in lines:
		this_bag, other_bags = line.split(" contain ")
		for bag in other_bags.split(", "):
			if target_bag in bag:
				seen.add(this_bag)
				seen |= unique_colors(this_bag[:-1], d, lines, seen)
				count += 1
	return seen
# find three values that sum to 2020 and print their product
def number_of(stack, d, lines, count):
	total = 0
	while len(stack) > 0:
		find = stack.pop()

		if "shiny gold bag" not in find:
			print(find, total, int(find.split()[0]))
			total += int(find.split()[0])
		for line in lines:
			this_bag, other_bags = line.split(" contain ")
			if ' '.join(find.strip('.').strip('s').strip().split()[1:]) in this_bag:
				n = 1
				if "shiny gold bag" not in find:
					n = int(find.split()[0])

				for bag in other_bags.split(", "):
					if "no other" in bag:
						continue
					#print(bag)
					count += int(bag.split()[0]) * n
					stack.append(f"{int(bag.split()[0]) * n} {' '.join(bag.split()[1:])}")
					print(stack)
					
	return total

# ---- simple cubic O(n^3) time complexity / constant O(1) space complexity algorithm ----
def solve(lines):

	d = dict()
	for line in lines:
		this_bag, other_bags = line.split(" contain ")
		d[this_bag] = [bag for bag in other_bags.split(", ")]
	return number_of(["shiny gold bag"], d, lines, 0)
	return len(unique_colors("shiny gold bag", d, lines, set()))

if __name__ == '__main__':
	# read in input (get_data() returns string)
	lines = [line.strip() for line in open('day7.txt')]
	#submit(sol1(i))
	#submit(sol1(i), part="a", day=2, year=2020)
	print(solve(lines))
	#submit(solve(lines))