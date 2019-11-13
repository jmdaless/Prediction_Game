# Assignment 1 - Author: Juan Martin D'Alessandro - GMBD2019

# define input values and lists with valid options. this will facilitate any upgrade or update in the future.
play_again = int(1)
play_again_options = ['1','2']
dificulty_options = ['1','2']
moves_options = 1
moves_options = list(range(5,51)) #set the valid input for number of moves. it is a list of 
player_move_options = ['1','0']

# create function linear_congruence as defined on the documentation to calculate computer bet on an aleatory way.
# this function is also used to generate random values of computer move on the dificult game
def linear_congruence(xi):
    '''function to calculate linear congruences value and computer bet'''
    a = 22695477
    b = 1
    n = 2**32
    xi_plus_1 = (a * xi + b) % n
    if xi_plus_1 <= 2**31:
        computer_move = 0
    else:
        computer_move = 1
    return (computer_move, xi_plus_1)
  
           
#------------------------------------------------------------------------------ 
# Opening Message.
print('Hello and Welcome to this exciting game: Human Behavior Prediction by JM DAlessandro')

# big loop with game. At the end of each game the player can decide to play again (1) or quit (other value).
# we create a variable to save the info if the player wants to continue playing.
while play_again == 1:

    # create a numeric variable with the input of the user to select the game level she/he wants to play
    select_dificulty = (input('Choose the type and difficulty of the game (1: Easy; 2: Difficult):'))
    while select_dificulty not in dificulty_options:
        select_dificulty = (input('Choose the type and difficulty of the game (1: Easy; 2: Difficult). (To quit the game press CTRL + C): '))
    select_dificulty = int(select_dificulty) # transform the variable to int.
    
    # define the number of moves the player wants to play on a variable called number_of_moves limiting the range to the values on the list called move options created at the begining.      
    number_of_moves = int(input('Enter the number of moves you want to play today:'))
    while number_of_moves not in moves_options:
        number_of_moves = int(input('Not Valid Entry. Min number of moves per play is 5 and Max is 50. (To quit the game press CTRL + C): '))
   
   
    
    # GAME 1 - Easy
    if select_dificulty == 1: 
        MS = 0 # reset the counters for every game
        PS = 0 # reset the counters for every game
        xi = 1234 # set seed
        
        for turn in range(number_of_moves):
            
            #player move as per input. limited only to 0 or 1
            player_move = input('Choose your move number %s (0 or 1):' % (turn+1))
            while player_move not in player_move_options: 
                player_move = input('wrong option. please insert 0 or 1!. (To quit the game press CTRL + C): ')
            player_move = int(player_move) # transform the variable to int.
                
            computer_move, xi = linear_congruence(xi) # randomnly generates the computer move.
            
            if player_move == computer_move:
                MS = MS + 1 # machine score is increased by 1 because both moves are equal.
                print('player = %d - machine = %d - Machine Wins!' % (player_move, computer_move))
              
            else:
                PS = PS+1  # player score is increased by 1 as moves are not equal. this means the computer didn't guess.
                print('player = %d - machine = %d - You Win!' % (player_move, computer_move))
            
            # Leaderboard as expected on the submission
            print('PLAYER:' + '*'*PS) 
            print('MACHINE:' + '*'*MS)
            print('----')
        
        # Final Message with total Score 
        if MS > PS :
            print('Game is Over. Machine wins!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))               
        elif MS < PS :
            print('Game is Over. You win!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))
        else :
            print('Game is Over. Is a tie!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))
                
            
    # GAME 2 - Dificult
    else:
        MS = 0 # reset the counters for every game leaderboard
        PS = 0 # reset the counters for every game leaderboard
        # reset the counters for every game. not the aim to save previous games information.
        throw00 = 0 # count of the number of times the human player chose 0 given that in the previous bid his/her bid was 0
        throw01 = 0 # count of the number of times the human player chose 0 given in the bid previous his/her bid was 1
        throw10 = 0 # count of the number of times the human player chose 1 given that his/her previous bid was 0
        throw11 = 0 # count of the number of times the human player chose 1 given his/her previous bid was 1
        xi = 1234
        prev_throw, xi = linear_congruence(xi) #for the 1st throw of the player, we set a random value of previous throw for the computer to start the training process.
        
        for turn in range(number_of_moves):
            
            # player move as per imput. limited only to 0 or 1
            player_move = input('Choose your move number %s (0 or 1):' % (turn+1))
            while player_move not in player_move_options: 
                player_move = input('wrong option. please insert 0 or 1! (To quit the game press CTRL + C): ')
            player_move = int(player_move)
            
            #the computer algorithm depends on the prev move and the current one.
            if prev_throw == 0:
                if throw10 > throw00: 
                    computer_move = 1
                elif throw10 < throw00: 
                    computer_move = 0
                else : 
                    computer_move, xi = linear_congruence(xi) #first move will come here as if throw 10 = throw 00
            else :#player move = 1
                if throw01 > throw11:
                    computer_move = 0
                elif throw11 > throw01:
                    computer_move = 1
                else :
                    computer_move, xi = linear_congruence(xi) #first move will come here as if throw 01 = throw 11
            
            if turn > 0: #after the first move, the counter will start saving information on the moves of the player
                if player_move == 0 and prev_throw == 0:
                    throw00 = throw00 + 1
                elif player_move == 1 and prev_throw == 0:
                    throw10 = throw10 +1
                elif player_move == 0 and prev_throw ==1:
                    throw01 = throw01 + 1
                else :
                    throw11 = throw11 + 1
            
            prev_throw = player_move # save this move as previous throw of the next time is getting on this for loop.
            
            if player_move == computer_move: #leaderboard as set on the submission. equal to level 1.
                MS = MS + 1
                print('player = %d - machine = %d - Machine Wins!' % (player_move, computer_move))
              
            else:
                PS = PS+1
                print('player = %d - machine = %d - You Win!' % (player_move, computer_move))
            
            print('PLAYER:' + '*'*PS)
            print('MACHINE:' + '*'*MS)
            print('----')
            
            
        if MS > PS :
            print('Game is Over. Machine wins!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))               
        elif MS < PS :
            print('Game is Over. You win!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))
        else :
            print('Game is Over. Is a tie!')
            print('Final Score: You: %d  Machine: %d' % (PS,MS))
                
    # once the game is finished, the player is asked if he wants to continue playing or close the programm.       
    play_again = input('Press 1 to play again or 2 if you want to quit:')
    while play_again not in play_again_options:
        play_again = input('invalid entry. Play Again: press 1 or Quit: press 2:')
    play_again = int(play_again)
            

    print('GoodBye. Hope you enjoyed the game!') # in case play_again = 2, and the player decides to quit playing.
            
            
            
            
            
            
            
            
            
            