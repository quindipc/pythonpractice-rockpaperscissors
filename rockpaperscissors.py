from tkinter import *
import random


# Initalize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='pink')

Label(root, text = 'Rock, Paper, Scissors' , font='helvetica 20 bold', bg = 'pink').pack()

# User Choice
user_take = StringVar()
Label(root, text = 'CHOOSE: rock, paper, scissors' , font='helvetica 17 bold', bg = 'pink').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'white').place(x=90 , y = 130)

# Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# Function to Start Game    
Result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('TIE')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('YOU LOSE, computer selected PAPER')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('YOU WIN, computer selected SCISSORS')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('YOU LOSE, computer selected SCISSORS')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('YOU WIN, computer selected ROCK')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('YOU LOSE, computer selected ROCK')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('YOU WIN , computer selected PAPER')
    else:
        Result.set('INVALID INPUT: please choose -- rock, paper, scissors')    
 
# Function to Reset       
def Reset():
    Result.set("") 
    user_take.set("")

# Function to Exit    
def Exit():
    root.destroy()

# Define Buttons    
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='white',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='lavenderblush' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='lavenderblush' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='lavenderblush' ,command = Exit).place(x=230,y=310)
root.mainloop()       