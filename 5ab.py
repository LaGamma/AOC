# find max seat ID and missing seat ID based on binary space partitioning algorithm
# ---- simple constant O(128log128) time complexity / constant O(128) space complexity algorithm ----
def solve(lines):
	all_seats = []
	for line in lines:
		# convert binary strings to int
		row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
		col = int(line[7:].replace('R', '1').replace('L', '0'), 2)
		all_seats.append(row * 8 + col)
	all_seats.sort()
	print(f"Part a: max seat == {all_seats[-1]}")

	for i in range(len(all_seats) - 1):
		if (all_seats[i] + 1 != all_seats[i + 1]):
			print(f"Part b: missing seat (your seat) == {all_seats[i] + 1}")

if __name__ == '__main__':
	# read in input
	solve([line.strip() for line in open('day5.txt')])