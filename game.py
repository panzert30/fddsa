from random import randint


choices=["rock", "paper", "scissors"]


player_lives = 5
computer_lives = 5


computer=choices[randint(0,2)]


player = False

def winorlose(status):
	print("called win or lose function", status, "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")




while player is False:
	print("========================================")
	print("Computer Lives:", computer_lives, "/5")
	print("Player Lives:", player_lives, "/5")
	print("========================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")
	 

	if player == computer:
		
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
		

	elif computer_lives is 0:
		winorlose("won")
		
	else:
		player = False
		computer=choices[randint(0,2)]



