from typing import List
import logging

logger = logging.getLogger('tictactoe')


def make_empty_board() -> List[List[str]]:
	return [[' ', ' ', ' '], 
		[' ', ' ', ' '], 
		[' ', ' ', ' ']]


def show_board(input_board: List[List[str]]):
	for row in input_board:
		print(row)


def receive_input(input_board: List[List[str]], turn: str) -> (int, int):
	while True:
		row = input("input row index: ")
		col = input("input col index: ")
		if not row.isdigit() or not col.isdigit():
			logger.error('{turn} input invalid: {row},{col}'.format(turn=turn, row=row, col=col))
			print('input invalid, not int')
		elif int(row) < 0 or int(row) > 2 or int(col) < 0 or int(col) > 2:
			logger.error('{turn} input invalid: {row},{col}'.format(turn=turn, row=row, col=col))
			print('input invalid, should >=0 and <=2')
		elif input_board[int(row)][int(col)] != ' ':
			logger.error('{turn} input invalid: {row},{col}'.format(turn=turn, row=row, col=col))
			print('input invalid, index already input')
		else:
			logger.info('received {turn} input: {row},{col}'.format(turn=turn, row=row, col=col))
			return int(row), int(col)


def change_turn(now: str) -> str:
	if now == 'X':
		next = 'Y'
	else:
		next = 'X'
	return next


def judge_winner(input_board: List[List[str]]) -> bool:
	for i in range(0, 3):
		if input_board[i][0] != ' ' and input_board[i][0] == input_board[i][1] == input_board[i][2]:
			logger.info('{turn} won'.format(turn=input_board[i][0]))
			print(input_board[i][0], ' Won')
			return True
	for i in range(0, 3):
		if input_board[0][i] != ' ' and input_board[0][i] == input_board[1][i] == input_board[2][i]:
			logger.info('{turn} won'.format(turn=input_board[0][i]))
			print(input_board[0][i], ' Won')
			return True
	if input_board[1][1] != ' ' and (
			input_board[0][0] == input_board[1][1] == input_board[2][2] or input_board[2][0] == input_board[1][1] ==
			input_board[0][2]):
		logger.info('{turn} won'.format(turn=input_board[1][1]))
		print(input_board[1][1], ' Won')
		return True
	for row in input_board:
		for col in row:
			if col == ' ':
				return False
	logger.info('Draw')
	print('Draw')
	return True
