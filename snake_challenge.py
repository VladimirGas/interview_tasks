import numpy as np


def moveOnce(board, snake):
	possibilites = []

	#possible horizonal moves and vertical moves
	hm = [1,0,-1,0]
	vm = [0,1,0,-1]

	snake = snake[:-1]

	for i in range(len(hm)):

		#checking validity of every possible 'new head'
		nh = [snake[0][0]+hm[i],snake[0][1]+vm[i]]
		if (nh not in snake) and (nh[0]<=board[0]) and (nh[1]<=board[1]) and (nh[0]>=0) and (nh[1]>=0):
			possibilites.append([nh]+snake)

	return possibilites


def moveSnakes(board, snakes):
	new_snakes = []
	for snake in snakes:
		new_snakes.extend(moveOnce(board,snake))

	return new_snakes


def numberOfAvailableDifferentPaths(board,snake,depth):
	board = [x-1 for x in board]
	snakes = [snake]

	for _ in range(depth):
		snakes = moveSnakes(board, snakes)

	return len(snakes)




#Testing

test_dict = {
	'board':[[4,3],[2,3],[10,10]],
	'snake':[
		[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],
		[[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]],
		[[5,5], [5,4], [4,4], [4,5]]
	],
	'depth':[3,10,4],
	'result':[7,1,81]
}


for i in range(len(test_dict['board'])):
	print(f"Test no.{i+1}:")
	if numberOfAvailableDifferentPaths(test_dict['board'][i],test_dict['snake'][i],test_dict['depth'][i]) == test_dict['result'][i]:
		print('correct')
	else:
		print('incorrect')
	


#print(numberOfAvailableDifferentPaths(board,snake,3))
