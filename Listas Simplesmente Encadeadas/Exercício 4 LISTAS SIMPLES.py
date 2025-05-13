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

def separar(lst, value):
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
        return l2
    
    atual = l1
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = l2
    return l1

def inverte(lst):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    atual = lst
    anterior = None
    while atual is not None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo
        
    return anterior

l = Lista(4)
l = insert_start(l, 3)
l = insert_start(l, 2)
l = insert_start(l, 1)
l = insert_end(l, 5)

print("\nLista:")
imprime_lista(l)

l = inverte(l)
print("Lista Inversa:")
imprime_lista(l)