class Coffee:

    def __init__(self, name, water, milk, coffee_beans, cups, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.price = price


class Machine_resources:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money


machine = Machine_resources(1000, 600, 1000, 60, 100)
espresso = Coffee('espresso', 250, 0, 16, 1, 4)
latte = Coffee('latte', 350, 75, 20, 1, 7)
cappuccino = Coffee('cappuccino', 200, 100, 12, 1, 6)

print(machine.water)


def greeting():
    print("Welcome to coffee machine")
    print(f'We have\n'
          f'espresso for {espresso.price}-GRN\n'
          f'latte for {latte.price}-GRN\n'
          f'cappuccino for {cappuccino.price}-GRN')
    print('Enter\n1 for espresso\n2 for latte\n3 for cappuccino')
    buyer_input = int(input(">"))
    if buyer_input == 1:
        print('Enter ammount of cups')
        cups_of_coffee_input = int(input('>'))
        if cups_of_coffee_input > machine.cups:
            print('Sorry dont enough cups for this')
        calculated_resources_water = cups_of_coffee_input * espresso.water
        calculated_resources_milk = cups_of_coffee_input * espresso.milk
        calculated_resources_beans = cups_of_coffee_input * espresso.coffee_beans
        if int(calculated_resources_water) <= int(espresso.water) and int(calculated_resources_beans) <= int(espresso.coffee_beans) and int(calculated_resources_milk) <= int(espresso.milk):
            print("Starting to make a coffee\n"
            "Grinding coffee beans\n"
            "Boiling water\n"
            "Mixing boiled water with crushed coffee beans\n"
            "Pouring coffee into the cup\n"
            "Pouring some milk into the cup\n"
            "Coffee is ready!")



def filling_machine():
    print('Write how many ml of water you want to add')
    fill_water = int(machine.water) + int(input('>'))
    filled_machine = Machine_resources(fill_water,
                                (),
                                (),
                                (),
                                ())


    print('Write how many ml of milk you want to add')
    fill_milk = int(machine.milk) + int(input('>'))
    filled_machine = Machine_resources(fill_water,
                                fill_milk,
                                (),
                                (),
                                ())


    print('Write how many gr of coffee beans you want to add')
    fill_coffee_beans = int(machine.coffee_beans) + int(input('>'))
    filled_machine = Machine_resources(fill_water,
                                fill_milk,
                                fill_coffee_beans,
                                (),
                                ())


    print('Write how many of cups you want to add')
    fill_cups = int(machine.cups) + int(input('>'))
    filled_machine = Machine_resources(fill_water,
                                fill_milk,
                                fill_coffee_beans,
                                fill_cups,
                                ())
    print(f'Machine now conatains\n'
          f'{filled_machine.water} ml of water,\n'
          f'{filled_machine.milk} ml of milk,\n'
          f'{filled_machine.coffee_beans} gr of beans\n'
          f'{filled_machine.cups} cups')
    machine.water = filled_machine.water
    machine.milk = filled_machine.milk
    machine.coffee_beans = filled_machine.coffee_beans
    machine.cups = filled_machine.cups

def taking_money():
    print(f'In coffee machine now {machine.money}\nEnter ammount to take')
    entering_ammount = input('>')
    if int(entering_ammount) > int(machine.money):
        print("In machine is not enough money")
    elif int(entering_ammount) <= int(machine.money):
        money = int(machine.money) - int(entering_ammount)
        machine.money = money
        print(f'Now in machine is {int(machine.money)}')



def proccessing():
    print(f'What action (buy, fill, take)')
    user_input = input('>')

    if user_input == 'buy':
        introduction = greeting()

    elif user_input == 'fill':
        fill = filling_machine()

    elif user_input == 'take':
        taking_money_from_machine = taking_money()


def coffee_machine():
    menu = proccessing()
    # introduction = greeting()



coffee_machine()