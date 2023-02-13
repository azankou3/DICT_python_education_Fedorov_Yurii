import random
import operator

# class Random_test:
#     x = random.randrange(2, 10)
#     y = random.randrange(2, 10)
#
#     sign_list = ['+', '-', '*']
#
#     sign = random.choice(sign_list)
#     def __init__(self, x, y, sign):
#         self.x = x
#         self.y = y
#         self.sign = sign
#
#     def __str__(self):
#         return (x, sign, y)
#Random easy test
def random_number():
    x = random.randrange(2, 10)
    y = random.randrange(2, 10)

    sign_list = {'+':operator.add,
                 '-':operator.sub,
                 '*':operator.mul}
    sign = random.choice(list(sign_list.keys()))
    res = (x, sign, y)
    answer = (sign_list.get(sign)(x, y))
    print(*res)
    # print(answer)
    client_input = int(input('>'))
    if client_input == answer:
        print('Right!')
    else:
        print('Wrong!')



print(random_number())
