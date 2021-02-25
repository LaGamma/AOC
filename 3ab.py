# ---- simple linear O(n) time complexity / constant O(1) space complexity algorithm ----
def solve(mapp, flag):
	slopes = [3]
	if flag == 'b':
		slopes.extend([1,5,7,0.5])

	col, row, count, prod = 0, 0, 0, 1
	for slope in slopes:

		col, row, count = 0, 0, 0
		while row < len(mapp):

			if mapp[row][col] == '#':
				count += 1

			# if slope is fractional then find the next whole number ratio
			while (col + slope) != int(col + slope):
				col += slope
				row += 1

			# circular wrapping since map repeats infinitely
			col = int(col + slope) % len(mapp[0])
			row += 1

		prod *= count
		print(f"slope: {slope}, trees encountered: {count}, current_product: {prod}")

	return prod if flag == 'b' else count


if __name__ == '__main__':
	# read in input, strip new lines at ends
	lines = [line.strip() for line in open('day3.txt')]
	print(f"\nPart a: {solve(lines, 'a')} total trees encountered\n")
	print(f"\nPart b: product of slopes == {solve(lines, 'b')}\n")