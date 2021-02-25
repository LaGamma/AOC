# TODO: clean this up a bit maybe
def solve(lines):
	items, allergens = dict(), dict()
	for i in range(len(lines[0])):
		if lines[0][i] == '':
			continue

		entry = lines[0][i].split(' (contains ')
		ingred_list = entry[0].split()
		allerg_list = entry[1].strip(')').split(', ')
		
		for a in allerg_list:
			if a not in allergens:
				allergens[a] = set(ingred_list)
			else:
				allergens[a] &= set(ingred_list)
			
			if len(allergens[a]) == 1:
				x = allergens[a].pop()
				items[x] = a
				for allerg in allergens:
					if x in allergens[allerg]:
						allergens[allerg].remove(x)

	while any(len(allergens[a]) == 1 for a in allergens):
		for a in allergens:
			if len(allergens[a]) == 1:
				x = allergens[a].pop()
				items[x] = a
				for allerg in allergens:
					if x in allergens[allerg]:
						allergens[allerg].remove(x)


	count = 0
	for i in range(len(lines[0])):
		if lines[0][i] == '':
			continue

		entry = lines[0][i].split(' (contains ')
		ingred_list = entry[0].split()
		allerg_list = entry[1].strip(')').split(', ')
	
		for ing in ingred_list:
			if ing not in items:
				#print(ing)
				count += 1

	print(count)
	print(items)
	
	return ",".join(sorted(items, key=lambda x: items[x]))


if __name__ == '__main__':
	# read in input
	lines = [line.split('\n') for line in open('day21.txt').read().split('\n\n')]
	print(solve(lines))