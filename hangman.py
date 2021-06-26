finished = False
word = ""
wordList = []
answerKey = []
guess = ""
valid = True
rightGuess = 0
wrongGuess = False
lives = 7

word = input("Enter a word. ")
    
for x in range(len(word)):
    answerKey.append(word[x])

for x in range(len(word)):
    wordList.append("_")
print(' '.join(wordList))

while(not finished):
    guess = input("Enter a letter. ")
    valid = True
    if(len(guess) != 1):
        print("That guess is not valid.")
        valid = False
        print(' '.join(wordList))
    if(valid):
        for x in range(len(word)):
            if(word[x] == guess):
                wordList[x] = guess
                rightGuess += 1
            else:
                wrongGuess = True
        if(wrongGuess == True and rightGuess == 0):
            lives -= 1
            print("That letter is not in the given word, attempts left: " + str(lives))
        else:
            wrongGuess = False
            rightGuess = 0
        print(' '.join(wordList))
    if(lives == 0):
            print("You failed to guess the word")
            finished = True
    if(answerKey == wordList):
            print("You have guessed the word: " + word)
            finished = True

