# si vuole tenere il conto del numero di stringhe contenute in una lista

# funzione alla quale passo come parametro una lista
# la funzione scorre tutti gli elementi della lista
# se trova una stringa, aggiunge 1 al contatore
# se trova una lista => ricorsione, eseguo nuovamente il metodo

def count_leaf_nodes(input_list):
    if len(input_list) == 0: # caso terminale, più semplice, quando la lista è vuota
        return 0
    else: # divido il problema in problema più piccoli
        # inizializzo un contatore a 0
        counter = 0
        # per ogni elemento della lista
        for element in input_list:
            # se l'elemento è una lista
            if type(element) == list:
                # allora vado a fare una ricorsione
                # aggiorno counter richiamando il metodo e passando come parametro l'elemento che è una lista
                counter += count_leaf_nodes(element)
            # se l'elemento è una stringa
            else: # di fatto questo è un caso terminale, mentre l' if iniziale gestisce il caso in cui la lista sia vuota
                # aggiorno il contatore
                counter += 1
        return counter

if __name__ == '__main__':
    names =  ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))