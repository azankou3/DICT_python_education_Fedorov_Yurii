"""rock paper scissors by Fedorov """
import random


def rock_paper_scissors():
    choice = ['rock', 'paper', 'scissors']
    all = ['help', '!save', '!exit', choice]
    wins = 0
    loses = 0
    draws = 0
    rating_points = 0
    while True:
        print(f'\nyour statistics\nwins - {wins}\nloses - {loses}\ndraws - {draws}\npoints - {rating_points}')
        option_print =(f'Enter your option\n{choice[0]}, {choice[1]}, {choice[2]}\n')
        help_pirnt = 'for help enter (help)'
        player_choice = input(f'{option_print}{help_pirnt}\n>')
        if player_choice.lower().strip() == 'help':
            game_help = 'Enter\n(!save) for saving rating\n(!exit) for exit game'
            print(game_help)
        elif player_choice.lower().strip() == '!save':
            print('Want save your results')
            results_choice = input('yes or no\n>')
            if results_choice.lower().strip() == 'yes' or results_choice.lower().strip() == 'y':
                players_name = input('Enter your name\n>')
                with open(f"rating.txt", "a") as text_write:
                    text_write.write(f"\n{players_name} wins = {wins} loses = {loses} draws = {draws}")
        elif player_choice.lower().strip() == '!exit':
            print('bye!')
            break

        computer_choice = random.choice(choice)
        if player_choice == 'rock':
            if player_choice == 'rock' and computer_choice == 'scissors':
                result = f'Well done.\nThe computer chose {computer_choice} and failed'
                print(result)
                wins += 1
                rating_points += 100
            elif player_choice == 'rock' and computer_choice == 'rock':
                result = f'There is draw ({player_choice})'
                print(result)
                draws += 1
                rating_points += 50
            elif player_choice == 'rock' and computer_choice == 'paper':
                result = f'Sorry, but computer chose {computer_choice}'
                print(result)
                loses += 1
        elif player_choice == 'paper':
            if player_choice == 'paper' and computer_choice == 'rock':
                result = f'Well done.\nThe computer chose {computer_choice} and failed'
                print(result)
                wins += 1
                rating_points += 100
            elif player_choice == 'paper' and computer_choice == 'paper':
                result = f'There is draw ({player_choice})'
                print(result)
                draws += 1
                rating_points += 50
            elif player_choice == 'paper' and computer_choice == 'scissors':
                result = f'Sorry, but computer chose {computer_choice}'
                print(result)
                loses += 1
        elif player_choice == 'scissors':
            if player_choice == 'scissors' and computer_choice == 'paper':
                result = f'Well done.\nThe computer chose {computer_choice} and failed'
                print(result)
                wins += 1
                rating_points += 100
            elif player_choice == 'scissors' and computer_choice == 'scissors':
                result = f'There is draw ({player_choice})'
                print(result)
                draws += 1
                rating_points += 50
            elif player_choice == 'scissors' and computer_choice == 'rock':
                result = f'Sorry, but computer chose {computer_choice}'
                print(result)
                loses += 1
        elif player_choice not in all:
            print(f'Try to use')
            for i in choice:
                print(i)
            else:
                print('')


rock_paper_scissors()
