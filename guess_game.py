import tkinter as tk
import random
from tkinter import messagebox

# Function to start a new game by generating a random number
def new_game():
    global random_number, attempts
    random_number = random.randint(1, 100)  # The computer generates a random number
    attempts = 0
    entry.delete(0, tk.END)
    message_label.config(text="Guess a number between 1 and 100!")
    guess_button.config(state=tk.NORMAL)

# Function to handle user's guess
def guess_number():
    global attempts
    try:
        user_guess = int(entry.get())  # Get the user's guess
        attempts += 1

        if user_guess < random_number:
            message_label.config(text="Too low! Try again.")
        elif user_guess > random_number:
            message_label.config(text="Too high! Try again.")
        else:
            message_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
            guess_button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", f"You guessed it! The number was {random_number}.\nAttempts: {attempts}")
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

# Game instructions
message_label = tk.Label(root, text="Guess a number between 1 and 100!", font=('Arial', 12))
message_label.pack(pady=10)

# Entry widget for user's guess
entry = tk.Entry(root, font=('Arial', 14), width=10)
entry.pack(pady=10)

# Button to submit guess
guess_button = tk.Button(root, text="Guess", font=('Arial', 12), command=guess_number)
guess_button.pack(pady=10)

# Button to start a new game
new_game_button = tk.Button(root, text="New Game", font=('Arial', 12), command=new_game)
new_game_button.pack(pady=10)

# Start the game by generating the first random number
new_game()

# Run the main loop
root.mainloop()

