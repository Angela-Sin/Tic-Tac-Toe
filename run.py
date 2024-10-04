#Tic-Tac-Toe

board_size = 3

board = [1,2,3,4,5,6,7,8,9]



def draw_board():
	print (('_' * 4 * board_size ))
	for i in range(board_size):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)


def start_game():
    draw_board()

print("Welcome to the game")
start_game()