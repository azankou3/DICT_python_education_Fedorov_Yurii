class Coffee:

    def __init__(self, name: object, water: object, milk: object, coffee_beans: object, cups: object, price: object) -> object:
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


machine = Machine_resources(10000, 2000, 500, 60, 100)
espresso = Coffee('espresso', 250, 0, 16, 1, 4)
latte = Coffee('latte', 350, 75, 20, 1, 7)
cappuccino = Coffee('cappuccino', 200, 100, 12, 1, 6)


def greeting():
    print("Welcome to coffee machine")

    print(f'We have\n'
          f'espresso for {espresso.price}-GRN\n'
          f'latte for {latte.price}-GRN\n'
          f'cappuccino for {cappuccino.price}-GRN')

    print('Enter\n1 for espresso\n2 for latte\n3 for cappuccino')
    buyer_input = int(input(">"))
    if int(buyer_input) == 1:
        print('Enter ammount of cups')

        coi = cups_of_coffee_input = int(input('>'))

        if int(coi) > int(machine.cups):
            print('Sorry dont enough cups for this')
        else:
            crw = calculated_resources_water = cups_of_coffee_input * espresso.water
            crm = calculated_resources_milk = cups_of_coffee_input * espresso.milk
            crb = calculated_resources_beans = cups_of_coffee_input * espresso.coffee_beans

            es = machine.water
            em = machine.milk
            eb = machine.coffee_beans

            x = es / crw
            # y = em / crm
            z = eb / crb
            max = min(x, z) - cups_of_coffee_input
            print(f'Yes, I can make that amount of coffee (and even {max} more than that)”,')
            coffee_list = (machine.water, machine.milk, machine.coffee_beans)
            mcoffe_list = (crw, crm, crb)
            if mcoffe_list > coffee_list:
                print("add coffee water or milk")
                filling_machine()
            if int(crw) < int(es) or int(crb) < int(eb) or int(crm) < int(em) or int(coi) < int(machine.cups):
                coffee_making = (f"Starting to make a coffee\nGrinding coffee beans\nBoiling water\n"
                                 f"Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n"
                                 f"Pouring some milk into the cup\nYour {coi} cup of coffee is ready!")
                machine.money = int(espresso.price) * int(coi)
                machine.water = int(es) - int(crw)
                machine.milk = int(em) - int(crm)
                machine.coffee_beans = int(eb) - int(crb)
                machine.cups = int(machine.cups) - int(coi)
                # maxc = max_cups_of_coffee =
                print(int(machine.cups), int(machine.water), int(machine.milk), int(machine.coffee_beans))
                print(coffee_making)

    if int(buyer_input) == 2:
        print('Enter ammount of cups')

        coi = cups_of_coffee_input = int(input('>'))

        if int(coi) > int(machine.cups):
            print('Sorry dont enough cups for this')
        else:
            crw = calculated_resources_water = cups_of_coffee_input * latte.water
            crm = calculated_resources_milk = cups_of_coffee_input * latte.milk
            crb = calculated_resources_beans = cups_of_coffee_input * latte.coffee_beans

            es = machine.water
            em = machine.milk
            eb = machine.coffee_beans

            x = es / crw
            y = em / crm
            z = eb / crb
            cups = min(x, y, z) - cups_of_coffee_input
            print(f'Yes, I can make that amount of coffee (and even {cups} more than that)”,')
            if int(crw) < int(es) or int(crb) < int(eb) or int(crm) < int(em) or int(coi) < int(machine.cups):
                coffee_making = (f"Starting to make a coffee\nGrinding coffee beans\nBoiling water\n"
                                 f"Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n"
                                 f"Pouring some milk into the cup\nYour {coi} cup of coffee is ready!")
                machine.money = int(espresso.price) * int(coi)
                machine.water = int(es) - int(crw)
                machine.milk = int(em) - int(crm)
                machine.coffee_beans = int(eb) - int(crb)
                machine.cups = int(machine.cups) - int(coi)
                # maxc = max_cups_of_coffee =
                print(coffee_making)

    if int(buyer_input) == 3:
        print('Enter ammount of cups')

        coi = cups_of_coffee_input = int(input('>'))

        if int(coi) > int(machine.cups):
            print('Sorry dont enough cups for this')
        else:
            crw = calculated_resources_water = cups_of_coffee_input * cappuccino.water
            crm = calculated_resources_milk = cups_of_coffee_input * cappuccino.milk
            crb = calculated_resources_beans = cups_of_coffee_input * cappuccino.coffee_beans

            es = machine.water
            em = machine.milk
            eb = machine.coffee_beans

            x = es / crw
            y = em / crm
            z = eb / crb
            cups = (min(x, y, z)) - cups_of_coffee_input
            print(f'Yes, I can make that amount of coffee (and even {cups} more than that)”,')
            if int(crw) < int(es) or int(crb) < int(eb) or int(crm) < int(em) or int(coi) < int(machine.cups):
                coffee_making = (f"Starting to make a coffee\nGrinding coffee beans\nBoiling water\n"
                                 f"Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n"
                                 f"Pouring some milk into the cup\nYour {coi} cup of coffee is ready!")
                machine.money = int(espresso.price) * int(coi)
                machine.water = int(es) - int(crw)
                machine.milk = int(em) - int(crm)
                machine.coffee_beans = int(eb) - int(crb)
                machine.cups = int(machine.cups) - int(coi)
                # maxc = max_cups_of_coffee =
                print(coffee_making)


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
