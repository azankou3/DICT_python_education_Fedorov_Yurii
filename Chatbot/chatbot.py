greetings = ("Hello! My name is R2D2 \nI was created in 2022")
print(greetings)

contact = ("Please remind me your name: ")
print(contact)

name = input(">")

discovername = (f"What a great name you have, {name}")
print(discovername)

guessing_age = ("Let me guess your age? \nEnter remainders of dividing your age by 3, 5 and 7")
print(guessing_age)

remainder3 =int(input(">"))
remainder5 =int(input(">"))
remainder7 =int(input(">"))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
your_age = (f"Your age is, {age} that`s a good time to start programming!")
print(your_age)
