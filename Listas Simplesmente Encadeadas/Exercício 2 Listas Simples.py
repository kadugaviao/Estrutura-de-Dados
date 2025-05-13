class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def imprime_lista(lst):
    if lst is None:
        print("Lista Vazia...")
        return None
    
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

def retira_n(lst, n):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual is not None and atual.prox is not None:
        if atual.prox.info == n:
            atual.prox = atual.prox.prox
        else:
            atual = atual.prox 


def separa(lst, n):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual is not None:
        if atual.info == n:
            l2 = atual.prox
            atual.prox = None
            return l2
        atual = atual.prox

    return None

def merge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    aux = Lista(0)
    atual = aux

    while l1 is not None and l2 is not None:
        atual.prox = l1
        l1 = l1.prox
        atual = atual.prox

        atual.prox = l2
        l2 = atual.prox
        atual = atual.prox

    if l1 is not None:
        atual.prox = l1
    elif l2 is not None:
        atual.prox = l2

    return aux.prox

lista = None
lista = insert_end(lista, 4)
lista = insert_start(lista, 3)
lista = insert_start(lista, 2)
lista = insert_start(lista, 1)
lista = insert_end(lista, 5)
lista = insert_end(lista, 6)

print("Lista:")
imprime_lista(lista)

lista2 = separa(lista, 3)

print("Primeira parte após separação:")
imprime_lista(lista)

print("Segunda parte após separação:")
imprime_lista(lista2)