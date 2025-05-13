class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def imprime_lista(lst):
    if lst is None:
        print("Lista Vazia...")
        return 
    
    atual = lst
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

def insert_start(lst, value):
    novo_elemento = Lista(value)
    novo_elemento.prox = lst

    return novo_elemento

def insert_end(lst, value):
    novo_elemento = Lista(value)

    if lst is None:
        return novo_elemento
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo_elemento

    return lst

lista = Lista(4)
lista = insert_start(lista, 3)
lista = insert_start(lista, 2)
lista = insert_start(lista, 1)
lista = insert_end(lista, 5)
lista = insert_end(lista, 6)

imprime_lista(lista)