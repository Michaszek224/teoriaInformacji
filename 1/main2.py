import random

hamlet = open("norm_hamlet.txt").read()
romeo = open("norm_romeo.txt").read()
wiki = open("norm_wiki_sample.txt").read()
# print(hamlet)
allText = hamlet + romeo + wiki

hamletLen = len(hamlet)
romeoLen = len(romeo)
wikiLen = len(wiki)
textLen = len(allText)

wordsHamlet = {}
wordsRomeo = {}
wordsWiki = {}
wordsText = {}

for word in range(len(allText)):
    if allText[word] in wordsText:
        wordsText[allText[word]] += 1
    else:
        wordsText[allText[word]] = 1

for word in wordsText:
    wordsText[word] = wordsText[word] / textLen * 100

print("text",wordsText,"\n")

letter, probability = zip(*wordsText.items())

for i in range(100000):
    currentLetter = random.choices(letter, probability)
    print(currentLetter[0], end="")