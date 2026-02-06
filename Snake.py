
import tkinter

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH  = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE


class Tile:
    def __init__(self, x ,y): 
      self.x = x 
      self.y = y

window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Create canvas where the game will be drawn
canvas = tkinter.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                       bg="pink", highlightthickness=0)
canvas.pack()
window.update()


window_width= window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

window_x = int (( screen_width/2) - (window_width/2))
window_y = int ((screen_height/2) - (window_height/2))

# format "(w)x (h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game 
snake = Tile (5*TILE_SIZE,5*TILE_SIZE) #single tile ,snake's head 
food =  Tile (10*TILE_SIZE,10*TILE_SIZE)
snake_body = [] #multiple snake tiles
velocityX = 0
velocityY = 0

def change_direction(e): #e = event 
    #print (e)
    print (e.keysym)
    global velocityX , velocityY

    if (e.keysym == "Up"):
        velocityX = 0
        velocityY = -1
    elif(e.keysym == "Down"):
        velocityX =0 
        velocityY =1
    elif(e.keysym == "Left"):
        velocityX =-1 
        velocityY = 0
    elif(e.keysym == "Right"):
        velocityX = 1
        velocityY = 0

def move():
    global snake 

    #coilision 
    if (snake.x == food .x and snake.y == food.y ):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1 ) * TILE_SIZE
        food.y = random.randaint (0, ROWS-1) *TILE_SIZE

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
        


def draw ():
    global snake 
    move()

    canvas.delete("all")


    #draw food 
    canvas.create_rectangle(food.x,food.y,food.x + TILE_SIZE, food.y + TILE_SIZE,fill ="lime red " )

     #draw snake 
    
    canvas.create_rectangle(snake.x, snake.y, snake.x  + TILE_SIZE , snake.y + TILE_SIZE, fill = "lime green ")

    for tile in snake_body: 
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE,tile.y + TILE_SIZE, fill= "lime green")


    window.after(100, draw )

    draw()
    window.bind("<KeyRelease>", change_direction)





window.mainloop()