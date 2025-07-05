import tkinter as tk
import random
from tkinter import messagebox

# Core Game Logic
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Action on player choosing
def play(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = get_winner(player_choice, computer_choice)

    player_label.config(text=f"You chose: {player_choice.capitalize()}")
    computer_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors ✊🖐✌")
root.geometry("400x400")
root.config(bg="#1e1e1e")

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=20)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 14), width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 14), width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 14), width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

player_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="cyan")
player_label.pack(pady=10)

computer_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="orange")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="lime")
result_label.pack(pady=20)

root.mainloop()



