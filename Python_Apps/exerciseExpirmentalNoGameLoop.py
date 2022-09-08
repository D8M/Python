
print("Card Busters".center(33, '*'),"\n") # Creates asterisks, and centers game title

import random # Importing random method for random choice of given cards between player & computer(player_2)

round_count = 8 # Initialising while loop counters for 0 to 7 turns, & creating empty winners list for storing comparison data.
guess_count = 1
winners_list = []
        
while guess_count < round_count: #While Loop initilaser        

    player_one = [10, 6, 8, 9, 7, 12, 7] # Creating a mutable list of card numbers for Player 1

    player_two = [7, 6, 9, 6, 2, 8, 11] # Creating a mutable list of card numbers for Player 2 which is the Computer            
   
    # Choosing random card number for Player one, Human           
    player_one = random.choice(player_one) ; winners_list.append(player_one)     

    # Choosing random card number for Player two, Computer    
    player_two = random.choice(player_two) ; winners_list.append(player_two)
    

            # Comparison of random card numbers chosen
    if player_one > player_two:
           print("Round number", guess_count,":", "Player 1 wins the round, with", player_one, "beating", player_two )
           winners_list.append('Player_one wins')
                
    elif player_one < player_two:
           print("Round number", guess_count,":","Player 2 wins the round, with", player_two,"beating", player_one)
           winners_list.append('Player_two wins')
                
    else:
           print("Round number", guess_count,":","This round has ended in a draw")
           winners_list.append('Both players draw')   
        
    guess_count += 1 #while loop add counter & end of while loop area
    

# Comparison of how many times each player wins using .count for If statement conditions.

if (winners_list.count("Player_one wins")) > (winners_list.count("Player_two wins")):
        print("\nPlayer 1 wins the game, by" , winners_list.count("Player_one wins"),"wins to", winners_list.count("Player_two wins"))
            
elif (winners_list.count("Player_one wins")) < (winners_list.count("Player_two wins")):
         print("\nPlayer 2 wins the game, by" , winners_list.count("Player_two wins"),"wins to", winners_list.count("Player_one wins"))
        
elif (winners_list.count("Player_one wins")) == (winners_list.count("Player_two wins")):
         print("\nBoth players have drawn.")      

            

    ################################################################################
