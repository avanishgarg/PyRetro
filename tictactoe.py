# importing required modules
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# variable to decide the player
sign = 0

# creating an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]


# checking the winner 
def winner(board, player):

	return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or
			(board[1][0] == player and board[1][1] == player and board[1][2] == player) or
			(board[2][0] == player and board[2][1] == player and board[2][2] == player) or
			(board[0][0] == player and board[1][0] == player and board[2][0] == player) or
			(board[0][1] == player and board[1][1] == player and board[2][1] == player) or
			(board[0][2] == player and board[1][2] == player and board[2][2] == player) or
			(board[0][0] == player and board[1][1] == player and board[2][2] == player) or
			(board[0][2] == player and board[1][1] == player and board[2][0] == player))


# configuring text on button while playing with another player
def get_text(i, j, game_board, player1, player2):

	global sign

	if board[i][j] == ' ':

		if sign % 2 == 0:
			player1.config(state=DISABLED)
			player2.config(state=ACTIVE)
			board[i][j] = "X"

		else:
			player2.config(state=DISABLED)
			player1.config(state=ACTIVE)
			board[i][j] = "O"

		sign += 1
		button[i][j].config(text=board[i][j])

	if winner(board, "X"):
		game_board.destroy()
		box = messagebox.showinfo("Winner", "Player 1 won the match")

	elif winner(board, "O"):
		game_board.destroy()
		box = messagebox.showinfo("Winner", "Player 2 won the match")

	elif(isfull()):
		game_board.destroy()
		box = messagebox.showinfo("Tie Game", "Tie Game")


# checking if the button free to be selected
def isfree(i, j):
	return board[i][j] == " "


# checking if all the buttons are selected on the board
def isfull():

	isBoardFull = True
	for buttons in board:
		if(buttons.count(' ') > 0):
			isBoardFull = False
	return isBoardFull


# creating GUI for multiplayer
def gameboard_pl(game_board, player1, player2):

	global button
	button = []

	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []

		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text, i, j, game_board, player1, player2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)

	game_board.mainloop()
	


# creating GUI for singleplayer
def gameboard_pc(game_board, player1, player2):

	global button
	button = []

	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []

		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, player1, player2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	game_board.mainloop()
	

# deciding computer's next move
def pc():

	possiblemove = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				possiblemove.append([i, j])
	move = []

	if possiblemove == []:
		return
	
	else:
		for let in ['O', 'X']:
			for i in possiblemove:
				boardcopy = deepcopy(board)
				boardcopy[i[0]][i[1]] = let
				if winner(boardcopy, let):
					return i
				
		corner = []
		for i in possiblemove:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				corner.append(i)

		if len(corner) > 0:
			move = random.randint(0, len(corner)-1)
			return corner[move]
		
		edge = []
		for i in possiblemove:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				edge.append(i)

		if len(edge) > 0:
			move = random.randint(0, len(edge)-1)
			return edge[move]


# configuring buttons for singleplayer
def get_text_pc(i, j, game_board, player1, player2):

	global sign

	if board[i][j] == ' ':

		if sign % 2 == 0:
			player1.config(state=DISABLED)
			player2.config(state=ACTIVE)
			board[i][j] = "X"

		else:
			button[i][j].config(state=ACTIVE)
			player2.config(state=DISABLED)
			player1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])

	x = True

	if winner(board, "X"):
		game_board.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Player won the match")

	elif winner(board, "O"):
		game_board.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Computer won the match")

	elif(isfull()):
		game_board.destroy()
		x = False
		box = messagebox.showinfo("Tie Game", "Tie Game")

	if(x):

		if sign % 2 != 0:
			move = pc()
			button[move[0]][move[1]].config(state=DISABLED)
			get_text_pc(move[0], move[1], game_board, player1, player2)


# initializing singleplayer gameboard
def withpc(game_board):

	game_board.destroy()
	game_board = Tk()
	
	game_board.title("Py-Retro: Tic Tac Toe")
	player1 = Button(game_board, text="Player : X", width=10)
	player1.grid(row=1, column=1)
	player2 = Button(game_board, text="Computer : O",
				width=10, state=DISABLED)

	player2.grid(row=2, column=1)
	gameboard_pc(game_board, player1, player2)


# initializing multiplayer gameboard
def withplayer(game_board):

	game_board.destroy()
	game_board = Tk()
	screen_width = game_board.winfo_screenwidth()  # Width of the screen
	screen_height = game_board.winfo_screenheight() # Height of the screen
	
	# Calculate Starting X and Y coordinates for Window
	x = (screen_width/2) - (250)
	y = (screen_height/2) - (250)
	game_board.geometry('%dx%d+%d+%d' % (250, 250, x, y))
	game_board.eval('tk::PlaceWindow . center')
	game_board.title("Py-Retro: Tic Tac Toe")
 
	player1 = Button(game_board, text="Player 1 : X", width=10)

	player1.grid(row=1, column=1)
	player2 = Button(game_board, text="Player 2 : O",
				width=10, state=DISABLED)

	player2.grid(row=2, column=1)
	gameboard_pl(game_board, player1, player2)


# main function for gameplay
def start_game():

	menu = Tk()
	screen_width = menu.winfo_screenwidth()  # Width of the screen
	screen_height = menu.winfo_screenheight() # Height of the screen
	
	# Calculate Starting X and Y coordinates for Window
	x = (screen_width/2) - (250)
	y = (screen_height/2) - (250)
	menu.geometry('%dx%d+%d+%d' % (250, 250, x, y))
	menu.title("Py-Retro: Tic Tac Toe")
	wpc = partial(withpc, menu)
	wpl = partial(withplayer, menu)


	button1 = Button(menu, text="Single Player", command=wpc,
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)

	button2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)

	button3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)

	button1.pack(side='top')
	button2.pack(side='top')
	button3.pack(side='top')
	menu.mainloop()


if __name__ == '__main__':
	start_game()