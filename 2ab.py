# count valid passwords according to company policy:

# i.e. given a list of strings in the form "policy char: password" 
# 		does the password contain a number of the characters char that fall within the bounds of the policy
# for example: 
#	1-3 a: abcde		is *valid* because the password contains 1 'a' (between 1 and 3)
#	1-3 b: cdefg		is *invalid* because the password contains 0 b's (not between 1 and 3)
#	2-9 c: ccccccccc	is *valid* because the password contains 9 'c's (between 2 and 9)

# Part b:
# 		does the password contain char at either position of the policy (and not at both positions)

# note: policy indices are 1-based, not 0-based

# for example: 
#	1-3 a: abcde		is *valid* because 'a' exists at index 1 and not at index 3
#	1-3 b: cdefg		is *invalid* because 'b' does not exist at index 1 or 3
#	2-9 c: ccccccccc	is *invalid* because 'c' exists at both indices 2 and 9

# ---- Part a:   O(lines * len(password)) time complexity / constant O(1) space complexity ----
# ---- Part b:                linear O(n) time complexity / constant O(1) space complexity ----
def validate(lines, part):
	count = 0
	for line in lines:
		# unpack space-separated components
		rule, letter, pw = line.split()
		# unpack bounds from rule
		lower, upper = map(int, rule.split('-'))
		if part == 'a': 
			# count if the number of char falls in the bounds
			count += lower <= pw.count(letter[0]) <= upper
		else:
			# count if either position (1-indexed) contains letter, but not both (xor)
			count += (pw[lower-1] == letter[0]) ^ (pw[upper-1] == letter[0])
	return count

if __name__ == '__main__':
	lines = [line for line in open('day2.txt')]
	print(f"Part a: found {validate(lines, 'a')} valid passwords of {len(lines)}")
	print(f"Part b: found {validate(lines, 'b')} valid passwords of {len(lines)}")