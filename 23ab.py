from aocd import submit
#-------------------------------Run once!---------------------
# get data from aocd
#import os
#os.system('del day23.txt')
#os.system('aocd 23 2020 >> day23.txt')
#--------------------------------------------------------------
class MyLLNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solveb(cups):
    nodes = {}

    # Build from input
    last_node = None
    for i in cups:
        node = MyLLNode(i)
        nodes[i] = node
        if last_node is not None:
            last_node.right = node
            node.left = last_node
        last_node = node

    # Complete 1 million nodes
    for i in range(len(cups)+1, 1_000_001):
        node = MyLLNode(i)
        nodes[i] = node
        if last_node is not None:
            last_node.right = node
            node.left = last_node
        last_node = node

    # Complete the circle
    ptr = nodes[cups[0]]
    last_node.right = ptr
    ptr.left = last_node

    assert len(nodes) == 1_000_000

    ptr = nodes[cups[0]]
    for i in range(10_000_000):
        if i % 500_000 == 0:
            print(i)
        p_val = ptr.val

        c1 = ptr.right
        c2 = c1.right
        c3 = c2.right

        ptr.right = c3.right
        ptr.right.left = ptr

        d_val = p_val - 1 or 1_000_000
        while d_val in (c1.val, c2.val, c3.val):
            d_val = d_val - 1 or 1_000_000

        d_node = nodes[d_val]

        c3.right = d_node.right
        c3.right.left = c3
        d_node.right = c1
        c1.left = d_node

        ptr = ptr.right

    while ptr.val != 1:
        ptr = ptr.right

    return ptr.right.val * ptr.right.right.val


def solve(cups):
	mini = min(cups)
	maxi = max(cups)
	cur = 0
	last_picked = None
	for i in range(100):
		print(cups[cur], cups)

		cur_label = cups[cur]

		a, b, c = (cups[(cur+i)%len(cups)] for i in range(1,4))
		cups.remove(a)
		cups.remove(b)
		cups.remove(c)

		print(a,b,c)

		destination = cur_label - 1
		while destination == last_picked or destination not in cups:
			if destination <= mini:
				destination = maxi
			else:
				destination -= 1
		last_picked = destination
		dest_index = cups.index(destination)
		if dest_index == len(cups)-1:
			cups.extend([a,b,c])
		else:
			cups.insert((dest_index+1) % len(cups), c)
			cups.insert((dest_index+1) % len(cups), b)
			cups.insert((dest_index+1) % len(cups), a)

		print(destination, dest_index)

		cur = (cups.index(cur_label) + 1) % len(cups)
	
	j = (cups.index(1)+1) % len(cups)
	while cups[j] != 1:
		print(cups[j], end='')
		j = (j+1) % len(cups)

		

		

if __name__ == '__main__':
	# read in input
	cups = list(map(int, open('day23.txt').read().strip()))
	#cups = list(map(int, list("389125467")))
	print(solveb(cups))