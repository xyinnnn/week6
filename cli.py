import logic
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    filename='./logs/tictactoe_{time}.log'.format(time=int(time.time())),
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(filename)s- %(lineno)d  - %(message)s')
logger = logging.getLogger('tictactoe')

if __name__ == '__main__':
	logger.info('game start')
	board = logic.make_empty_board()
	turn = 'X'
	logic.show_board(board)
	while True:
		print('Next turn: ', turn)
		row, col = logic.receive_input(board, turn)
		board[row][col] = turn
		logic.show_board(board)
		turn = logic.change_turn(turn)
		if logic.judge_winner(board):
			logger.info('game finished')
			break
