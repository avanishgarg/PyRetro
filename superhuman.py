# import modules
import random
import sys
import pygame
from pygame.locals import *

# defining height and width of game window
game_window_width = 600
game_window_height = 499

# set height and width of window
window = pygame.display.set_mode((game_window_width, game_window_height))
elevation = game_window_height * 0.9
game_images = {}

# setting fps
frame_per_second = 50

# setting paths of images
wall_image = 'images/wall.jpg'
background_image = 'images/background.jpg'
superhuman_image = 'images/player-remove.png'
sealevel_image = 'images/base.jfif'


def superhuman():
	
	# defining variables
	player_score = 0
	horizontal = int(game_window_width/5)
	vertical = int(game_window_width/2)
	ground = 0
	my_temp_height = 100

	# generating two walls for blitting on window
	first_wall = create_wall()
	second_wall = create_wall()

	# Llst of lower walls
	down_walls = [
		{'x': game_window_width+300-my_temp_height,
		'y': first_wall[1]['y']},
		{'x': game_window_width+300-my_temp_height+(game_window_width/2),
		'y': second_wall[1]['y']},
	]

	# list of upper walls
	up_walls = [
		{'x': game_window_width+300-my_temp_height,
		'y': first_wall[0]['y']},
		{'x': game_window_width+200-my_temp_height+(game_window_width/2),
		'y': second_wall[0]['y']},
	]

	# wall velocity along x axis
	wall_vel_x = -4

	# superhuman velocity
	superhuman_velocity_y = -9
	superhuman_Max_Vel_Y = 10
	superhuman_Min_Vel_Y = -8
	superhumanAccY = 1
	superhuman_flap_velocity = -8
	
	superhuman_flapped = False

	while True:
		for event in pygame.event.get():
			
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				if vertical > 0:
					superhuman_velocity_y = superhuman_flap_velocity
					superhuman_flapped = True

		
		# function to check if superhuman crashes onto a wall
		is_game_over = isGameOver(horizontal,
							vertical,
							up_walls,
							down_walls)
		
		if is_game_over:
			return

		# checking player's score
		playerMidPos = horizontal + game_images['superhuman'].get_width()/2
		
		for wall in up_walls:
			wallMidPos = wall['x'] + game_images['wall_image'][0].get_width()/2
		
			if wallMidPos <= playerMidPos < wallMidPos + 4:
				player_score += 1
				print(f"Your score is {player_score}")

		if superhuman_velocity_y < superhuman_Max_Vel_Y and not superhuman_flapped:
			superhuman_velocity_y += superhumanAccY

		if superhuman_flapped:
			superhuman_flapped = False
		
		playerHeight = game_images['superhuman'].get_height()
		vertical = vertical + \
			min(superhuman_velocity_y, elevation - vertical - playerHeight)

		# moving walls
		for upper_wall, lower_wall in zip(up_walls, down_walls):
			upper_wall['x'] += wall_vel_x
			lower_wall['x'] += wall_vel_x

		# adding a new wall to the right when leftmost wall disappears
		if 0 < up_walls[0]['x'] < 5:
			newwall = create_wall()
			up_walls.append(newwall[0])
			down_walls.append(newwall[1])

		# deleting a wall when not on screen
		if up_walls[0]['x'] < -game_images['wall_image'][0].get_width():
			up_walls.pop(0)
			down_walls.pop(0)

		# loading game images
		window.blit(game_images['background'], (0, 0))
		
		for upper_wall, lower_wall in zip(up_walls, down_walls):
			window.blit(game_images['wall_image'][0],
						(upper_wall['x'], upper_wall['y']))
			window.blit(game_images['wall_image'][1],
						(lower_wall['x'], lower_wall['y']))

		window.blit(game_images['sea_level'], (ground, elevation))
		window.blit(game_images['superhuman'], (horizontal, vertical))

		# loading score images
		numbers = [int(x) for x in list(str(player_score))]
		width = 0

		# finding the width of score images from numbers
		for num in numbers:
			width += game_images['scoreimages'][num].get_width()
		Xoffset = (game_window_width - width)/1.1

		# ading images to the game window
		for num in numbers:
			window.blit(game_images['scoreimages'][num],
						(Xoffset, game_window_width*0.02))
			Xoffset += game_images['scoreimages'][num].get_width()

		# Refreshing the game window and displaying the score.
		pygame.display.update()
		framepersecond_clock.tick(frame_per_second)


# function for checking if game is over
def isGameOver(horizontal, vertical, up_walls, down_walls):
	
	if vertical > elevation - 25 or vertical < 0:
		return True

	for wall in up_walls:
		wall_height = game_images['wall_image'][0].get_height()
		
		if(vertical < wall_height + wall['y'] and\
		abs(horizontal - wall['x']) < game_images['wall_image'][0].get_width()):
			return True

	for wall in down_walls:
		
		if (vertical + game_images['superhuman'].get_height() > wall['y']) and\
		abs(horizontal - wall['x']) < game_images['wall_image'][0].get_width():
			return True
	return False

# function for creating a wall
def create_wall():
	offset = game_window_height/3
	wall_height = game_images['wall_image'][0].get_height()
	y2 = offset + \
		random.randrange(
			0, int(game_window_height - game_images['sea_level'].get_height() - 1.2 * offset))
	wallX = game_window_width + 10
	y1 = wall_height - y2 + offset
	wall = [
		# upper wall
		{'x': wallX, 'y': -y1},

		# lower wall
		{'x': wallX, 'y': y2}
	]
	return wall


# main function
if __name__ == "__main__":

	# initializing modules of pygame library
	pygame.init()
	framepersecond_clock = pygame.time.Clock()

	# setting the title on top of game window
	pygame.display.set_caption('Py-Retro: Super Human')

	# loading all the images which we will use in the game

	# images for displaying score
	game_images['scoreimages'] = (
		pygame.image.load('images/0.png').convert_alpha(),
		pygame.image.load('images/1.png').convert_alpha(),
		pygame.image.load('images/2.png').convert_alpha(),
		pygame.image.load('images/3.png').convert_alpha(),
		pygame.image.load('images/4.png').convert_alpha(),
		pygame.image.load('images/5.png').convert_alpha(),
		pygame.image.load('images/6.png').convert_alpha(),
		pygame.image.load('images/7.png').convert_alpha(),
		pygame.image.load('images/8.png').convert_alpha(),
		pygame.image.load('images/9.png').convert_alpha()
	)
	game_images['superhuman'] = pygame.image.load(
		superhuman_image).convert_alpha()
	game_images['sea_level'] = pygame.image.load(
		sealevel_image).convert_alpha()
	game_images['background'] = pygame.image.load(
		background_image).convert_alpha()
	game_images['wall_image'] = (pygame.transform.rotate(pygame.image.load(
		wall_image).convert_alpha(), 180), pygame.image.load(
	wall_image).convert_alpha())


	# printing welcome message
	print("WELCOME TO THE Py-Retro: Super Human")
	print("Press space or enter to start the game")


	# infinte loop
	while True:

		# setting the coordinates of superhuman

		horizontal = int(game_window_width/5)
		vertical = int(
			(game_window_height - game_images['superhuman'].get_height())/2)
		ground = 0
		
		while True:
			for event in pygame.event.get():

				# if user clicks on cross button, close the game
				if event.type == QUIT or (event.type == KEYDOWN and \
										event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				# game starts when user presses space key or up arrow
				elif event.type == KEYDOWN and (event.key == K_SPACE or\
												event.key == K_UP):
					superhuman()

				# nothing happens if the user doesn't press any key
				else:
					window.blit(game_images['background'], (0, 0))
					window.blit(game_images['superhuman'],
								(horizontal, vertical))
					window.blit(game_images['sea_level'], (ground, elevation))
					pygame.display.update()
					framepersecond_clock.tick(frame_per_second)
