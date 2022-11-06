class Coffee:

    def __init__(self, name, water, milk, coffee_beans, cups, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.price = price
        print(self.name)
        print(f'{self.price}-grn')


class Coffee_machine_resources:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

# espresso_coffee = Coffee('espresso', 350, 75, 20, 1, 4)
espr = Coffee('espresso', 350, 75, 20, 1, 4)

