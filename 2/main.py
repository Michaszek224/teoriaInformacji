import random
from collections import defaultdict

def tokenize(text):
    """ Dzieli tekst na słowa """
    return text.split()

def build_markov_model(words, order=1):
    """ Tworzy model Markova dla danego tekstu i rzędu """
    model = defaultdict(lambda: defaultdict(int))
    
    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])
        next_word = words[i+order]
        model[prefix][next_word] += 1
    
    # Normalizacja do prawdopodobieństw
    for prefix, transitions in model.items():
        total = sum(transitions.values())
        model[prefix] = {word: count/total for word, count in transitions.items()}
    
    return model

def generate_text(model, order=1, seed=None, length=200):
    """ Generuje losowy tekst na podstawie modelu Markova """
    if seed is None:
        seed = random.choice(list(model.keys()))
    elif isinstance(seed, str):
        seed_words = seed.split()
        if len(seed_words) < order:
            # Szukaj prefiksów zaczynających się od podanych słów
            possible_prefixes = [p for p in model.keys() if p[:len(seed_words)] == tuple(seed_words)]
            if possible_prefixes:
                seed = random.choice(possible_prefixes)
            else:
                seed = random.choice(list(model.keys()))
        else:
            seed = tuple(seed_words[:order])
    
    output = list(seed)
    
    for _ in range(length - order):
        if seed not in model:
            break
        next_word = random.choices(
            list(model[seed].keys()), 
            weights=model[seed].values()
        )[0]
        output.append(next_word)
        seed = tuple(output[-order:])
    
    return ' '.join(output)


#wczytywanie tekstu
with open("norm_hamlet.txt") as f:
    hamlet = f.read()

with open("norm_romeo.txt") as f:
    romeo = f.read()

with open("norm_wiki_sample.txt") as f:
    wiki = f.read()

text = hamlet + romeo + wiki

# Budowanie modeli
words = tokenize(text)
markov_1 = build_markov_model(words, order=1)
markov_2 = build_markov_model(words, order=2)

# Generowanie tekstu
print("Pierwszy rząd:")
print(generate_text(markov_1, order=1))

print("\nDrugi rząd:")
print(generate_text(markov_2, order=2))

print("\nDrugi rząd od 'probability':")
print(generate_text(markov_2, order=2, seed="probability"))
