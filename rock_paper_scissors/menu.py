'''
Menu for rock paper scissors
'''
import random

line70 = ['-']
line70 = line70 * 70

def Menu():
    """

    """
    user_name = input("Введіть ваше ім'я: ")
    user_score = 0

    with open('rating.txt', 'r') as file:
        lines = file.readlines()
        print(type(lines))
        for line in lines:
            name, score = line.strip().split()

            if user_name in line:
                user_score = score

                print(user_score is score)
                print(line)
                user_score = score
                print(user_score is score)

            elif user_name not in lines:
                user_name = user_name
                user_score = 0

    print(user_name)
    print(user_score)
    max_rounds = 0
    choice = ['rock', 'paper', 'scissors']
    all = ['help', '!save', '!modes', '!exit']
    print('Welcome to Rock Paper Scissors Plus Ultra')
    print(f'Hello {user_name}')
    while True:
        print(*line70)
        option_print ='Enter your option\n'
        help_print = 'for help enter (help)'
        player_choice = input(f'{option_print}{help_print}\n>')
        if player_choice.lower().strip() == 'help':
            game_help = 'Enter\n(!save) for saving rating\n(!modes) for list of modes\n(!exit) for exit game'
            print(game_help)
        elif player_choice.lower().strip() == '!save':
            with open('rating.txt', 'a') as file:
                file.write(f'\n{user_name}, {user_score}')
        elif player_choice.lower().strip() == '!exit':
            print('bye!')
            break
        elif player_choice.lower().strip() == '!modes' or player_choice.lower().strip() == '!mode':
            print('(!standard) only rock, paper, scissors')
            print('(!ultimate) - all 15 is on')
        elif player_choice.lower().strip() == '!standard':
                                    #"""Standard mode is pure 'rock paper scissors' mode"""
            print('five rounds standard mode')
            max_rounds += 5
            while max_rounds > 0:
                print(f'You`re score is = {user_score}')
                variants = ['paper', 'scissors', 'rock']
                variants = variants * 3
                print(*line70)
                                    #'''Print line70 makes line for more beauty for terminal'''
                print('Please enter your choice from list below')
                print('rock, paper, scissors')
                computer_input = random.randint(3, 7)
                                    #'''computer input is random picker for rock paper scissors'''
                player_input = input('>').strip().lower()
                win = variants[(computer_input + 1): (computer_input + 2)]
                                    #'''win is variants of win conditions'''
                # print(win)
                lose = variants[(computer_input - 1): computer_input]
                                    #'''lose is variants of lose conditions'''
                # print(lose)

                print(f'You chose - {player_input}')
                if player_input == variants[computer_input]:
                    print(f'There is draw, computer and you chose - {player_input}')
                    print('This is draw')
                    user_score = int(user_score) + 50

                elif player_input in lose:
                    print(variants[0], variants[1], variants[2], variants[3])
                    print(f'Sorry, but computer chose {variants[computer_input]}')
                    print('You lose')
                elif player_input in win:
                    print(f'Well done.\nThe computer chose - {variants[computer_input]} and failed')
                    print('You win')
                    user_score = int(user_score) + 100

                else:
                    print('Error\nIncorrect input')
                max_rounds -= 1


        elif player_choice.lower().strip() == '!ultimate':
            print('five rounds ultimate mode')
            max_rounds += 5
            while max_rounds > 0:
                print(f'You`re score is = {user_score}')
                variants = ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree',
                            'human',
                            'snake', 'scissors', 'fire', 'rock']
                variants = variants * 3
                print(*line70)
                print('\nPlease enter your choice from list below')
                print(
                    'gun, lightning, devil\ndragon, water, air\npaper, sponge, wolf\ntree, human, snake\nscissors, fire, rock\n')
                computer_input = random.randint(14, 28)
                player_input = input('>').strip().lower()
                win = variants[(computer_input + 1): (computer_input + 8)]
                lose = variants[(computer_input - 7): computer_input]

                print(f'You chose - {player_input}')
                if player_input == variants[computer_input]:
                    print(f'There is draw, computer and you chose - {player_input}')
                    print('This is draw')
                    user_score = int(user_score) + 50
                elif player_input in lose:
                    print(f'Sorry, but computer chose {variants[computer_input]}')
                    print('You lose')
                elif player_input in win:
                    print(f'Well done.\nThe computer chose - {variants[computer_input]} and failed')
                    print('You win')
                    user_score = int(user_score) + 100
                else:
                    print('Error\nIncorrect input')
                max_rounds -= 1

        elif player_choice not in all:
            print(f'Try to use')
            for i in all:
                print(i)
            else:
                print('')



Menu()
