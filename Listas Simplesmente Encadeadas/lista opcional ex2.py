class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def lista_vazia(lst):
    return lst is None

def imprieme(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return
    
    atual = lst
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")


def insere_ordenado(lst, value):
    novo_elemento = Lista(value)

    if lst is None or lst.info > value:
        novo_elemento.prox = lst
        return novo_elemento
    
    atual = lst
    while atual.prox is not None and atual.prox.info < value:
        atual = atual.prox 

    novo_elemento.prox = atual.prox 
    atual.prox = novo_elemento

    return lst

lista = None
lista = insere_ordenado(lista, 2)
lista = insere_ordenado(lista, 3)
lista = insere_ordenado(lista, 1)
lista = insere_ordenado(lista, 4)
    
imprieme(lista)