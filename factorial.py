# si vuole realizzare il fattoriale di un numero

def factorial(n):
    # prende come argomento un intero positivo,
    # saltiamo per il momento la verifica della correttezza del parametro
    if n<=1:
        return 1
    else:
        counter = n-1
        return n * factorial(counter)


if __name__ == '__main__':
    print(factorial(4))