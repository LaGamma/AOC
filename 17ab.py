# from itertools import product:
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

# generate all neighbors around a N-dimensional point
def neighbors(point):
    N = len(point)
    for rel_idx in product((-1, 0, 1), repeat=N):
        if not all(i == 0 for i in rel_idx):
            yield tuple(i + i_rel for i, i_rel in zip(point, rel_idx))

def run(initial_state, cycles, extra_dim=[]):
    # length and width of the initial x,y slice
    length, width = len(initial_state[0]), len(initial_state)
    # set of initially active points in the x,y slice
    active = {tuple([x,y]+extra_dim) for x,y in product(range(length), range(width)) if initial_state[x][y] == '#'}

    for _ in range(cycles):

        next_gen = set()
        for idxs in product(range(-cycles, length+cycles), repeat=len(extra_dim)+2):

            pt = tuple(idxs)
            count = sum(neighbor in active for neighbor in neighbors(pt))

            # set next gen
            if count == 3:
                next_gen.add(pt)
            elif count == 2 and pt in active:
                next_gen.add(pt)
        
        active = next_gen

    return len(next_gen)

if __name__ == '__main__':
    # read in input
    initial_state = [[x for x in line.strip()] for line in open('day17.txt')]
    cycles = 6
    #initial_state = [[".","#","."], [".",".","#"], ["#","#","#"]]
    print(f"3-Dimensions, 6 Cycles, Active States: {run(initial_state, cycles, extra_dim=[0])}")
    print(f"4-Dimensions, 6 Cycles, Active States: {run(initial_state, cycles, extra_dim=[0,0])}")