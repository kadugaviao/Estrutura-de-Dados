class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def lista_inserir(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento


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

    if l1 is not None:
        atual.prox = l1

    if l2 is not None:
        atual.prox = l2
    
    return aux.prox
    
def imprime_lista(lst):
    while lst is not None:
        print(lst.info)
        lst = lst.prox
    print("None")


l1 = None
l2 = None

l1 = lista_inserir(l1, 5)
l1 = lista_inserir(l1, 3)
l1 = lista_inserir(l1, 1)

l2 = lista_inserir(l2, 6)
l2 = lista_inserir(l2, 4)
l2 = lista_inserir(l2, 2)

print("Lista 1:")
imprime_lista(l1)

print("Lista 2:")
imprime_lista(l2)

l3 = merge(l1, l2)
print("Lista Mesclada:")
imprime_lista(l3)

