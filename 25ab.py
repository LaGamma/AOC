def crack(nums):

	secret_loop_sizes = []

	for public_key in nums:

		loop_size = 0
		n = 1
		while n != public_key:
			n *= 7
			n %= 20201227
			loop_size += 1

		secret_loop_sizes.append(loop_size)


	encryption_key = 1
	for _ in range(secret_loop_sizes[0]):
		encryption_key *= nums[1]
		encryption_key %= 20201227

	return encryption_key

if __name__ == '__main__':
	# test
	assert crack([5764801, 17807724]) == 14897079
	# read in input
	nums = [int(n) for n in open('day25.txt').read().strip().split()]
	print(crack(nums))