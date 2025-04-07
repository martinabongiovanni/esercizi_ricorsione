# si vuole effettuare una ricerca dicotomica di un certo valore all'interno di una lista

def dichotomic(input_list, val):
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        # 1) divido la lista a metà
        index = len(input_list) // 2
        # 2) effettuo la ricerca nella prima o nella seconda metà della lista,
        # mi basta che uno dei due casi sia True per andar bene: ho trovato il val che cerco nella lista
        # se entrambe restituiscono False: il val che cerco non è presente nella lista
        return dichotomic(input_list[:index], val) or dichotomic(input_list[index:], val)
        # questo return può essere reso più efficiente

if __name__ == "__main__":
    sequenza = [1, 2,3, 4, 5,6, 7, 8, 9, 10]
    print(dichotomic(sequenza, 2))
    print(dichotomic(sequenza, 11))