def new_game():
    guesses =[]
    correct_guess = 0
    question_num =1
    for key in questions:
        print("----------------------------------")
        print(key)
        for i in options[question_num -1]:
            print(i)
        guess= input("Enter A B c or D: ")
        guess= guess.upper()
        guesses.append(guess)
        correct_guess += check_answer(questions.get(key),guess)
        question_num +=1
    display_score(correct_guess,guesses)
#--------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0
#--------------------------------
def display_score(corret_guesses, guesses):
    print("----------------------------------")
    print("RESULTS")
    print("----------------------------------")
    print("Answer: ", end = "")
    for i in questions:
        print(questions.get(i), end ="")
    print()
    print("Guesses: ",end ="")
    for i in guesses:
        print( i, end ="")
    print()
    score = int((corret_guesses/len(questions))*100)
    print("Score: " + str(score) + "%")
#--------------------------------
def play_again():
    response = input("Play agian? Y or N:")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False
    pass
#--------------------------------
questions ={
    "Who created Python?": "A",
    "what year was Python created?":"B",
    "Python is tributed to which comedy group?": "C",
    "Is the Earth round?":"C"
}

options = [["A. Guido","B. Elon","C. Gates","D. Zuck"],
["A. 1989","B. 1991","C. 2000","D. 2016"],
["A. Lonely Island","B. Smosh", "C. Monty Python", "D. SNL"],
["A. True","B. FALSE","C. sometimes","D. What"]]

new_game()
for key in questions:
    print(questions.get(key))