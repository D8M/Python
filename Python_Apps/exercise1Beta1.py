# Card Busters code

print("Card Busters".center(33, '*'),"\n")

import random # Importing random method for random choice of cards

round_count = 8
guess_count = 1
winners_list = []

#While Loop initilaser
while guess_count < round_count:
    #print("Round number",guess_count)

    player_one = [10, 6, 8, 9, 7, 12, 7] # Creating list of nums for Player 1

    player_twoComputer = [7, 6, 9, 6, 2, 8, 11] # Creating list of nums for Player 2 -> Computer    
    
    pl1 = random.sample(player_one,1)
    pl2 = random.sample(player_twoComputer,1)
    winners_list.append(pl1+ pl2)
    #print("Winners List: ",winners_list)
    

    
    # Comparison of random numbers chosen
    if pl1 > pl2:
            print("Round number",guess_count,":","Player 1 wins the round, with",pl1,"beating",pl2 )
            pl1 = winners_list.append('Player_one wins')
    elif pl1 <pl2:
            print("Round number",guess_count,":","Player 2 wins the round, with",pl2,"beating",pl1)
            pl2 = winners_list.append('Player_two wins')
    else:
            print("Round number",guess_count,":","This round has ended in a draw!")
            bp = winners_list.append('Both players draw')
    

    #while loop counter & end of while loop area
            
    guess_count += 1
#new_list(map(int, winners_list))
ls = [type(item) for item in winners_list]
print(ls)


#print("Winners List: ",winners_list)


  
        

#print("Player", ,"wins the game, by", ,"wins to",)

    
    




