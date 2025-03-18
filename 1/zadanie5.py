import random
import string
from collections import defaultdict

def build_model(text, order):
    """ Tworzy model Markova dla danego tekstu i rzędu """
    model = defaultdict(list)
    
    for i in range(len(text) - order):
        prefix = text[i:i+order]  # Sekwencja znaków (kontekst)
        next_char = text[i+order] # Następny znak
        model[prefix].append(next_char)  # Dodajemy przejście
    
    return model

def generate_text(model, order, length, seed=None):
    """ Generuje losowy tekst na podstawie modelu Markova """
    if seed is None:
        seed = random.choice(list(model.keys()))  # Losowy start
    text = seed
    
    for _ in range(length - len(seed)):
        prefix = text[-order:]  # Pobieramy ostatnie `order` znaków
        if prefix in model:
            next_char = random.choice(model[prefix])  # Losujemy następny znak
        else:
            next_char = " "  # Jeśli brak przejść, dodajemy spację
        text += next_char
    
    return text

def average_word_length(text):
    """ Oblicza średnią długość słowa w tekście (bez spacji) """
    words = text.split()
    total_letters = sum(len(w) for w in words)
    return total_letters / len(words) if words else 0

# 📌 Wczytanie tekstu źródłowego
with open("norm_hamlet.txt") as f:
    hamlet = f.read()

with open("norm_romeo.txt") as f:
    romeo = f.read()

with open("norm_wiki_sample.txt") as f:
    wiki = f.read()

corpus = hamlet + romeo + wiki

# 📌 Generowanie przybliżeń dla różnych rzędów
orders = [1, 3, 5]
length = 5000  # Długość generowanego tekstu

for order in orders:
    model = build_model(corpus, order)
    seed = "probability" if order == 5 else None  # Seed tylko dla 5. rzędu
    generated_text = generate_text(model, order, length, seed)
    
    # 📌 Obliczenie średniej długości słowa
    avg_len = average_word_length(generated_text)
    
    print(f"\n--- Markov {order}-go rzędu ---")
    print(generated_text + "\n")  # Podgląd fragmentu
    print(f"Średnia długość słowa: {avg_len:.2f}")
