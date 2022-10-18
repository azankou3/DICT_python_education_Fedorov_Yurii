import random

greetings = ("HANGMAN \nThe game will be avalible soon.")
print(greetings)

HANGMAN = [0, 1, 2, 3, 4, 5, 6, 7,]

max_wrong = len(HANGMAN)
words = ["python", "java", "php", "javascript", "ruby", "c++", "c", "html"]

word = random.choice(words)

print(f"You`re max mistake is {max_wrong}")

word_apperance = '_' * len(word)
wrong = 0
used = []

while wrong < max_wrong and word_apperance != word:
    print("youre mistake",HANGMAN[wrong])
    print('\nUsed letter:', used)
    print('\nword looks like\n', word_apperance)

    guess = input('>')

    while guess in used:
        print('This letter can`t be used again', guess)
        guess = input('Pick another letter\n>')

    used.append(guess)

    if guess in word:
        print(guess, 'is in the word')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += word_apperance[i]
        word_apperance = new
    else:
        print(f'\n{guess} is wrong letter')
        wrong += 1

if wrong == max_wrong:
    print('\n You`re dead')
else:
    print('\nYou survived')

print(f'\nConceived word is {word} ')
