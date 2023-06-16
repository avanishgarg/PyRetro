import numpy as np
import pygame
import sys
import math


# setting rgb values for colors
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

 
# setting row and column count
count_of_row = 6
count_of_column = 7


# creating GUI
def draw_gui(game_board):

    for c in range(count_of_column):
        for r in range(count_of_row):
            pygame.draw.rect(screen, blue, (c*square_size, r*square_size+square_size, square_size, square_size))
            pygame.draw.circle(screen, black, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), radius)
     
    for c in range(count_of_column):
        for r in range(count_of_row):      
            if game_board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
            elif game_board[r][c] == 2: 
                pygame.draw.circle(screen, yellow, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
    pygame.display.update()
 

# creating a game board
def create_board_for_game():
    game_board = np.zeros((count_of_row, count_of_column))
    return game_board
 

# droping a piece down
def drop_piece_down(game_board, row, col, piece):
    game_board[row][col] = piece
 

# checking if location is valid
def is_valid_location(game_board, col):
    return game_board[count_of_row-1][col] == 0
 

# checking for next open row
def check_next_open_row(game_board, col):
    for r in range(count_of_row):
        if game_board[r][col] == 0:
            return r
 

# printing the game board
def print_game_board(game_board):
    print(np.flip(game_board, 0))
 

# checking if the move is winning move
def make_winning_move(game_board, piece):
    
    # checking a row for a win
    for c in range(count_of_column):
        for r in range(count_of_row-3):
            if game_board[r][c] == piece and game_board[r+1][c] == piece and game_board[r+2][c] == piece and game_board[r+3][c] == piece:
                return True
 
    # checking a column for a win
    for c in range(count_of_column-3):
        for r in range(count_of_row):
            if game_board[r][c] == piece and game_board[r][c+1] == piece and game_board[r][c+2] == piece and game_board[r][c+3] == piece:
                return True
 
    # checking diaganol for a win (positive)
    for c in range(count_of_column-3):
        for r in range(count_of_row-3):
            if game_board[r][c] == piece and game_board[r+1][c+1] == piece and game_board[r+2][c+2] == piece and game_board[r+3][c+3] == piece:
                return True
 
    # checking diagonal for a win (negative) 
    for c in range(count_of_column-3):
        for r in range(3, count_of_row):
            if game_board[r][c] == piece and game_board[r-1][c+1] == piece and game_board[r-2][c+2] == piece and game_board[r-3][c+3] == piece:
                return True
    
 
# initializing local variables 
game_board = create_board_for_game()
print_game_board(game_board)
is_game_over = False
turn = 0


# reseting the game once over
def reset_game():

    game_board = create_board_for_game()
    print_game_board(game_board)
    is_game_over = False
    turn = 0

    # initalizing pygame module
    pygame.init()
    
    # setting the size of the game and width and height
    square_size = 100
    width = count_of_column * square_size
    height = (count_of_row+1) * square_size
    
    # setting window size
    size = (width, height)
    
    # setting the radius of the sqaures
    radius = int(square_size/2 - 5)
    
    screen = pygame.display.set_mode(size)

    # calling function draw_gui again
    draw_gui(game_board)
    pygame.display.update()
    
    # setting a font for the game
    my_game_font = pygame.font.SysFont("Comic Sans MS", 75)
    
    while not is_game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, black, (0,0, width, square_size))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, red, (posx, int(square_size/2)), radius)
                else: 
                    pygame.draw.circle(screen, yellow, (posx, int(square_size/2)), radius)
            pygame.display.update()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, black, (0,0, width, square_size))
               
                # asking for input from Player 1 
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/square_size))
    
                    if is_valid_location(game_board, col):
                        row = check_next_open_row(game_board, col)
                        drop_piece_down(game_board, row, col, 1)
    
                        if make_winning_move(game_board, 1):
                            label = my_game_font.render("Player 1 wins!!", 1, red)
                            screen.blit(label, (40,10))
                            is_game_over = True
    
    
                # asking for input from Player 2
                else:               
                    posx = event.pos[0]
                    col = int(math.floor(posx/square_size))
    
                    if is_valid_location(game_board, col):
                        row = check_next_open_row(game_board, col)
                        drop_piece_down(game_board, row, col, 2)
    
                        if make_winning_move(game_board, 2):
                            label = my_game_font.render("Player 2 wins!!", 1, yellow)
                            screen.blit(label, (40,10))
                            is_game_over = True
    
                print_game_board(game_board)
                draw_gui(game_board)
    
                turn += 1
                turn = turn % 2
    
                if is_game_over:
                    pygame.time.wait(3000)
                    reset_game()


# initalizing pygame module
pygame.init()
 
# setting the size of the game and width and height
square_size = 100
width = count_of_column * square_size
height = (count_of_row+1) * square_size

# setting window size
size = (width, height)

# setting the radius of the sqaures
radius = int(square_size/2 - 5)

screen = pygame.display.set_mode(size)

# calling function draw_gui again
draw_gui(game_board)
pygame.display.update()

# setting a font for the game
my_game_font = pygame.font.SysFont("Comic Sans MS", 75)

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0,0, width, square_size))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(square_size/2)), radius)
            else: 
                pygame.draw.circle(screen, yellow, (posx, int(square_size/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0,0, width, square_size))
            
            # asking for input from Player 1 
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))

                if is_valid_location(game_board, col):
                    row = check_next_open_row(game_board, col)
                    drop_piece_down(game_board, row, col, 1)

                    if make_winning_move(game_board, 1):
                        label = my_game_font.render("Player 1 wins!!", 1, red)
                        screen.blit(label, (40,10))
                        is_game_over = True


            # asking for input from Player 2
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))

                if is_valid_location(game_board, col):
                    row = check_next_open_row(game_board, col)
                    drop_piece_down(game_board, row, col, 2)

                    if make_winning_move(game_board, 2):
                        label = my_game_font.render("Player 2 wins!!", 1, yellow)
                        screen.blit(label, (40,10))
                        is_game_over = True

            print_game_board(game_board)
            draw_gui(game_board)

            turn += 1
            turn = turn % 2

            if is_game_over:
                pygame.time.wait(3000)
                reset_game()