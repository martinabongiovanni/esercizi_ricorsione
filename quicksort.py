# si vuole ordinare una lista di numeri

def quicksort(sequenza):
    if len(sequenza) <= 1: # quando la sequenza ha lunghezza 1 o 0, ho raggiunto il caso terminale
        return sequenza
    else: # ho una sequenza di n elementi, devo:
        # 1) scegliere run pivot random
        pivot = sequenza[0]
        # 2) dividere la sequenza in sotto sequenze
        sequenza_smaller = [] # qui inserirò i numeri minori del pivot
        sequenza_larger = [] # qui inserirò i numeri maggiori del pivot
        sequenza_pivot = [] # perché potrebbero esserci più elementi pari al valore scelto come pivot
        for i in sequenza:
            if i<pivot:
                sequenza_smaller.append(i)
            elif i>pivot:
                sequenza_larger.append(i)
            else:
                sequenza_pivot.append(i)

        # un modo più semplice per risolverlo è:
        # sequenza_smaller = [n for n in sequenza if n < pivot]
        # sequenza_larger = [n for n in sequenza if n > pivot]
        # sequenza_pivot = [n for n in sequenza if n == pivot]

        return (quicksort(sequenza_smaller) +
                sequenza_pivot +
                quicksort(sequenza_larger))




if __name__ == "__main__":
    sequenza = [3, 5, 2, 9, 11, 4, 7]
    print(quicksort(sequenza))