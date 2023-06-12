# Word Guessig game using Python

# 1. The Word Guessig game program randomly selects a secrete word from a list of secret words. The random module will provide this ability.
# 2. The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game. 
# 3. When a letter in that word is guessed correctly, that letter position in the word is made visible. In his way, all letters of the word are to be guessed before all th chances are over.
# 4. For convenience, we have given length of word +2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

# Code:

import random 
# from collections import Counter

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ') # gives a List of fruits

word = random.choice(someWords) # randomly choose a secret word from our "someWords" LIST


print('Guess the word! HINT: word is a name of a fruit')

for _ in word:
    # For printing the empty spaces for letters of the word 
    print('_', end=' ')
print()

playing = True
# List for storing the letters guessed by the player
letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0

try:
    while (chances!=0) and flag == 0: # flag is updated when the word is correctly guessed 
        print()
        chances-=1

        try:
            guess = str(input('Enter a letter to guess: ')) 
        except:
            print('Enter only a Letter!')
            continue

        if not guess.isalpha():
            print('Enter only a Letter!')
            continue
        elif len(guess) > 1 or len(guess) <= 0:
            print('Enter only a Single Letter!')
            continue
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        if guess in word:
            k = word.count(guess)
            for _ in range(k):
                letterGuessed+=guess

        for i in range(len(word)):
            if (word[i] == guess) or (word[i] in letterGuessed):
                print(word[i],end=' ')
            else:
                print('_',end=' ')

        print()

        if len(letterGuessed) == len(word):
            print("Congratulations, you did it! word is",word)
            flag = 1 

except KeyboardInterrupt:
    print("Bye")


                
