import random
import operator

class Random_test:
    def __init__(self):
        pass
# #Easy test
#     def random_number(self):
#         x = random.randrange(2, 10)
#         y = random.randrange(2, 10)
#         sign_list = {'+': operator.add,
#                      '-': operator.sub,
#                      '*': operator.mul}
#         sign = random.choice(list(sign_list.keys()))
#         res = (x, sign, y)
#         answer = (sign_list.get(sign)(x, y))
#         print(*res)
#         print(answer)
#         client_input = int(input('>'))
#         if client_input == answer:
#             print('Right!')
#         else:
#             print('Wrong!')

#Second stage
    def second_stage(self):
        marks = 0
        tests = 0
        number_of_tests = 5
        while tests < number_of_tests:
            tests = tests + 1
            x = random.randrange(2, 10)
            y = random.randrange(2, 10)
            sign_list = {'+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul}
            sign = random.choice(list(sign_list.keys()))
            res = (x, sign, y)
            answer = (sign_list.get(sign)(x, y))
            print(*res)
            print(answer)
            client_input = int(input('>'))
            if client_input == answer:
                print('Right!')
                marks = marks + 1
            else:
                print('Wrong!')
            if tests == number_of_tests:
                final = (f'Your mark is {marks}/{number_of_tests}')
                print(final)
                print("Would you like to save your result to file\nEnter\n1.yes\n2.no")
                results_file_input = input('>')
                if results_file_input == "1":
                    with open("Results File.txt","a") as text_write:
                        text_input = input("Enter your name: >")
                        text_input_group = input("Enter your group")
                        text_write.write(f"\n\n{text_input} {text_input_group}"
                                         f" Simple arithmetic operations with numbers from 2 to 9-{final}")
                else:
                    Menu.welcome(Menu)


#Thir stage
    def thrid_stage(self):
        marks = 0
        tests = 0
        number_of_tests = 5
        while tests < number_of_tests:
            tests = tests + 1
            x = random.randrange(11, 29)
            res = (f'{x}^2')
            answer = (x**2)
            print(res)
            print(answer)
            client_input = int(input('>'))
            if client_input == answer:
                print('Right!')
                marks = marks + 1
            else:
                print('Wrong!')
            if tests == number_of_tests:
                final = (f'Your mark is {marks}/{number_of_tests}')
                print(final)
                print("Would you like to save your result to file\nEnter\n1.yes\n2.no")
                results_file_input = input('>')
                if results_file_input == "1":
                    with open("Results File.txt", "a") as text_write:
                        text_input = input("Enter your name: >")
                        text_input_group = input("Enter your group")
                        text_write.write(f"\n\n{text_input} {text_input_group}"
                                         f" Squaring numbers from 11 to 29-{final}")
                else:
                    Menu.welcome(Menu)


class Menu:
#Start menu
    def welcome(self):
        print('Виберіть рівень складності\n'
              '1. Прості арифметичні операції з числами від 2 до 9\n'
              '2. Зведення у квадрат чисел від 11 до 29')
        menu_input = input('>')
        if menu_input == '1':
            Random_test.second_stage(Random_test)
        elif menu_input == '2':
            Random_test.thrid_stage(Random_test)
        else:
            print('Enter only numbers from Menu')
            Menu.welcome(Menu)
if __name__ == '__main__':
    Menu.welcome(Menu)
