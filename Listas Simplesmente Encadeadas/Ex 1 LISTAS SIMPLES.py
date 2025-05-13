class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def lista_vazia(lst):
    return lst is None

def imprime_lista(lst):
    if lista_vazia(lst):
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

    if lista_vazia(lst):
        return novo_elemento
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo_elemento
    
    return lst

def insert_order(lst, value):
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

def lista_comprimento(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    i = 0
    atual = lst
    while atual is not None:
        i += 1
        atual = atual.prox
    
    return i 

def maiores(lst, value):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    atual = lst
    n_maiores = 0
    while atual is not None:
        if atual.info > value:
            n_maiores += 1
        atual = atual.prox
    
    print(f"A lista possui {n_maiores} valores maiores que {value}!")

def ultimo(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    print(f"Último nó: {atual.info}")
            
def media(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    atual = lst
    valores_soma = 0
    while atual is not None:
        valores_soma += atual.info
        atual = atual.prox

    valores_qtd = lista_comprimento(lst)
    media_final = valores_soma / valores_qtd
    print(f"Média Aritmetica: {media_final}")
    return media_final
    
def lista_retira_v(lst, value):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    if lst.info == value:
        print("Não há elemento anterior ao primeiro...")
        return lst
    
    pre_anterior = None
    anterior = lst
    atual = lst.prox

    while atual is not None and atual.info != value:
        pre_anterior = anterior
        anterior = atual
        atual = atual.prox
    
    if lista_vazia(atual):
        print(f"Valor {value} não encontrado...")
        return lst
    
    if lista_vazia(pre_anterior):
        lst = atual
    else:
        pre_anterior.prox = atual

    return lst


lista = Lista(2)
lista = insert_start(lista, 0)
lista = insert_order(lista, 1)
lista = insert_order(lista, 3)
lista = insert_order(lista, 4)
lista = insert_order(lista, 5)
lista = insert_order(lista, 6)
lista = insert_end(lista, 7)

imprime_lista(lista)

lista_comprimento(lista)
maiores(lista, 0)
ultimo(lista)
media(lista)

lista_retira_v(lista, 7)
imprime_lista(lista)