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

    return lst

def insert_end(lst, value):
    novo_elemento = Lista(value)
    
    if lst is None:
        return novo_elemento
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo_elemento

    return lst

def retirar_value(lst, value):
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

def separa(lst, value):
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

def merge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    atual = l1
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = l2
    return l1

l1 = Lista(1)
l1 = insert_end(l1, 2)
l1 = insert_end(l1, 3)
l1 = insert_end(l1, 4)
l1 = insert_end(l1, 5)

l2 = Lista(6)
l2 = insert_end(l2, 7)
l2 = insert_end(l2, 8)
l2 = insert_end(l2, 9)
l2 = insert_end(l2, 10)

print("\nLista 1:")
imprime_lista(l1)

print("\nLista 2:")
imprime_lista(l2)

novaLista = merge(l1, l2)
print("Lista Mesclada:")

imprime_lista(novaLista)
