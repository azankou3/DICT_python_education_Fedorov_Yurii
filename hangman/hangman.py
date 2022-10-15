import random

greetings = ("HANGMAN \nThe game will be avalible soon.")
print(greetings)

HANGMAN = [0, 1, 2, 3, 5, 6, 7]

max_wrong = len(HANGMAN)

words = ["python", "java", "php", "javascript"]
word = random.choice(words)


