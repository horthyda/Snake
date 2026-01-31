
import tkinter

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH  = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE

window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Create canvas where the game will be drawn
canvas = tkinter.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                       bg="black", highlightthickness=0)
canvas.pack()
window.update()


window_width= window.winfo_with()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()



window.mainloop()