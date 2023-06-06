import random
import time

#slowpring function
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)




#on tie
def tie():
    slow_print("You tied!" + "\n")
    
#on win condition
def win():
    slow_print("You won!" + "\n")
    
#on loss condition
def loss():
    slow_print("You lost!" + "\n")
    

def game():

        #list for random picker
        list = [1,2,3]
    
        #player and bot score
        bot_score = 0
        player_score = 0
        
        
        while not bot_score == 10 and not player_score == 10:
            
            npc = random.choice(list)
            player = input("rock paper, or scissors: ")
            
            #player inputs rock
            if player == "r" or "rock" and npc == 1:
                tie()
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "r" or "rock" and npc == 2:
                loss()
                bot_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "r" or "rock" and npc == 3:
                win()
                player_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            
            #player inputs paper
            elif player == "p" or "paper" and npc == 1:
                win()
                player_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "p" or "paper" and npc == 2:
                tie()
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "p" or "paper" and npc == 3:
                loss()
                bot_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            
            #player inputs scissors
            elif player == "s" or "scissors" and npc == 1:
                loss()
                bot_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "s" or "scissors" and npc == 2:
                win()
                player_score += 1
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            elif player == "s" or "scissors" and npc == 3:
                tie()
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
            
            #player inputs invalid phrases
            elif not player == "r" or "rock" or "p" or "paper" or "s" or "scissors":
                print("invalid phrase")
                time.sleep(.5)
                
        if player_score == 10 or bot_score == 10:
            if player_score == 10:
                slow_print("You win!")
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
                slow_print("Game Over" + "\n" + "Goodbye")
            elif bot_score == 10:
                slow_print("You lose!" + "\n")
                slow_print("Your score is: " + str(player_score) + "\n")
                slow_print("The bot's score is: " + str(bot_score) + "\n")
                time.sleep(.5)
                slow_print("Game Over" + "\n" + "Goodbye")
                
                
game()
        