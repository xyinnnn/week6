from typing import List
import logging

logger = logging.getLogger('tictactoe')


def make_empty_board() -> List[List[str]]:
	return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def show_board(input_board: List[List[str]]):
	for row in input_board:
		print(row)


def receive_input(input_board: List[List[str]], turn: str) -> (int, int):
	while True:
		r = input("input row index: ")
		c = input("input col index: ")
		if not r.isdigit() or not c.isdigit():
			logger.error('{turn} input invalid: {r},{c}'.format(turn=turn, r=r, c=c))
			print('input invalid, not int')
		elif int(r) < 0 or int(r) > 2 or int(c) < 0 or int(c) > 2:
			logger.error('{turn} input invalid: {r},{c}'.format(turn=turn, r=r, c=c))
			print('input invalid, should >=0 and <=2')
		elif input_board[int(r)][int(c)] != ' ':
			logger.error('{turn} input invalid: {r},{c}'.format(turn=turn, r=r, c=c))
			print('input invalid, index already input')
		else:
			logger.info('received {turn} input: {r},{c}'.format(turn=turn, r=r, c=c))
			return int(r), int(c)


def change_turn(old: str) -> str:
	if old == 'X':
		new = 'Y'
	else:
		new = 'X'
	return new


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
