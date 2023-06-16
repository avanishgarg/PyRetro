
# importing required modules
import turtle
import time
import random

delay = 0.1

segments = []


# variables for storing scores
score = 0
high_score = 0

# speed of snake
speed=15

# Creating a window screen
window = turtle.Screen()
window.title("Py-Retro: Snake Game")

# background color of the window
window.bgcolor("blue")

# the width and height can be put as user's choice
window.setup(width=600, height=600)

# setting the animation delay to 0
window.tracer(0)

# creating and configuring the snake's head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "Stop"

# creating and configuring the food
food = turtle.Turtle()
food_colors = random.choice(['red', 'green', 'black'])
food_shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(food_shapes)
food.color(food_colors)
food.penup()
food.goto(0, 100)

# creating and configuring the scr_wrtr for score
scr_wrtr = turtle.Turtle()
scr_wrtr.speed(0)
scr_wrtr.shape("square")
scr_wrtr.color("white")
scr_wrtr.penup()
scr_wrtr.hideturtle()
scr_wrtr.goto(0, 250)
scr_wrtr.write("Score : 0 High Score : 0", align="center", font=("Comic Sans MS", 24, "bold"))


# assigning upward movement for snake
def go_up():
	if snake_head.direction != "down":
		snake_head.direction = "up"


# assigning downward movement for snake
def go_down():
	if snake_head.direction != "up":
		snake_head.direction = "down"


# assigning left movement for snake
def go_left():
	if snake_head.direction != "right":
		snake_head.direction = "left"


# assigning right movement for snake
def go_right():
	if snake_head.direction != "left":
		snake_head.direction = "right"


# moving snake
def move():
	
    # moving snake in upward direction
	if snake_head.direction == "up":
		y = snake_head.ycor()
		snake_head.sety(y+speed)
		
	# moving snake in downward direction
	if snake_head.direction == "down":
		y = snake_head.ycor()
		snake_head.sety(y-speed)
		
    # moving snake in left direction
	if snake_head.direction == "left":
		x = snake_head.xcor()
		snake_head.setx(x-speed)
		
    # moving snake in right direction
	if snake_head.direction == "right":
		x = snake_head.xcor()
		snake_head.setx(x+speed)


# adding the keypress listener for snake movement
window.listen()

window.onkeypress(go_up, "w")
window.onkeypress(go_up, "Up")

window.onkeypress(go_down, "s")
window.onkeypress(go_down, "Down")

window.onkeypress(go_left, "a")
window.onkeypress(go_left, "Left")

window.onkeypress(go_right, "d")
window.onkeypress(go_right, "Right")


# Main Gameplay
while True:
	window.update()
	
    # restarting the game if the snake has touches the boundary
	if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
		scr_wrtr.clear()
		scr_wrtr.write("Game Over", align="center", font=("Comic Sans MS", 24, "bold"))
		time.sleep(1)		
		snake_head.goto(0, 0)
		snake_head.direction = "Stop"
		food_colors = random.choice(['red', 'blue', 'green'])
		food_shapes = random.choice(['square', 'circle'])
		
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		scr_wrtr.clear()
		scr_wrtr.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("Comic Sans MS", 24, "bold"))


    # randomizing the position of food if eaten by the snake
	if snake_head.distance(food) < speed:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		
		if score > high_score:
			high_score = score
		scr_wrtr.clear()
		scr_wrtr.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("Comic Sans MS", 24, "bold"))


	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	
	if len(segments) > 0:
		x = snake_head.xcor()
		y = snake_head.ycor()
		segments[0].goto(x, y)
	
	move()
	for segment in segments:
		if segment.distance(snake_head) < speed:
			scr_wrtr.clear()
			scr_wrtr.write("Game Over", align="center", font=("Comic Sans MS", 24, "bold"))
			time.sleep(1)
			snake_head.goto(0, 0)
			snake_head.direction = "stop"
			food_colors = random.choice(['red', 'blue', 'green'])
			food_shapes = random.choice(['square', 'circle'])
	
			for segment in segments:
				segment.goto(1000, 1000)
			segment.clear()

			score = 0
			delay = 0.1
			scr_wrtr.clear()
			scr_wrtr.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("Comic Sans MS", 24, "bold"))
	time.sleep(delay)

window.mainloop()
