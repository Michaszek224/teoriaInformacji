from bitarray import bitarray

def openFile(path):
    """Otwiera plik i zwraca jego zawartosc"""
    with open(path, "r") as f:
        return f.read()

def decToBin(n):
    """Zamienia liczbe dziesietna na binarna"""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decToBin(n // 2) + str(n % 2)

def toBits(n):
    """Zamienia liczbe na binarna i dodaje zera na poczatek"""
    bits = decToBin(n)
    #kod ma 6 bitow
    while len(bits) < 6:
        bits = "0" + bits
    return bits

def create(text):
    """Na podstawie czestotliwosi liter tworzy kod"""
    letters = {}
    #zliczanie czestotliwosci liter
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    #sortowanie liter w kolejnosci od najczestszej
    letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    #tworzenie kodu
    kod = {}
    for i in range(len(letters)):
        kod[letters[i][0]] = toBits(i + 1)
    return kod

def encode(text, kod):
    """Koduje tekst na podstawie kodu"""
    zakodowane = bitarray()
    for letter in text:
        zakodowane.extend(kod[letter])
    return zakodowane 


def decode(text, kod):
    """Dekoduje tekst na podstawie kodu"""
    #odwracanie kodu
    odwr = {v: k for k, v in kod.items()}
    encodedText = ""
    counter = 0
    localText = ""
    for i in text:
        
        if counter == 6:
            encodedText += odwr[localText]
            localText = ""
            counter = 0
        counter += 1
        localText += str(i)
    #dodanie osatnich 6 bitow
    encodedText += odwr[localText]
    return encodedText

def save():
    pass

def load():
    pass

path = "sample.text"
text = openFile(path)
text = text[:1000]

kod = create(text)
encodedText = encode(text, kod)
decodedText = decode(encodedText.tolist(), kod)

print("Kod:", kod, "\n")
print("Zakodowany tekst:", encodedText, "\n")
print("Oryginalny tekst:", text, "\n")
print("Odkodowany tekst:", decodedText, "\n")