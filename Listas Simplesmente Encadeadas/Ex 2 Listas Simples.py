"""
2. Considere listas de valores inteiros e implemente uma função que receba
como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
duas, de forma a segunda lista começar no primeiro nó logo após a
ocorrência de n na lista original. A figura a seguir ilustra esta separação:
"""

class Lista:
    def __init__(self, info=None):
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

def retira_v(lst, value):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    if lst is not None and lst.info == value:
        lst = lst.prox
    
    atual = lst
    while atual is not None and atual.prox is not None:
        if atual.prox.info == value:
            atual.prox = atual.prox.prox
        else:
            atual = atual.prox

    return lst

def divide_lista(lst, value):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual is not None:
        if atual.info == value:
            l2 = atual.prox 
            atual.prox = None
            return l2
        atual = atual.prox

    return None

lista = Lista(9)
lista = insert_start(lista, 8)
lista = insert_start(lista, 7)
lista = insert_start(lista, 6)
lista = insert_start(lista, 5)
lista = insert_start(lista, 4)
lista = insert_start(lista, 3)
lista = insert_start(lista, 2)
lista = insert_start(lista, 1)
lista = insert_end(lista, 10)

print("\nLista:")
imprime_lista(lista)

l2 = divide_lista(lista, 5)
print("\nDividir lista em duas:")

imprime_lista(lista)
imprime_lista(l2)