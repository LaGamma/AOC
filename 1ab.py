from timeit import default_timer as timer
from tqdm import tqdm

################ Part a: find two values that sum to 2020 and print their product ################

# ---- simple quadratic O(n^2) time complexity / constant O(1) space complexity algorithm ----
def sol1a(nums):
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			a, b = nums[i], nums[j]
			if a + b == 2020:
				return a, b
# ---- linear O(n) time complexity / linear O(n) space complexity algorithm using hashsets ----
def sol2a(nums):
	nums = set(nums)
	for a in nums:
		b = 2020 - a
		if b in nums:
			return a, b


################ Part b: find three values that sum to 2020 and print their product ###############

# ---- simple cubic O(n^3) time complexity / constant O(1) space complexity algorithm ----
def sol1b(nums):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			for k in range(j+1, len(nums)):
				a, b, c = nums[i], nums[j], nums[k]
				if a + b + c == 2020:
					return a, b, c
# ---- quadratic O(n^2) time complexity / linear O(n) space complexity algorithm using hashsets ----
def sol2b(nums):
	numset = set(nums)
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			a, b, c = nums[i], nums[j], 2020 - nums[i] - nums[j]
			if c in numset:
				return a, b, c

if __name__ == '__main__':
	# read in input
	nums = [int(x) for x in open('day1.txt')]
	# check that algorithms produce same result
	a,b = sol1a(nums)
	c,d = sol2a(nums)
	assert a*b == c*d
	print(f"{a} + {b} == 2020,")
	print(f"{a} * {b} == {a * b}\n")

	a,b,c = sol1b(nums)
	d,e,f = sol2b(nums)
	assert a*b*c == d*e*f
	print(f"{a} + {b} + {c} == 2020,")
	print(f"{a} * {b} * {c} == {a * b * c}\n")


	# run timing test
	def test_time():
		func_timings = {sol1a:0, sol2a:0, sol1b:0, sol2b:0}
		repeat = 50
		for i in tqdm(range(repeat)):
			for f in func_timings:
				start = timer()
				f(nums)
				end = timer()
				func_timings[f] += end - start
		for f in func_timings:
			func_timings[f] /= repeat
			
		print(f"part a - double loop\t\t\tO(n^2): {func_timings[sol1a]:.8f}")
		print(f"part a - hashset and single loop\tO(n):   {func_timings[sol2a]:.8f}")
		print(f"part b - triple loop\t\t\tO(n^3): {func_timings[sol1b]:.8f}")
		print(f"part b - hashset and double loop\tO(n^2): {func_timings[sol2b]:.8f}")

	test_time()