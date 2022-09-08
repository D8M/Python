# Card Busters code with Computer opponent and Player 1

print("Card Busters".center(33, '*'),"\n") # Creates asterisks, and centers game title

import random # Importing random method for random choice of given cards between player & computer

round_count = 8 # Initialising while loop counters & empty winners list
guess_count = 1
winners_list = []


while guess_count < round_count: #While Loop initilaser
    

    player_one = [10, 6, 8, 9, 7, 12, 7] # Creating list of numbers for Player 1

    player_twoComputer = [7, 6, 9, 6, 2, 8, 11] # Creating list of numbers for Player 2 which is the Computer    
    

    # Choosing random num for Player one, Human           
    rand_num = random.randrange(len(player_one)) # Picks a random num from the length of the list in player_one
    random_num1 = player_one[rand_num]
    winners_list.append(random_num1)  # Appends chosen random number to winners_list

    # Choosing random num for Player two, Computer    
    rand_num = random.randrange(len(player_twoComputer)) # Picks a random num from the length of the list in player_two
    random_num2 = player_twoComputer[rand_num]
    winners_list.append(random_num2) # Appends chosen random number to winners_list
   

    # Comparison of random numbers chosen
    if random_num1 > random_num2:
            print("Round number",guess_count,":","Player 1 wins the round, with",random_num1,"beating",random_num2 )
            winners_list.append('Player_one wins')
    elif random_num1 <random_num2:
            print("Round number",guess_count,":","Player 2 wins the round, with",random_num2,"beating",random_num1)
            winners_list.append('Player_two wins')
    else:
            print("Round number",guess_count,":","This round has ended in a draw")
            winners_list.append('Both players draw')    

    
    guess_count += 1 #while loop counter & end of while loop area


# Comparison of how many times each player wins using .count for If statement conditions.
if (winners_list.count("Player_one wins")) > (winners_list.count("Player_two wins")):
        print("\nPlayer 1 wins the game, by" , winners_list.count("Player_one wins"),"wins to", winners_list.count("Player_two wins"))
        
elif (winners_list.count("Player_one wins")) < (winners_list.count("Player_two wins")):
        print("\nPlayer 2 wins the game, by" , winners_list.count("Player_two wins"),"wins to", winners_list.count("Player_one wins"))
        
elif (winners_list.count("Player_one wins")) == (winners_list.count("Player_two wins")):
        print("\nBoth players have drawn.")
        

################################################################################
        





    
    




