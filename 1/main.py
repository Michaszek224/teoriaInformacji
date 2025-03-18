import random
x = 1000000
word = ""
for i in range(x):
    randomNumber = random.randint(97,123)
    if randomNumber == 123:
        randomNumber = 32
    word += chr(randomNumber)
    print(chr(randomNumber), end='')

words = []

currentWord = ""
for i in range(x):

    if word[i] == " " and currentWord != "":
        words.append(currentWord)
        currentWord = ""
    else:
        currentWord += word[i]

print("\n",len(words))
print(x / len(words))