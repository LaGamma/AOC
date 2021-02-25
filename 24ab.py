def insert(d, d_count):
    opp = {'e': 'w', 'w': 'e', 'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}[d]
    # cancel out opposites
    if d_count[opp] > 0:
        d_count[opp] -= 1
    # nw + e becomes ne, nw + w becomes ne
    elif len(d) == 1 and d_count['n' + opp] > 0:
        d_count['n' + opp]    -= 1
        d_count['n' + d]      += 1
    # sw + e becomes se, sw + w becomes se
    elif len(d) == 1 and d_count['s' + opp] > 0:
        d_count['s' + opp]    -= 1
        d_count['s' + d]      += 1
    # e + xw becomes xe, w + xe becomes xw
    elif len(d) == 2 and d_count[opp[1]] > 0:
        d_count[opp[1]]       -= 1
        d_count[d[0]+opp[1]]  += 1
    # nw + sw becomes w, ne + se becomes e
    elif  len(d) == 2 and d_count[opp[0]+d[1]] > 0:
        d_count[opp[0]+d[1]]  -= 1
        d_count[d[1]]         += 1
    # xw + e becomes xe, xe + w becomes xw
    elif len(d) == 2 and d_count[opp[1]] > 0:
        d_count[opp[1]]       -= 1
        d_count[d[0]+opp[1]]  += 1
    # no substitution was made so simply add
    else:
        d_count[d] += 1
    return d_count

class HexOfLife:

    def __init__(self, lines):
        self.black = set()
        self.directions = {'e', 'w', 'ne', 'nw', 'se', 'sw'}
        
        for line in lines:
            moves = {d: 0 for d in self.directions}
            skip = False
            for i in range(len(line)):
                if skip:
                    skip = False
                    continue

                d = line[i]
                if line[i] in ('n','s'):
                    d += line[i+1]
                    skip = True
                insert(d, moves)

            moves = frozenset(moves.items())
            if moves in self.black:
                self.black.remove(moves)
            else:
                self.black.add(moves)
        
        print(f"Part a: initially {len(self.black)} black tiles")

    def run(self, generations):

        def get_neighbors(tile):
            return [frozenset(insert(dkey, dict(tile)).items()) for dkey in self.directions]


        for _ in range(generations):

            next_gen_black = set()
            for tile in self.black:
               
                cur_count = 0
                for neighbor in get_neighbors(tile):

                    if neighbor not in next_gen_black:
                        # count it's neighbors that are black
                        count = 0
                        for neighneigh in get_neighbors(neighbor):
                            if neighneigh in self.black:
                                count += 1
                        # add to next gen
                        if count == 2 or (count == 1 and neighbor in self.black):
                            next_gen_black.add(neighbor)

                    if neighbor in self.black:
                        cur_count += 1
                
                # add to next gen
                if cur_count in (1,2) and tile not in next_gen_black:
                    next_gen_black.add(tile)

            self.black = next_gen_black

        print(f"Part b: {len(self.black)} black tiles after {generations} generations")


if __name__ == '__main__':
    # read in input
    lines = open('day24.txt').read().strip().split()
    # run simulation
    HexOfLife(lines).run(100)