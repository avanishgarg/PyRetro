import sys
import os
from tkinter import *
from tkinter import simpledialog,ttk

window=Tk()

# Add image file
bg = PhotoImage(file = "images/template.png")
  
# Show image using label
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

width = 600 # Width 
height = 600 # Height
 
screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

window.title("Py-Retro")
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def run_snake():
    os.system('snake.py')

def run_connect_four():
    os.system('connect_four.py')

def run_superhuman():
    os.system('superhuman.py')
    
def run_tetris():
    os.system('tetris.py')

def run_tictactoe():
    os.system('tictactoe.py')
    
def memory_game():
    os.system('memorygame.py')

def display_text():
   global entry
   string= "Welcome to Py-Retro "+ entry.get()
   label.configure(text=string)
   entry.delete(0, END)
   btn_inp.after(1, btn_inp.destroy)
   entry.after(1,entry.destroy)



#Initialize a Label to display the User Input
label=Label(window, text="", fg="white", font=("Comic Sans MS",22),bg="#3A928E")
# label.grid(column=1, row=0)
label.place(relx = 0.5,
                   rely = 0.49,
                   anchor = CENTER)
# label.pack()

#Create an Entry widget to accept User Input
entry= Entry(window, width= 40, bd=0, highlightthickness=0)
entry.focus_set()
entry.pack()
entry.place(relx=0.5, rely=0.47,anchor=CENTER)
# entry.pack()

#Create a Button to validate Entry Widget
btn_inp=Button(window, text= "Okay",fg="white",width= 20, command= display_text,highlightthickness=0, bg="#3A928E")
# btn_label.grid(column=1, row=0)
btn_inp.pack()
btn_inp.place(relx=0.5, rely=0.52, anchor=CENTER)



# create 5 buttons in the frame
button1 = Button(window,text="Snake Game", bd=0,fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=run_snake,highlightthickness=0)
button1.pack(padx=10, pady=10)

button2 = Button(window, text="Connect four",bd=0, fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=run_connect_four,highlightthickness=0, highlightbackground="white")
button2.pack(padx=10, pady=10)

button3 = Button(window, text="SuperHuman",bd=0 ,fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=run_superhuman,highlightthickness=0, highlightbackground="white")
button3.pack(padx=10, pady=10)

button4 = Button(window, text="Tetris",bd=0 ,fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=run_tetris,highlightthickness=0, highlightbackground="white")
button4.pack(padx=10, pady=10)

button5 = Button(window, text="Tic Tac Toe",bd=0,fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=run_tictactoe,highlightthickness=0, highlightbackground="white")
button5.pack(padx=10, pady=10)

button6 = Button(window, text="Memory Game",bd=0,fg="white",font=("Comic Sans MS", 17),bg="#5E3174",width= 20,height=1,command=memory_game,highlightthickness=0, highlightbackground="white")
button6.pack(padx=10, pady=10)

button1.place(relx=0.25, rely=0.60, anchor=CENTER)
button2.place(relx=0.75, rely=0.60, anchor=CENTER)
button3.place(relx=0.25, rely=0.70, anchor=CENTER)
button4.place(relx=0.75, rely=0.70, anchor=CENTER)
button5.place(relx=0.25, rely=0.80, anchor=CENTER)
button6.place(relx=0.75, rely=0.80, anchor=CENTER)


window.mainloop()


# vulnerable code
import os
filename = input("Enter a filename: ")
file = open(filename, "r")
print(file.read())
file.close()


# vulnerable code 2
import subprocess
command = input("Enter a command: ")
output = subprocess.check_output(command, shell=True)
print(output)


# vulnerable code 3
def execute_command(command):
    subprocess.call(command)

command = input("Enter a command to execute: ")
execute_command(command)