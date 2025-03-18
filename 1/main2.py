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

# for word in range(len(hamlet)):
#     if hamlet[word] in wordsHamlet:
#         wordsHamlet[hamlet[word]] += 1
#     else:
#         wordsHamlet[hamlet[word]] = 1

# for word in range(len(romeo)):
#     if romeo[word] in wordsRomeo:
#         wordsRomeo[romeo[word]] += 1
#     else:
#         wordsRomeo[romeo[word]] = 1

# for word in range(len(wiki)):
#     if wiki[word] in wordsWiki:
#         wordsWiki[wiki[word]] += 1
#     else:
#         wordsWiki[wiki[word]] = 1

for word in range(len(allText)):
    if allText[word] in wordsText:
        wordsText[allText[word]] += 1
    else:
        wordsText[allText[word]] = 1

# for word in wordsHamlet:
#     wordsHamlet[word] = wordsHamlet[word] / hamletLen * 100

# for word in wordsRomeo:
#     wordsRomeo[word] = wordsRomeo[word] / romeoLen * 100

# for word in wordsWiki:
#     wordsWiki[word] = wordsWiki[word] / wikiLen * 100

for word in wordsText:
    wordsText[word] = wordsText[word] / textLen * 100

# wordsHamlet = sorted(wordsHamlet.items(), key=lambda x: x[1], reverse=True)
# wordsRomeo = sorted(wordsRomeo.items(), key=lambda x: x[1], reverse=True)
# wordsWiki = sorted(wordsWiki.items(), key=lambda x: x[1], reverse=True)

# print("hamlet",wordsHamlet,"\n")
# print("romeo",wordsRomeo,"\n")
# print("wiki",wordsWiki,"\n")
print("text",wordsText,"\n")

letter, probability = zip(*wordsText.items())

for i in range(100000):
    currentLetter = random.choices(letter, probability)
    print(currentLetter[0], end="")