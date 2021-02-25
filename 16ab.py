def passes(n, rule):
	if (rule[0] <= n <= rule[1]) or (rule[2] <= n <= rule[3]):
		return True
	return False

if __name__ == '__main__':
	# read in input
	lines = [line.strip() for line in open('day16.txt')]
	
	# process lines to format rules
	rules = dict()
	i = 0
	while lines[i] != '':
		label, rule = (item.strip() for item in lines[i].split(':'))
		rule = rule.split()
		rules[label] = tuple(map(int, rule[0].split('-') + rule[2].split('-')))
		i += 1
	
	# process remaining lines to format your ticket and other tickets
	i += 2
	your_ticket = tuple(int(n) for n in lines[i].split(','))
	i += 3
	tickets = set(tuple(int(n) for n in lines[r].split(',')) for r in range(i, len(lines)))
	
	# filter out impossible tickets
	invalid_sum = 0
	for tic in tuple(tickets):
		for num in tic:
			if not any(passes(num, rules[r]) for r in rules):
				invalid_sum += num
				tickets.remove(tic)
				break
	print("Part a (invalid sum):", invalid_sum)

	# creating initial 1-to-many mapping between ticket position i and the set of possible rules that ticket position i successfully fits in for all tickets
	mapping = dict()
	for i in range(len(rules)):
		mapping[i] = set()
		for rule in rules:
			if all(passes(tic[i], rules[rule]) for tic in tickets):
				mapping[i].add(rule)
	
	# build the final 1-to-1 rule:index mapping from the 1-to-many index:{possibleRules} mapping
	final = dict()
	while len(mapping) > 0:
		for i in tuple(mapping):
			# necessary constraint found
			if len(mapping[i]) == 1:
				val = mapping[i].pop()
				final[val] = i
				# clean up rest of mapping
				del mapping[i]
				for other in mapping:
					if val in mapping[other]:
						mapping[other].remove(val)
				break
	
	# calculate product of departure values on your ticket
	prod = 1
	for rule in final:
		if "departure" == rule[:9]:
			prod *= your_ticket[final[rule]]
	print("Part b (departure product):", prod)