import random

# ANSI escape codes for colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

CHOICES = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

def display_title():
    print(f"{BOLD}{BLUE}-----------------------------------{RESET}")
    print(f"{BOLD}{BLUE}   Rock, Paper, Scissors - The Game   {RESET}")
    print(f"{BOLD}{BLUE}-----------------------------------{RESET}")
    print()

def get_player_choice():
    while True:
        choice_prompt = f"Choose your weapon ({BLUE}rock{RESET} {CHOICES['rock']}, {GREEN}paper{RESET} {CHOICES['paper']}, {YELLOW}scissors{RESET} {CHOICES['scissors']}): "
        choice = input(choice_prompt).lower()
        if choice in CHOICES:
            return choice
        else:
            print(f"{RED}Invalid choice.{RESET} Please enter rock, paper, or scissors.")

def get_cpu_choice():
    choices = list(CHOICES.keys())
    return random.choice(choices)

def display_choices(player_choice, cpu_choice):
    print(f"{BOLD}You chose:{RESET} {BLUE}{player_choice.upper()} {CHOICES[player_choice]}{RESET}")
    print(f"{BOLD}CPU chose:{RESET} {RED}{cpu_choice.upper()} {CHOICES[cpu_choice]}{RESET}")
    print("-" * 30) # Visual separator

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "tie"
    elif (player_choice == "rock" and cpu_choice == "scissors") or \
         (player_choice == "paper" and cpu_choice == "rock") or \
         (player_choice == "scissors" and cpu_choice == "paper"):
        return "player"
    else:
        return "cpu"

def display_round_result(result):
    if result == "player":
        print(f"{GREEN}{BOLD}You win this round!{RESET} 🎉")
    elif result == "cpu":
        print(f"{RED}{BOLD}CPU wins this round!{RESET} 🤖")
    else:
        print(f"{YELLOW}{BOLD}This round is a tie!{RESET}")
    print("-" * 30)

def display_score(player_score, cpu_score):
    print(f"{BOLD}Score:{RESET}")
    print(f"  {BLUE}You:{RESET} {player_score}")
    print(f"  {RED}CPU:{RESET} {cpu_score}")
    print("-" * 30)

def play_round(player_score, cpu_score):
    player_choice = get_player_choice()
    cpu_choice = get_cpu_choice()
    display_choices(player_choice, cpu_choice)
    result = determine_winner(player_choice, cpu_choice)
    display_round_result(result)
    if result == "player":
        player_score += 1
    elif result == "cpu":
        cpu_score += 1
    display_score(player_score, cpu_score)
    return player_score, cpu_score

def main():
    display_title()
    player_score = 0
    cpu_score = 0
    while True:
        player_score, cpu_score = play_round(player_score, cpu_score)
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"{YELLOW}Final Score - You: {player_score}, CPU: {cpu_score}{RESET}")
            print(f"{YELLOW}Thanks for playing!{RESET} 👋")
            break
        print("-" * 30) # Separator between rounds

if __name__ == "__main__":
    main()