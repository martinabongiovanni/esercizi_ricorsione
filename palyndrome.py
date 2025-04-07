# si vuole verificare se una parola è un palindromo

def palyndrome(word):
    if len(word) <= 1:
        # se abbiamo 1 o 0 lettere allora la parola è un palindromo
        return True
    else:
        # se la parola ha una lunghezza diversa si dovrà verificare:
        # 1) che la prima e l'ultima lettera siano uguali
        # 2) che le altre lettere rimanente in mezzo siano un palindromo
        return (word[0] == word[-1]) and palyndrome(word[1:-1])

def palyndrome_banale(word):
    return word == word[::-1] # inverto la parola

if __name__ == '__main__':
    print(palyndrome("casa"))
    print(palyndrome("civic"))

    print(palyndrome_banale("casa"))