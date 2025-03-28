import tkinter as tk
from tkinter import ttk
import random

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and cpu_choice == "scissors") or \
         (player_choice == "paper" and cpu_choice == "rock") or \
         (player_choice == "scissors" and cpu_choice == "paper"):
        return "You win!"
    else:
        return "CPU wins!"

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")

        self.player_choice = tk.StringVar()
        self.cpu_choice = tk.StringVar()
        self.result_text = tk.StringVar()
        self.player_score = 0
        self.cpu_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = ttk.Label(self.master, text="Rock, Paper, Scissors!", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Player Choice Buttons
        choice_frame = ttk.Frame(self.master)
        choice_frame.pack(pady=10)

        rock_button = ttk.Button(choice_frame, text="Rock", command=lambda: self.play("rock"))
        rock_button.pack(side=tk.LEFT, padx=10)

        paper_button = ttk.Button(choice_frame, text="Paper", command=lambda: self.play("paper"))
        paper_button.pack(side=tk.LEFT, padx=10)

        scissors_button = ttk.Button(choice_frame, text="Scissors", command=lambda: self.play("scissors"))
        scissors_button.pack(side=tk.LEFT, padx=10)

        # Display Choices
        choices_frame = ttk.Frame(self.master)
        choices_frame.pack(pady=10)

        player_choice_label = ttk.Label(choices_frame, text="You chose:")
        player_choice_label.pack(side=tk.LEFT)
        self.player_choice_display = ttk.Label(choices_frame, textvariable=self.player_choice, font=("Arial", 12, "bold"))
        self.player_choice_display.pack(side=tk.LEFT, padx=5)

        cpu_choice_label = ttk.Label(choices_frame, text="CPU chose:")
        cpu_choice_label.pack(side=tk.LEFT, padx=15)
        self.cpu_choice_display = ttk.Label(choices_frame, textvariable=self.cpu_choice, font=("Arial", 12, "bold"))
        self.cpu_choice_display.pack(side=tk.LEFT, padx=5)

        # Result Label
        result_label = ttk.Label(self.master, textvariable=self.result_text, font=("Arial", 14))
        result_label.pack(pady=10)

        # Score Label
        score_frame = ttk.Frame(self.master)
        score_frame.pack(pady=5)
        ttk.Label(score_frame, text="Your Score:").pack(side=tk.LEFT)
        self.player_score_label = ttk.Label(score_frame, text="0", font=("Arial", 12, "bold"))
        self.player_score_label.pack(side=tk.LEFT, padx=5)
        ttk.Label(score_frame, text="CPU Score:").pack(side=tk.LEFT, padx=15)
        self.cpu_score_label = ttk.Label(score_frame, text="0", font=("Arial", 12, "bold"))
        self.cpu_score_label.pack(side=tk.LEFT, padx=5)

    def play(self, player_choice):
        cpu_choice = get_cpu_choice()

        self.player_choice.set(player_choice.upper())
        self.cpu_choice.set("...")  # Show a placeholder initially
        self.result_text.set("")  # Clear previous result

        # Update CPU choice after a short delay
        self.master.after(500, lambda: self.show_cpu_choice(cpu_choice))

    def show_cpu_choice(self, cpu_choice):
        self.cpu_choice.set(cpu_choice.upper())
        result = determine_winner(self.player_choice.get().lower(), cpu_choice)
        self.result_text.set(result)
        self.update_score(result)

    def update_score(self, result):
        if "You win" in result:
            self.player_score += 1
        elif "CPU wins" in result:
            self.cpu_score += 1
        self.player_score_label.config(text=str(self.player_score))
        self.cpu_score_label.config(text=str(self.cpu_score))

def main():
    root = tk.Tk()
    gui = RockPaperScissorsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()