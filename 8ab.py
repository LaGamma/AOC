# Part a: step through the program until you execute the same instruction twice 
# 		---- linear O(n) time complexity / constant O(1) space complexity algorithm ----
# Part b: step through the program (swapping a nop with jmp or jmp with a nop) until you find the end of the program
#		---- quadratic O(n^2) time complexity / linear O(n) space complexity algorithm ----
def compute(lines, halt=True):
	swappable = [i for i in range(len(lines)) if lines[i].split()[0] in {"nop", "jmp"}]
	# re-run program with different swapped instruction
	for swap in swappable:
		acc, cpu, all_inst = 0, 0, set()

		# stop when detect infinite loop
		while cpu not in all_inst:
			
			# completed program
			if cpu == len(lines):
				return cpu, lines[swap], acc
			
			# process instruction
			all_inst.add(cpu)
			inst = lines[cpu].split()
			if inst[0] == "acc":
				acc += int(inst[1])
			elif inst[0] == "nop" and cpu == swap or inst[0] == "jmp" and cpu != swap:
				cpu += int(inst[1]) - 1
			cpu += 1

		if halt:
			return acc

if __name__ == '__main__':
	# read in input
	lines = [line.strip() for line in open('day8.txt')]
	# Part a
	acc1 = compute(lines)
	# Part b
	i, inst, acc2 = compute(lines, halt=False)
	print(f"\nFirst repeat instruction found:\n\t- halted with accumulator == {acc1}\n")
	print(f"Program completed after swapping instruction {i} ({inst}):\n\t- completed with accumulator == {acc2}\n")