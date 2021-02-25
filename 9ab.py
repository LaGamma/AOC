# ---- quadratic O(n^3) time complexity / linear O(1) space complexity algorithm ----
def find_XMAS_encryption_weakness(lines, target):

	for start in range(len(lines)):
		for stop in range(start+1, len(lines)):
			summ = sum(lines[start:stop])
			# short circuit to next start if we pass sum
			if summ > lines[target]:
				break
			# found sum sequence
			if summ == lines[target]:
				maxx = max(lines[start:stop])
				minn = min(lines[start:stop])
				print(f"\nPart b: sum sequence found...\n\tsmallest ({minn}) + largest ({maxx}) == {maxx + minn}\n")
				return maxx + minn


# ---- linear O(n*25*25) time complexity / constant O(25) space complexity algorithm ----
def find_invalid_num(lines):
	nums = set(lines[0:25])

	for i in range(25, len(lines)):
		found = False
		for a in nums:
			for b in nums:
				if a != b and a + b == lines[i]:
					found = True
		
		if not found:
			print(f"\nPart a: invalid number found...\n\tcannot sum any pair of the previous 25 numbers to make {lines[i]}")
			find_XMAS_encryption_weakness(lines, i)
			# could continue to find the rest of the weaknesses, but for now let's stop here
			return lines[i]
		else:
			# shift sliding window
			nums.remove(lines[i-25])
			nums.add(lines[i])

if __name__ == '__main__':
	# read in input
	lines = [int(line.strip()) for line in open('day9.txt')]
	# solve
	find_invalid_num(lines)