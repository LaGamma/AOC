# easy O(n) time and O(n?) space solution
def solve(seq, stop):
	mem = {seq[i]: i+1 for i in range(len(seq)-1)}
	i = len(seq)
	cur = seq[-1]

	while i < stop:

		next_cur = 0
		if cur in mem:
			next_cur = i - mem[cur]

		mem[cur] = i

		cur = next_cur
		i += 1

	return cur


if __name__ == '__main__':
	# read in input
	seq = []
	for line in open('day15.txt'):
		seq.extend(map(int, line.strip().split(',')))
	# set up tests
	tests = {(0,3,6): [436, 175594],
			 (1,3,2): [1, 2578],
			 (2,1,3): [10,3544142],
			 (1,2,3): [27, 261214],
			 (2,3,1): [78, 6895259],
			 (3,2,1): [438, 18],
			 (3,1,2): [1836, 362]}
	s = [2020, 30000000]
	# run tests	and solve each part	 
	for i in range(2):
		print(f"Sit tight while we run stop={s[i]} checks...")
		for j, t in enumerate(tests):
			assert solve(t, s[i]) == tests[t][i]
			print(f"{j+1} of 7")
		print(f"Passes all stop={s[i]} checks! Running on main sequence...")
		print(f"Part {('a','b')[i]} solution: {solve(seq, s[i])}\n")