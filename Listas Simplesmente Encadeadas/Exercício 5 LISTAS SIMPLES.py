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

def retira_value(lst, value):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    if lst is None and lst.info is not None:
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

def iguais(l1, l2):
    while l1 is not None and l2 is not None:
        if l1.info != l2.info:
            print("As listas são diferentes...")
            return False
        
        l1 = l1.prox
        l2 = l2.prox


    if l1 is not None or l2 is not None:
        print("As listas são diferentes...")    

    print("As listas são iguais!")
    return True

def copia(lst):
    if lst is None:
        print("Lista Vazia...")
        return None
    
    nova_lista = Lista(lst.info)
    atual_original = lst.prox
    atual_copia = nova_lista

    while atual_original is not None:
        novo_elemento = Lista(atual_original.info)
        atual_copia.prox = novo_elemento
        atual_copia = novo_elemento
        atual_original = atual_original.prox

    return nova_lista