#Alexander Dolghii
#4/23/2019
#Dolghii_CST_Game.py
#Program designed to simulate a rock paper scissors game using simple geometric shapes


from easygui import *     #Imports the easyGUI interface so program can display visuals
import random   #Imports random library so computer can randomly pick an option

Flag = True   #Enables menu loop

while Flag == True:  #Begins loop to run menu to get user input
    program_title = 'Circle Square Triangle: A RPS Game'   #Creates variable to display program title in easyGUI interface
    options = ['PLAY','HELP','QUIT']  #Creates variable to set different options user can click
    user_choice = buttonbox('Welcome to Circle Square Triangle!',program_title,options,image='./Dolghii_CST_Logo.jpg')   #Gets user choice through a buttonbox easyGUI interface
    if user_choice == 'PLAY':  #If user clicks play button, this will display
        Flag_user = True   #Enables main program loop
        Flag = False   #Ends main menu loop so program can start
    elif user_choice == 'HELP':  #If user clicks help, this will display
        user_help = 'Last Updated: May 1, 2019 \n \n This game is a different version of the popular game Rock Paper Scissors. Circle beats triangle, triangle beats square, and square beats circle. The winner is decided by best of 3. If a draw happens, the turn will be repeated. Have fun! \n \n Made By: Alexander Dolghii'
        msgbox(user_help,program_title)  #Displays to user information about program
        Flag_user = False   #Disables main program loop from starting
    elif user_choice == 'QUIT':  #If user clicks quit, this will display
        msgbox('Thanks for playing!',program_title)
        Flag_user = False  #Ends both loops so program can close
        Flag = False
    else:  #If error happens, this will display
        print('Error')


    while Flag_user == True:  #Main program loop begins

        def playerTurn(title):  #Creates function to get player input for their turn in the game
            turn_choices = ['Circle','Square','Triangle','Random']   #Creates list to set different option user can pick to act as their turn
            turn_choice = buttonbox('Your Turn!',title,turn_choices,image='./Dolghii_CST_Logo.jpg')  #Asks user to pick their action for the current turn
            if turn_choice == 'Random':   #If user chooses random, this will display
                turn_choice = random.randint(1,3)  #Program chooses a random number between 1 and 3
                if turn_choice == 1:  #If program chooses 1, this will display
                    turn_choice = 'Circle'  #Sets turn action to circle
                    msgbox(' ',title,image='./Dolghii_user_circle.jpg')   #Outputs to user their turn action
                elif turn_choice == 2:  #If program chooses 2, this will display
                    turn_choice = 'Square'  #Sets turn action to square
                    msgbox(' ',title,image='./Dolghii_user_square.jpg')  #Outputs to user their turn action
                elif turn_choice == 3:  #If program chooses 3, this will display
                    turn_choice = 'Triangle'   #Sets turn action to triangle
                    msgbox(' ',title,image='./Dolghii_user_triangle.jpg')   #Outputs to user their turn action
                else:
                    print('Error')
            return turn_choice  #Returns player choice to variable

        def cpuTurn(title):  #Creates function to get computer's input for their turn in the game
            cpu_turn = random.randint(1,3)   #Program chooses random number between 1 and 3 to decide turn action
            if cpu_turn == 1:  #If program chooses 1, this will display
                msgbox(' ',title,image='./Dolghii_cpu_circle.jpg')   #Outputs to user computer's turn action
                cpu_turn = 'Circle'  #Sets value to computer's choice
                return cpu_turn  #Returns value to variable
            elif cpu_turn == 2:  #If program chooses 2, this will display
                msgbox(' ',title,image='./Dolghii_cpu_square.jpg')   #Outputs to user computer's turn action
                cpu_turn = 'Square'   #Sets value to computer's choice
                return cpu_turn   #Returns value to variable
            elif cpu_turn == 3:   #If program chooses 3, this will display
                msgbox(' ',title,image='./Dolghii_cpu_triangle.jpg')   #Outputs to user computer's turn action
                cpu_turn = 'Triangle'   #Sets value to computer's choice
                return cpu_turn   #Returns value to variable
            else:   #If anything else happens, error message will occur
                print('Error')

        def roundWinner(player,cpu,title):   #Creates function to determine current round winner
            if player == cpu:  #If player's choice is the same as the computer's choice, this will display
                game = 'Draw'   #Sets round outcome variable to a tie
            elif player == 'Circle' and cpu == 'Square':   #If player chooses circle and program chooses square, this will display
                game = 'Lose'   #Sets round outcome variable to a loss for player
            elif player == 'Square' and cpu == 'Triangle':   #If player chooses square and program chooses triangle, this will display
                game = 'Lose'   #Sets round outcome variable to a loss for player
            elif player == 'Triangle' and cpu == 'Circle':   #If player chooses triangle and program chooses circle, this will display
                game = 'Lose'   #Sets round outcome variable to a loss for player
            elif player == 'Square' and cpu == 'Circle':  #If player chooses sqaure and program chooses circle, this will display
                game = 'Win'   #Sets round outcome variable to a win for player
            elif player == 'Triangle' and cpu == 'Square':  #If player chooses triangle and program chooses square, this will display
                game = 'Win'   #Sets round outcome variable to a win for player
            elif player == 'Circle' and cpu == 'Triangle':   #If player chooses circle and program chooses triangle, this will display
                game = 'Win'   #Sets round outcome variable to a win for player
            return game   #Returns value to variable

        player_score = 0  #Sets user score tracker 
        computer_score = 0  #Sets computer score tracker
        game_length = 3   #Sets game length variable
        
        while game_length > 0:   #Loop begins to run the game until user or computer wins
            player_choice = playerTurn(program_title)   #Calls function to get player action for their turn
            computer_choice = cpuTurn(program_title)   #Calls function to get program action for turn
            round_winner = roundWinner(player_choice,computer_choice,program_title)  #Calls function to take user and program action and determine's round winner
            if round_winner == 'Win':   #If function returns win, this will display
                player_score = player_score + 1  #Adds one point to user score tracker
                msgbox(player_choice + ' VS. ' + computer_choice + '\n \n You win this round!' + '\n \n Computer Score: ' + str(computer_score) + '\n Player Score: ' + str(player_score),program_title)  #Outputs to user the round outcome
            elif round_winner == 'Lose':   #If function returns lose, this will display
                computer_score = computer_score + 1  #Adds one point to computer score tracker
                msgbox(player_choice + ' VS. ' + computer_choice + '\n \n You lose this round.' + '\n \n Computer Score: ' + str(computer_score) + '\n Player Score: ' + str(player_score),program_title)   #Outputs to user the round outcome
            elif round_winner == 'Draw':   #IF function returns draw, this will display
                msgbox(player_choice + ' VS. ' + computer_choice + '\n \n Draw! Play again.' + '\n \n Computer Score: ' + str(computer_score) + '\n Player Score: ' + str(player_score),program_title)  #Outputs to user the round outcome
            else:   #If error occurs, error message will display
                print('Error')
            
            if player_score == 2:   #If the user's score tracker reaches 2, this will display
                msgbox(' ',program_title,image='./Dolghii_you_win.jpg')   #Outputs to user that they have won
                Flag_user = False  #Ends main program loop
                Flag = True  #Begins main menu loop
                game_length = 0   #Ends game loop 
            elif computer_score == 2:   #If the program's score tracker reaches 2, this will display
                msgbox(' ',program_title,image='./Dolghii_you_lose.jpg')   #Outputs to user that the program has won
                Flag_user = False   #Ends main program loop
                Flag = True  #Begins main menu loop
                game_length = 0   #Ends game loop
            
        
        
        
        
