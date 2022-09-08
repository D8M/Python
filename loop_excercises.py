# # Loop Eccers

# # Print the cubes of all the elements in a list using a for loop

# results = []
# list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in list_of_nums:
#     results.append(i ** 3)

# print(results)

# #####################################################################

# # Given a 2D list, create a 1D list

# two_d_list = [['volkswagen', 'Mercedes', 'BMW'], ['Honda', 'Toyota', 'Mazada']]

# one_d_list = []

# for i in two_d_list:

#     for j in i:
#         one_d_list.append(i)

#     print(one_d_list)

# ########################################################################

# # Use Range to print out all leap years in 21 century
# # num_list = []
# # for i in range(2000, 2100, 4):
# #     num_list.append(i)
# #     print(num_list)

    # Card Busters code with Computer opponent and Player 1

    print("Card Busters".center(33, '*'),"\n") # Creates asterisks, and centers game title

    import random # Importing random method for random choice of given cards between player & computer

    round_count = 8 # Initialising while loop counters & empty winners list
    guess_count = 1
    winners_list = []


        
        while guess_count < round_count: #While Loop initilaser
        

            player_one = [10, 6, 8, 9, 7, 12, 7] # Creating a mutable list of numbers for Player 1

            player_two = [7, 6, 9, 6, 2, 8, 11] # Creating a mutable list of numbers for Player 2 which is the Computer    
        

            # Choosing random card number for Player one, Human           
            player_one = random.choice(player_one) ; winners_list.append(player_one)     

            # Choosing random card number for Player two, Computer    
            player_two = random.choice(player_two) ; winners_list.append(player_two)
           

            # Comparison of random card numbers chosen
            if player_one > player_two:
                    print("Round number",guess_count,":", "Player 1 wins the round, with", player_one,"beating", player_two )
                    winners_list.append('Player_one wins')
                
            elif player_one < player_two:
                    print("Round number",guess_count,":","Player 2 wins the round, with",player_two,"beating",player_one)
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
            





        
        




