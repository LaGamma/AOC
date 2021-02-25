def orient(tile, degrees):
	out_tile = ''
	for i in range(len(tile)):
		for j in range(len(tile[i])):
			if degrees == 0:
				out_tile += tile[i][j]
			elif degrees == 90:
				out_tile += tile[-(j+1)][i]
			elif degrees == 180:
				out_tile += tile[-(i+1)][-(j+1)]
			elif degrees == 270:
				out_tile += tile[j][-(i+1)]
		out_tile += '\n'
	return out_tile


def process_side_match(tile_id, flipped, unmatched, matched_sides, matches):
	#print('match found',unmatched[flipped[0]], tile_id)
	if flipped[0] not in unmatched and flipped[1] not in unmatched:
		unmatched[flipped[0]] = tile_id
	else:
		flip = False
		if flipped[0] in unmatched:
			flip = True

		side = flipped[(int(flip)+1)%2]
		if unmatched[side] not in matches:
			matches[unmatched[side]] 		= []
			matched_sides[unmatched[side]] 	= []
		if tile_id not in matches:
			matches[tile_id] 		= []
			matched_sides[tile_id] 	= []

		matches[unmatched[side]].append(tile_id)
		matches[tile_id].append(unmatched[side])
		matched_sides[unmatched[side]].append(side)
		matched_sides[tile_id].append(side)

		del unmatched[side]

def decipher(tiles):

	ids, matches, matched_sides, unmatched = dict(), dict(), dict(), dict()
	
	for tile in tiles:
		lines = tile.strip().split('\n')
		tile_id = int(lines[0].split()[1].strip(':'))
		ids[tile_id] = lines[1:]
		
		# check top and bottom edges
		for e in (1,-1):
			flipped = [(lines[e],lines[e][::-1]), (lines[e][::-1],lines[e])]
			process_side_match(tile_id, flipped, unmatched, matched_sides, matches)
		# check left and right edges
		for e in (0,-1):
			string = "".join([lines[i][e] for i in range(1, len(lines))])
			flipped = [(string,string[::-1]), (string[::-1],string)]
			process_side_match(tile_id, flipped, unmatched, matched_sides, matches)

	# by definition, corners are those tiles which have 2 sides unmatched
	corners = []
	side_count = dict()
	for unm in unmatched:
		if unmatched[unm] not in side_count:
			side_count[unmatched[unm]] = 1
		else:
			side_count[unmatched[unm]] += 1
			corners.append(unmatched[unm])

	prod = corners[0] * corners[1] * corners[2] * corners[3]
	print(f"Part a: {corners[0]} * {corners[1]} * {corners[2]} * {corners[3]} == {prod}")

	# --------------------------------------

	used_set = set()
	grid = [[0 for _ in range(12)] for _ in range(12)]

	# build constrained tiling order starting from one corner
	C1 = corners[0]
	C2 = matches[C1][1]
	D1 = matches[C1][0]
	D2 = [x for x in matches[C2] if x != C1 and x in matches[D1]][0]

	for j in range(0, 12, 2):
		Eb, Mb = C1, C2
		Ea, Ma = D1, D2
		grid[0][j], grid[0][j+1] = Eb, Mb
		grid[1][j], grid[1][j+1] = Ea, Ma
		used_set |= {Eb, Mb, Ea, Ma}
		
		for i in range(2, 12, 2):
			Eb = [x for x in matches[Ea] if x not in matches[Mb] and x not in used_set][0]
			Mb = [x for x in matches[Eb] if x in matches[Ma] and x != Ea and x not in used_set][0]
			Ea = [x for x in matches[Eb] if x not in matches[Ma] and x not in used_set][0]
			Ma = [x for x in matches[Ea] if x in matches[Mb] and x != Eb and x not in used_set][0]
			grid[i][j], grid[i][j+1] = Eb, Mb
			grid[i+1][j], grid[i+1][j+1] = Ea, Ma
			used_set |= {Eb, Mb, Ea, Ma}

		if (j < 10):
			C1 = [x for x in matches[C2] if x not in matches[D1]][0]
			D1 = [x for x in matches[D2] if x in matches[C1] and x != C2][0]
			C2 = [x for x in matches[C1] if x not in matches[D2]][0]
			D2 = [x for x in matches[C2] if x in matches[D1] and x != C1][0]

	# print out the ids in their constrained tiling order
	for row in grid:
		for x in row:
			print(x, ' ', end='')
		print()

	full_grid = [['' for _ in range(12)] for _ in range(12)]
	# rotate initial tile left
	full_grid[0][0] = orient(ids[grid[0][0]], 270)
	for i in range(12):
		for j in range(12):
			if i != 0 or j != 0:

				cur = grid[i][j]
				prev = grid[i-1][j] if j == 0 else grid[i][j-1]
				side = [x for x in matched_sides[prev] if x in matched_sides[cur]][0]
				offset = 0 if j != 0 else 90
				# get angle
				angle = 0
				for flip in range(2):
					if side[flip] == ids[cur][0]:
						angle = (270 - offset) % 360
					elif side[flip] == ids[cur][-1]:
						angle = (90 - offset) % 360
					elif side[flip] == ''.join([ids[cur][j][0] for j in range(len(ids[cur]))]):
						angle = (0 - offset) % 360
					elif side[flip] == ''.join([ids[cur][j][-1] for j in range(len(ids[cur]))]):
						angle = (180 - offset) % 360
				puzzle = orient(ids[cur], angle)

				if j != 0 and ''.join([puzzle.split()[x][0] for x in range(len(puzzle.split()))]) != ''.join(full_grid[i][j-1].split()[x][-1] for x in range(len(full_grid[i][j-1].split()))):
					#flip horizontal
					puzzle = '\n'.join([line for line in puzzle.split()[::-1]])

				if i != 0 and puzzle.split()[0] != full_grid[i-1][j].split()[-1]:
					#flip vertical and horizontal
					puzzle = '\n'.join([line[::-1] for line in puzzle.split()[::-1]])
					if puzzle.split()[0] != full_grid[i-1][j].split()[-1]:
						puzzle = '\n'.join([line[::-1] for line in puzzle.split()])

				full_grid[i][j] = puzzle
	
	# print out full tiling with matching edges
	for row in range(12):
		for line in range(10):
			for col in range(12):
				print(full_grid[row][col].split()[line], ' ', end='')
			print()
		print()

	print('\n\n')

	# print out monster map with edges removed
	monster_map = []
	cur = ''
	for row in range(12):
		for line in range(1,9):
			for col in range(12):
				cur += full_grid[row][col].split()[line][1:9]
				print(full_grid[row][col].split()[line][1:9], end='')
			monster_map.append(cur)
			cur = ''
			print()

	print('\n\n')

	monster_map = orient(monster_map, 0).split()
	map_copy = [list(line) for line in monster_map]
	found_monsters = False

	# search for monsters in different map orientations
	for attempt in range(8):
		if attempt == 4:
			monster_map = '\n'.join([line[::-1] for line in monster_map]).split()
			map_copy = [list(line) for line in monster_map]
		
		for row in range(len(monster_map)-2):
			for col in range(len(monster_map[row])-19):
				if monster_map[row][col+18] == '#':
					if all(monster_map[row+1][col+c] == '#' for c in (0,5,6,11,12,17,18,19)):
						if all(monster_map[row+2][col+c] == '#' for c in (1,4,7,10,13,16)):
							
							found_monsters = True
							map_copy = [list(line) for line in map_copy]
							map_copy[row][col+18] = "O"
							for c in (0,5,6,11,12,17,18,19):
								map_copy[row+1][col+c] = "O"
							for c in (1,4,7,10,13,16):
								map_copy[row+2][col+c] = "O"
		
		if found_monsters:
			print(f"found sea monsters in orientation {attempt}:")
			break
		else:
			monster_map = orient(monster_map, 90).split()
			map_copy = [list(line) for line in monster_map]

	# sum all # that are not monsters
	water_roughness = 0
	for line in map_copy:
		print("".join(line))
		water_roughness += "".join(line).count("#")
		
	print(f"Part b: water roughness == {water_roughness}")


if __name__ == '__main__':
	# read in input
	tiles = [tile for tile in open('day20.txt').read().split('\n\n')]
	decipher(tiles)