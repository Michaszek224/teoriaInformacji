import math
from collections import Counter

def openFile(path):
    """Otwiera plik i zwraca jego zawartosc"""
    with open(path, "r") as f:
        return f.read()

def entropia(tekst):
    """Funkcja obliczajaca entropie dla podanego tekstu"""
    entropia = 0
    counter = Counter(tekst)
    for znak in counter:
        p = counter[znak] / len(tekst)
        entropia += -p * math.log2(p)
    return entropia

def entropiaSlow(tekst):
    """Funkcja obliczająca entropię słów w tekście"""
    slowa = tekst.split()
    counter = Counter(slowa)
    total = sum(counter.values())
    entropia = 0
    for count in counter.values():
        p = count / total
        entropia += -p * math.log2(p)
    return entropia


def entropiaLaczna(tekst, n):
    """Funkcja obliczajaca entropie laczna"""
    pair_counter = Counter(tekst[i:i+n] for i in range(len(tekst) - n + 1))
    entropia = 0
    total = sum(pair_counter.values())
    for pair in pair_counter:
        p = pair_counter[pair] / total
        entropia += -p * math.log2(p)
    return entropia

def entropiaWarunkowa(tekst, n):
    """Funkcja obliczająca entropie warunkowa dla danego rzedu n"""
    laczna = entropiaLaczna(tekst, n+1)
    zwykla = entropiaLaczna(tekst, n)
    return laczna - zwykla

def wyliczenieEntropi(tekst, nazwa, rzad=5):
    """Funkcja obliczajaca entropie dla znakow i slow w podanym tekscie"""
    wikiEnEntropia = entropia(tekst)
    print(f"Entropia dla znakow {nazwa}: {wikiEnEntropia}")

    wikiEnEntropiaSlowa = entropiaSlow(tekst)
    print(f"Entropia dla slow {nazwa}: {wikiEnEntropiaSlowa}")

    for i in range(1, rzad+1):
        print(f"Entropia warunkowa dla {nazwa} rzedu {i}: {entropiaWarunkowa(tekst, i)}")
    print()

wikiEn = openFile("daneFolder/norm_wiki_en.txt")
wyliczenieEntropi(wikiEn, "wikiEn", 6)

wikiLo = openFile("daneFolder/norm_wiki_la.txt")
wyliczenieEntropi(wikiLo, "wikiLo", 6)

sample0 = openFile("daneFolder/sample0.txt")
wyliczenieEntropi(sample0, "sample0", 6)

sample1 = openFile("daneFolder/sample1.txt")
wyliczenieEntropi(sample1, "sample1", 6)

sample2 = openFile("daneFolder/sample2.txt")
wyliczenieEntropi(sample2, "sample2", 6)

sample3 = openFile("daneFolder/sample3.txt")
wyliczenieEntropi(sample3, "sample3", 6)

sample4 = openFile("daneFolder/sample4.txt")
wyliczenieEntropi(sample4, "sample4", 6)

sample5 = openFile("daneFolder/sample5.txt")
wyliczenieEntropi(sample5, "sample5", 6)

#wynik programu: