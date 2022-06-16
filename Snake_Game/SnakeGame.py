#---------- Libraries -----------------

from ast import Global
from  tkinter import *
import random
from turtle import up, window_height, window_width

#---------- Constantes / Game Settings -----------------

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR  = "green"
FOOD_COLOR = "red"
BACKGROUND = "black"


#---------- Create our Snake -----------------
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        #Here we will create the initials coordinates for the snake
        for i  in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x , y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)    
        pass
    pass

#---------- Create our Food -----------------
class Food:
    #Here we will set a random position for the food on the screen, calculate the amount of spaces, and multiply by the SPACE SIZE to transform it into pixels
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        #seting food coordinate
        self.coordinates = [x, y]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")
        pass
    pass

#---------- Here we will set the snake head direction -----------------
def nextTurn(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down": 
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":      
        x += SPACE_SIZE

    snake.coordinates.insert(0, ( x , y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)

    snake.squares.insert(0, square)

    #Here we will create a new food and up the scrore, in case the snake eat the food
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()
    else: 
        #Here will delete snake last body parts of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    #Here we are checking is there is a collision, if it is true, the game will update to next turn
    if checkCollisions(snake):
        gameOver()
    else:    
        window.after(SPEED, nextTurn, snake, food)    

    pass


#---------- Snake direction -----------------
def changeDirection(newDirection):

    global direction
    #here we will set the snake direction
    if newDirection == 'left':
        if direction != 'right':
            direction = newDirection

    elif newDirection == 'right':
        if direction != 'left':
            direction = newDirection

    elif newDirection == 'up':
        if direction != 'down':
            direction = newDirection

    elif newDirection == 'down':
        if direction != 'up':
            direction = newDirection                
    pass

#---------- Collisions -----------------
def checkCollisions(snake):

    x, y = snake.coordinates[0]

    #Screen collision
    if x < 0  or x >= GAME_WIDTH:
        return True
    elif y < 0  or y >= GAME_HEIGHT:
        return True

    #Snake collision
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("game over")
            return True
       
    return False     

    

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="RED", tag="gameover")


#---------- Game Interface -----------------

# window interface
window = Tk()
window.title("Snake Game")
window.resizable(False,False)

score = 0 
direction = 'down'

#Here we will set the word score and font of the word
label = Label(window, text  = "Score:{}".format(score), font =  ('consolas', 40))
label.pack()

#Here we will set the game background, height and width
canvas = Canvas(window, bg = BACKGROUND, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

#Here we will  centralize the screen
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height  =  window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# the controls of the game 
window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))

#Here we will set the snake and the food 
snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()


