from random import randint
print("Rock, Paper, Scissors:")
while True:
	computer = randint(0,2)
	player = input().capitalize()
	if player == "Done":
		break
	if computer == 0:
		computer ="Paper"
	if computer == 1:
		computer = "Scissors"
	if computer == 2:
		computer = "Rock"
	print("----")
	print ("You choose: " + player)
	if player == computer:
		print ("Computer chooses: " + computer)
		print("=> Draw")
	else:
		if player == "Scissors":
			if computer == "Rock":
				print ("Computer chooses: " + computer)
				print("You Lose")			
			else:
				print ("Computer chooses: " + computer)
				print ("You Win")
		elif player == "Rock":
			if computer == "Scissors":
				print ("Computer chooses: " + computer)
				print("You Win")
			else:
				print ("Computer chooses: " + computer)
				print ("You Lose")
		elif player == "Paper":
			if computer == "Scissors":
				print ("Computer chooses: " + computer)
				print("You Lose")
			else:
				print ("Computer chooses: " + computer)
				print("You Win")
		else:
			if player != "Rock" :
				if player != "Scissors":
					if player != "Paper":
						print("Invalid input")
						continue
print("Good bye")		
		 