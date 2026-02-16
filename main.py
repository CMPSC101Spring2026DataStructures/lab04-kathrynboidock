
# Basic Rock Paper Scissors Game
# Name: Kathryn Boidock
# Date: 02/16/2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# : Implement this function to get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	# : Use console.input and validate input (accept 1/2/3 or words)
	# loop to check for user input errors
	while True:
		user_input = console.input("Please enter your choice (1/rock, 2/paper, or 3/scissors): ").lower().strip()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("Please enter a valid choice!")
	
	return user_choice

# : Implement this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	# calls randowm library to get a computer choice
	return random.choice(choices)

# : Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	# a series of if/elif statements to determine winner
	if user_choice == computer_choice:
		return "tie"
	elif user_choice == "rock" and computer_choice == "scissors":
		return "user"
	elif user_choice == "paper" and computer_choice == "rock":
		return "user"
	elif user_choice == "scissors" and computer_choice == "paper":
		return "user"
	else:
		return "computer"


# : Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	# didnt use user_choice here as it's not needed
	"""Print the choices and the winner of the round using rich colors."""
	# checks the winner for user and prints results based on that
	if winner == "user":
		console.print(f"Computer chose: {computer_choice}")
		console.print("[bold green] You won this round![/bold green]")
	# if not user, continues to computer check
	elif winner == "computer":
		console.print(f"Computer chose: {computer_choice}")
		console.print("[bold red] Sorry, you lost this round :( [/bold red]")
	# if neither then draw
	else:
		console.print(f"Computer chose: {computer_choice}")
		console.print("[bold yellow] It's a tie...( [/bold yellow]")

# : Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	# default values
	user_score = 0
	computer_score = 0
	rounds = 3
	# beginning text to explain to user what game is
	console.print("Welcome super cool user! On todays episode of 'Computer Science Class 101' we're playing Rock! Paper! Scissors!!")
	console.print("You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors btdubs :) ")
	# main game loop for loop through rounds
	for round_num in range(1, rounds + 1):
		console.print(f"Round {round_num} of 3")
		# : Get user and computer choices
		user_choice = get_user_choice()
		comp_choice = get_computer_choice()
		# : Determine winner
		winner = determine_winner(user_choice, comp_choice)
		# : Print round result
		print_round_result(user_choice, comp_choice, winner)
		# : Update scores
		if winner == "user":
			user_score += 1
		elif winner == "computer":
			computer_score += 1
		console.print()
		
	# : Print final scores and announce the overall winner
	console.print(f"User Score: {user_score}")
	console.print(f"Computer Score: {computer_score}")
	if user_score > computer_score:
		console.print("[bold green] Congratulations, you win the game!!![/bold green]")
	elif computer_score > user_score:
		console.print("[bold red] Sorry, you lost the game :( [/bold red]")
	else:
		console.print("[bold yellow] Erm, you didn't lose, but you didn't win, which is equally as bad...( [/bold yellow]")

if __name__ == "__main__":
	main()
	