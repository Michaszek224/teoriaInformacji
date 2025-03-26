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

def entropiaOgolna(tekst):
    """Funkcja obliczajaca entropie dla znakow i slow w podanym tekscie"""
    wikiEnEntropia = entropia(wikiEn)
    print(f"Entropia dla znakow wiki_en: {wikiEnEntropia}")

    wikiEnSlowa = wikiEn.split()
    wikiEnEntropiaSlowa = entropia(wikiEnSlowa)
    print(f"Entropia dla slow wiki_en: {wikiEnEntropiaSlowa}")


    

wikiEn = openFile("daneFolder/norm_wiki_en.txt")
entropiaOgolna(wikiEn)

