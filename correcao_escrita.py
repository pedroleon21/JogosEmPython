from unicodedata import normalize
def string_normalizada(palavra):
    return normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')

if(__name__ == '__main__'):
    print(string_normalizada(input("digite uma palavra para vela normalizada")))