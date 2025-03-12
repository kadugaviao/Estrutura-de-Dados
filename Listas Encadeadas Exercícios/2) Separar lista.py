class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def separa(lst, n):
    if lst is None:
        return None

    atual = lst
    anterior = None

    while atual is not None and atual.info != n:
        anterior = atual
        atual = atual.prox

    if atual is None:
        return None
    
    segunda_lista = atual.prox
    atual.prox = None

    return segunda_lista

lista_encadeada = Lista(1)
lista_encadeada.prox = Lista(3)
lista_encadeada.prox.prox = Lista(5)
lista_encadeada.prox.prox.prox = Lista(7)
lista_encadeada.prox.prox.prox.prox = Lista(9)

def lista_imprime(lst):
    atual = lst

    while atual is not None:
        print(atual.info)
        atual = atual.prox
    print("None")

print("Lista Original: ")
lista_imprime(lista_encadeada)

nova_lista = separa(lista_encadeada, 5)

print("Primeira parte da lista: ")
lista_imprime(lista_encadeada)

print("Segunda parte da lista: ")
lista_imprime(nova_lista)