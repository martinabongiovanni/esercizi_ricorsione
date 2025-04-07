from time import sleep

# si vuole realizzare un countdown da 10 a 0

# soluzione iterativa
def countdown(n):
    while n>=0:
        print(n)
        sleep(0.5)
        n-=1

# soluzione ricorsiva
def countdown_recursive(n):
    if n<=0: # contiene la condizione terminale
        print ("Stop")
    else: # contiene la procedura per scomporre ulteriormente il problema
        print(n)
        sleep(0.5)
        counter = n-1
        countdown_recursive(counter)


if __name__ == '__main__':
    countdown(10)
    # in questo modo chiamo sempre la stessa funzione countdown
    countdown_recursive(10)
    # in questo modo faccio n chiamate diverse del metodo perché ogni volta passo un parametro diverso
    # il risultato viene della prima istanza del metodo viene propagato alla seconda e così via
    # solo quando termino la ricorsione, quindi solo quando eseguo l'operazione definita nell' if
    # "chiudo" tutte le istanze del metodo che ho eseguito.