from collections import deque

# WAR CARD GAME (luck based game - can't be a competitive coin flipper)
# this solution has been extended to allow for any number of N players (handles arbitrary number of decks as input)
# input expects any iterable of iterables of integers (ex. list(list(int)) representing each players deck of cards where cards should be non-negative integers
# output is a tuple representing the winner and their score
def play(decks, recursive = False):
	# exit on receipt of any negative inputs
	if (any(any(c < 0 for c in d) for d in decks)):
		return "Cannot use negative numbers in deck", None

	# copy mem
	decks = [deque(d) for d in decks]
	prev_states = set()

	while sum(len(d) > 0 for d in decks) > 1:
		# check which top card is larger
		top = [d.popleft() if len(d) > 0 else -1 for d in decks]
		winner = top.index(max(top))

		if recursive:
			# track state history
			state = tuple(tuple(d) for d in decks)
			if state in prev_states:
				# prevent infinite recursive loop: p1 wins (score ignored)
				return 0, None
			prev_states.add(state)
			# check if recursive match should be played
			if all(top[i] <= len(decks[i]) for i in range(len(decks))):
				winner = play([tuple(decks[i])[:top[i]] for i in range(len(decks))], recursive=True)[0]
			
		# place winner's card (and then opponent's card(s)) at bottom of winner's deck
		decks[winner].append(top.pop(winner))
		decks[winner].extend([i for i in top if i != -1])

	# check if more players are still in the game
	won = None
	for i in range(len(decks)):
		if len(decks[i]) > 0:
			won = i
	return won, sum(decks[won][-(i+1)]*(i+1) for i in range(len(decks[won])))
	


if __name__ == '__main__':
	# test extra deck
	#start_decks = ((2,5,7),(8,4,6),(9,1,3))
	#print(play(start_decks))
	#print(play(start_decks, recursive=True))

	# tests
	start_decks = ((9,2,6,3,1),(5,8,4,7,10))
	assert play(start_decks) == (1, 306)
	assert play(start_decks, recursive=True) == (1, 291)

	# read in input decks
	start_decks = [list(map(int, line.split('\n')[1:])) for line in open('day22.txt').read().strip().split('\n\n')]

	winner, score = play(start_decks)
	print(f"Part a: p{winner+1} wins with score: {score}")
	
	winner, score = play(start_decks, recursive=True)
	print(f"Part b: p{winner+1} wins with score: {score}")