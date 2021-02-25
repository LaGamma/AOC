""" 
Validate passports to ensure they contain the following fields:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)

    cid (Country ID) -- (doesn't need to be checked)

"""
def strict_validate(d):
	# byr (Birth Year) - four digits; at least 1920 and at most 2002.
	if 1920 <= int(d['byr']) <= 2002:
		# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
		if 2010 <= int(d['iyr']) <= 2020:
			# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
			if 2020 <= int(d['eyr']) <= 2030:
				# hgt (Height) - a number followed by either cm or in:
        			# If cm, the number must be at least 150 and at most 193.
        			# If in, the number must be at least 59 and at most 76.
				if (d['hgt'][-2:] == 'cm' and 150 <= int(d['hgt'][:-2]) <= 193) or (d['hgt'][-2:] == 'in' and 59 <= int(d['hgt'][:-2]) <= 76):
					# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
					if d['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
						# pid (Passport ID) - a nine-digit number, including leading zeroes.
						if len(d['pid']) == 9 and d['pid'].isdigit():
							# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
							if len(d['hcl']) == 7 and d['hcl'][0] == '#':
								try:
									# base-16 check
									int(d['hcl'][1:], 16)
									# passed every check
									return True
								except:
									pass
	return False

# ---- simple linear O(n) time complexity / linear O(n) space complexity algorithm ----
def validate(passports, strict=False):
	def _check(d):
		if all(tag in d for tag in ('ecl', 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid')):
			if not strict or strict_validate(d):
				return True	
		return False					
	
	count = 0
	d = dict()
	for line in lines:
		if line == '\n':
			# validate passport and start processing the next one
			count += _check(d)
			d = dict()
		else:
			# continue building on most recent passport
			for data in line.strip().split():
				k, v = data.split(':')
				d[k] = v
	# validate final passport
	count += _check(d)
	return count

if __name__ == '__main__':
	# read in input
	lines = [line for line in open('day4.txt')]
	print(f'Part a (weak validation):   found {validate(lines)} passports valid')
	print(f'Part b (strict validation): found {validate(lines, strict=True)} passports valid')