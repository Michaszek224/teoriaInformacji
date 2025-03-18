import random
import string

x = 1_000_000  # Liczba znaków do wygenerowania
letters = string.ascii_lowercase + " "  # 26 liter + spacja

# Generowanie losowego tekstu
word = "".join(random.choices(letters, k=x))

# Podział na słowa i liczenie ich długości
words = word.split()
total_letters = sum(len(w) for w in words)  # Suma liter we wszystkich słowach
avg_word_length = total_letters / len(words)  # Średnia długość słowa (bez spacji)

print(words)

print(f"\nLiczba słów: {len(words)}")
print(f"Średnia długość słowa (bez spacji): {avg_word_length:.2f}")
