import random

player_score = 0
bot_score = 0

list1 = [1, 2, 3]

def score():
    print("Your score is :" + str(player_score))
    print("The bot's score is: " + str(bot_score))

while not player_score == 10 and not bot_score == 10:
    choice = random.choice(list1)
    player = input("rock paper, or scissor: ")
    if player == "r" and choice == 1:
        print("you Tie!")
        score()
    elif player == "r" and choice == 2:
        print("you Lose!")
        bot_score += 1
        score()
    elif player == "r" and choice == 3:
        print("You Win!")
        player_score += 1
        score()
    
    elif player == "p" and choice == 1:
        print("you Win!")
        player_score += 1
        score()
    elif player == "p" and choice == 2:
        print("you Tie!")
        score()
    elif player == "p" and choice == 3:
        print("You lose!")
        bot_score += 1
        score()
        
    if player == "s" and choice == 1:
        print("you Lose!")
        bot_score += 1
        score()
    elif player == "s" and choice == 2:
        print("you Win!")
        player_score += 1
        score()
    elif player == "s" and choice == 3:
        print("You Tie!")