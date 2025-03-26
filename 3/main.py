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

def wyliczenieEntropi(tekst):
    """Funkcja obliczajaca entropie dla znakow i slow w podanym tekscie"""
    wikiEnEntropia = entropia(wikiEn)
    print(f"Entropia dla znakow wiki_en: {wikiEnEntropia}")

    wikiEnSlowa = wikiEn.split()
    wikiEnEntropiaSlowa = entropia(wikiEnSlowa)
    print(f"Entropia dla slow wiki_en: {wikiEnEntropiaSlowa}")

def entropiaLaczna(tekst, n):
    """Funkcja obliczajaca entropie laczna"""
    pair_counter = Counter(wikiEn[i:i+n] for i in range(len(wikiEn) - n + 1))
    entropia = 0
    for pair in pair_counter:
        p = pair_counter[pair] / len(wikiEn)
        entropia += -p * math.log2(p)
    return entropia

def entropiaWarunkowa(tekst, n):
    """Funkcja obliczająca entropie warunkowa dla danego rzedu n"""


wikiEn = openFile("daneFolder/norm_wiki_en.txt")
wyliczenieEntropi(wikiEn)

for i in range(1, 6):
    print(f"Entropia laczna dla n={i}: {entropiaLaczna(wikiEn, i)}")