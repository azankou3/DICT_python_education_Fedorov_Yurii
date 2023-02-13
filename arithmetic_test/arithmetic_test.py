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
            # Random_test.random_number(Random_test)
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
                print(f'Your mark is {marks}/{number_of_tests}')
                pass
        pass

if __name__ == '__main__':
    Random_test.second_stage(Random_test)
