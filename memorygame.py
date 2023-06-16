# importing modeules
import tkinter as tk
import random
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


# defining variables
mouse_clicks = -1
num_of_flipped_tiles = 16
num_of_moves = 0
high_score = 0


# check if all tiles are matched
def check_win():
    global high_score, num_of_moves
    
    if num_of_flipped_tiles == 0:
        
        if num_of_moves <= high_score or high_score == -1:
            high_score = num_of_moves

            # accessing high score from the file
            f = open('highScore.txt', 'w')
            f.write(str(high_score))
            f.close()            

        winner_label['text']='CLICKS: '+str(num_of_moves)+', BEST: '+str(high_score)


# printing num of moves
def print_moves():
    winner_label['text'] = 'CLICKS: ' + str(num_of_moves)


# starting a new game
def new_game():
    global mouse_clicks, num_of_flipped_tiles, buttons
    global colours, num_of_moves, winner_label, high_score

    mouse_clicks = -1
    num_of_flipped_tiles = 16
    num_of_moves = 0
    buttons = {}
    winner_label['text'] = ''

    # accessing high score from the file
    f = open('highScore.txt', 'r')
    high_score = int(f.readline().strip())
    f.close()

    # randomizing the colours
    random.shuffle(colours)

    k=0
    for i in range(4):
        for j in range(4):
            btn = b(k)
            buttons[k] = btn
            
            if k!= len(colours)-1: 
                k+=1
        
    k=0
    for i in range(4):
        for j in range(4):
            buttons[k].bttn.grid(row=i, column=j, sticky='nsew')
            
            if k!= len(colours)-1: 
                k+=1

 
class b:
    
    # init function
    def __init__(self, k):
        self.index = k
        self.bttn = tk.Button(frm,
                             width=6, height=2,
                             borderwidth=6, 
                             bg='white', activebackground = colours[self.index],
                             command=self.btn_press
                             )
        
    # function for btn press  
    def btn_press(btn):
        global mouse_clicks, num_of_moves

        btn.bttn.configure(bg=colours[btn.index])
        num_of_moves += 1
        print_moves()

        if mouse_clicks == -1:
            mouse_clicks = btn.index

        else:
            btn.compare_pressed_btns()
    
    # checking if the previous and present btn click have same color
    def compare_pressed_btns(btn):
        global mouse_clicks
        global num_of_flipped_tiles

        if (colours[btn.index] != colours[mouse_clicks]):
            btn.bttn.configure(bg='white')
            buttons[mouse_clicks].bttn.configure(bg='white')
            mouse_clicks = -1

        elif colours[btn.index] == colours[mouse_clicks] and (btn.index != mouse_clicks):
            btn.bttn['state'] = tk.DISABLED
            buttons[mouse_clicks].bttn['state']= tk.DISABLED
            mouse_clicks = -1
            num_of_flipped_tiles -= 2
            check_win()

        elif  btn.index == mouse_clicks:
            btn.bttn.configure(bg='white')
            mouse_clicks = -1
       

# configuring windows
window = tk.Tk()
window.title('Py-Retro: Memory Game')
window.config(bg = 'black')

window.rowconfigure([0,1],weight=1,pad=2)
window.columnconfigure(0,weight =1, pad=2)

frm = tk.Frame(window, bg='Gray')
frm.grid(row = 0, column=0, sticky='nsew')

frm.rowconfigure(list(range(4)), minsize=50, pad=2)
frm.columnconfigure(list(range(4)), minsize=50, pad=2)


# dictionary of buttons
buttons = {}


# list of colours
colours=['YellowGreen', 'Violet', 'Tomato', 'SlateBlue', 'DarkCyan', 'Orange','DodgerBlue', 'ForestGreen']*2


# randomizing the colours
random.shuffle(colours)


frm2 = tk.Frame(window, bg='Khaki')


# label for displaying winner details
winner_label = tk.Label(frm2,
                  width=19, height=1,
                 bg='PowderBlue',
                 relief=tk.GROOVE,
                 borderwidth=2)
winner_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')


# button for new game
new_game_btn = tk.Button(text='NEW GAME',
                        master=frm2,
                       width=10, height=1, borderwidth=3,
                       bg='Plum',
                       command=new_game)
new_game_btn.grid(row=0, column=1, padx=5, pady=5, sticky = 'nsew')

frm2.grid(row=1, column=0, sticky='nsew')


# calling the new game function
new_game()

window.mainloop()