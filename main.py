import random as rd #importing module


def roll_the_dice():
    
    dice_result = rd.randint(1,6)  #it will generate the random integer between the range.
    
    return dice_result



print("\n Let start our 'Pig' game.. \n")

while True:
    players = input("Enter how many players want to play(3-4): ")
    if players.isdigit():
        if players =="3" or players =="4":
            players_number = int(players)
            break
        else:
            print("Enter the input between (3-4)")
        continue
    
    else:
        print("Invalid input! ")
        quit()

players_score = [0 for _ in range(players_number)] #using list comprehension it will make the score all of those who want to play.
max_score = 30                                     # the list element depends upon the players_number.     

print(f"Max score of this game is: {max_score}")
print("You all guys don't beat this score.")


while max(players_score) < max_score:     #the game won't be end until and unless the score would be greater than max
    print(f"\nThe maximum score is {max_score} try to beat it!\n")
    for player in range(players_number):  # The for loop would depends upon the number of players.
        player_score = 0
        print(f"This is the turn of player {player+1}.\n")
        while True:
            print(f" Player {player+1} current  score is {player_score}\n")
            start_game = input("Do you want to play(y/n): ").lower()
            if start_game!="y":
                break
            score = roll_the_dice()
            if score == 1:
                print(f"Damn Player  {player+1} just got the 1! so you got zero and you lost your previous score")
                player_score = 0
                break
            else:
                print(f"You got {score}! ")
                player_score+=score
                print(f"Your score is {score}")
        players_score[player] = player_score    
        print(f"Your score is {player_score} ")
    print(f"The maximum score in this turn {max(players_score)}")
    if (max(players_score))>max_score:
        print("\nThe game is completed you guys have beaten the max-score! ")
    else:
        end = "The turn is going to start again. "
        print(end.center(100,"*"))
        

winner_player = players_score.index(max(players_score))#finding the index the max score.
print(f"The player {winner_player+1} has won the game.\nCongratulaions!!")


            