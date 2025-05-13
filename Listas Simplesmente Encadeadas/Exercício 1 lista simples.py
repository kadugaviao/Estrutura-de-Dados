class ListaDupla:
    def __init__(self, info=None):
        self.info = info 
        self.ant = None
        self.prox = None

def lista_vazia(lst):
    return lst is None

def imprime_lista(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual is not None:
        print(atual.info, end=" <-> ")
        atual = atual.prox
    print("None")

def imprime_inverso(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    while atual is not None:
        print(atual.info, end=" <-> ")
        atual = atual.ant
    print("None")

def insert_start(lst, value):
    novo_elemento = ListaDupla(value)
    novo_elemento.prox = lst

    if lst is not None:
        lst.ant = novo_elemento

    return novo_elemento

def insert_end(lst, value):
    novo_elemento = ListaDupla(value)

    if lst is None:
        return novo_elemento
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo_elemento
    novo_elemento.ant = atual

    return lst
    
def busca(lst, value):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return None
    
    atual = lst
    while atual is not None:
        if atual.info == value:
            valor = atual.info
            print(f"Valor {valor} está na lista.")
            return valor
        else:
            atual = atual.prox

    print(f"Valor: {value} não está na lista...")
    return None

def inserção_ordenada(lst, value):
    novo_elemento = ListaDupla(value)

    if lista_vazia(lst) or lst.info >= value:
        novo_elemento.prox = lst

        if lst is not None:
            lst.ant = novo_elemento
    
    atual = lst
    anterior = None

    while atual is not None and atual.info < value:
        atual = atual.prox
    proximo = atual.prox

    atual.prox = novo_elemento
    novo_elemento.ant = atual
    novo_elemento.prox = proximo
    if proximo:
        proximo.ant = novo_elemento
    return lst

def remover_valor(lst, value):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return None
    
    atual = lst

    while atual is not None:
        if atual.info == value:
            if atual.ant:
                atual.ant.prox = atual.prox
            else:
                lst = atual.prox

            if atual.prox is not None:
                atual.prox.ant = atual.ant

            print(f"Valor {value} foi removido da lista!")
            return lst
        atual = atual.prox

    print(f"Valor {value} não está na lista...")
    return lst
