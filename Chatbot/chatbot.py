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

proving_that_bot_can_count = ("Now i will prove to you that I can count any number you want.")
completed_counting = ("Completed, have a nice day!")
print(proving_that_bot_can_count)
countinput = (int(input(">")))
count = 0
while count < countinput:
    count = count + 1
    print(f"{count}!")

print(completed_counting)



