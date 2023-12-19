# Import necessary modules
from tkinter import *
import random

# Generate a random number between 1 and 3301
num = random.randint(1, 3301)

# Function to check the user's guess
def Check_Guess():
    guess = int(number.get())
    if guess == num:
        result_label.config(text="Well done! You found the number.")
    elif guess < num:
        result_label.config(text="More!")
    else:
        result_label.config(text="Less!")

# Create the main window
game = Tk()
game.title("Number Guessing Game")

# Create and pack widgets
Label(game, text="Guess A Number Between 1 And 3301").pack()

number = Entry(game)
number.pack()

check_button = Button(game, text="Check it", command=Check_Guess)
check_button.pack()

result_label = Label(game, text="")
result_label.pack()

# Set window properties
game.geometry('500x500+450+150')  # Set window size and position
game.iconbitmap('C:\\Users\\salah\\Downloads\\game.ico')  # Set window icon

# Start the Tkinter event loop
game.mainloop()
