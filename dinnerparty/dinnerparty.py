import random

y_or_n = {'y': True, 'n': False}

greeting = ("Hello this is dinnerparty")
dinner_party_info = ("dinnerparty made for sharing the cost of the dinner")

enter_name = ("Enter name of people in the dinnerparty")
enter_number = ("Enter number of people in the dinnerparty\n>")

no_one_is_at_dinnerparty = ("No one enter the dinnerparty")

The_Winning_Hand = ('Wanna to use "The Winning Hand" type\ny/n')

End_of_dinnerparty = ("Thanks for using dinnerparty")

payments = {}

print(f"{greeting} \n{dinner_party_info}")

number_of_members = int(input(f"{enter_number}"))

if number_of_members < 1:
    print(no_one_is_at_dinnerparty)
    exit()

print(enter_name)

for i in range(number_of_members):
    name = input(">")
    payments[name] = 0

total_amount = int(input("Enter amount\n>"))

print(The_Winning_Hand)
lucky = y_or_n[input(">").lower()]
lucky_name = ""

if lucky:
    lucky_name = random.choice(list(payments.keys()))
    print(f"New owner of The Winning Hand is {lucky_name}")

else:
    print("No owners of The Winning Hand")

price = round(total_amount / (number_of_members - int(lucky)), 2)

for p in payments.keys():
    payments[p] = price

if lucky:
    payments[lucky_name] = 0

print(payments)

print(End_of_dinnerparty)
