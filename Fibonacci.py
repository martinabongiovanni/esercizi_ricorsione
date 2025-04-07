# si vuole risolvere la sequenza di Fibonacci
from time import time
from functools import lru_cache

class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1} # tecnica di MEMORIZATION

    def calcola_elemento (self, n):
        # skip del check che n non sia negativo
        if n == 0 or n == 1: # caso terminale
            return n
        else: # definisco la ricorsione, qui applico Fibonacci
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

    def calcola_elemento_cache(self, n):
        # se n è già presente nel mio dict, restituisco il valore che ho memorizzato
        if self.cache.get(n) is not None:
            return self.cache[n]
        else: # non ho n nel mio dict, quindi ne calcolo il valore e lo memorizzo nel dict
            self.cache[n] = self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2)
            return self.cache[n]

    @lru_cache(maxsize=None)
    # questa funzione, a livello di codice, è uguale a calcola_elemento, ma ha il decoratore lru_cache
    # che creerà da sè un dict e prima di richiamare il metodo, verifica se ha l'elemento salvato nel dict
    def calcola_elemento_lru(self, n):
        if n == 0 or n == 1: # caso terminale
            return n
        else: # definisco la ricorsione, qui applico Fibonacci
            return self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2)

if __name__ == '__main__':
    # chiamo il metodo definito nella classe Fibonacci e osservo quanto tempo impiega nel calcolo
    start_time = time()
    print(Fibonacci().calcola_elemento(40))
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")

    start_time_cache = time()
    print(Fibonacci().calcola_elemento_cache(40))
    end_time_cache = time()
    print(f"Elapsed time: {end_time_cache - start_time_cache}")

    start_time_lru = time()
    print(Fibonacci().calcola_elemento_lru(40))
    end_time_lru = time()
    print(f"Elapsed time: {end_time_lru - start_time_lru}")