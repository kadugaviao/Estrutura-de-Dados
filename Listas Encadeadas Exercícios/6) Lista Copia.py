class Lista:
    def __init__(self, info):
        self.info = info 
        self.prox = None

def copia(lst):
    if lst is None:
        return None
    
    nova_lista = Lista(lst.info)
    atual_nova = nova_lista
    atual_original = lst.prox

    while atual_original is not None:
        novo_elemento = Lista(atual_original.info)
        atual_nova.prox = novo_elemento
        atual_nova = novo_elemento
        atual_original = atual_original.prox

    return nova_lista

def lista_insere(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento

def imprime_lista(lst):
    atual = lst
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

lista_encadeada_original = None
lista_encadeada_original = lista_insere(lista_encadeada_original, 1)
lista_encadeada_original = lista_insere(lista_encadeada_original, 2)
lista_encadeada_original = lista_insere(lista_encadeada_original, 3)

print("Lista Original:")
imprime_lista(lista_encadeada_original)

print("\nLista Copiada:")
lista_encadeada_copiada = copia(lista_encadeada_original)
imprime_lista(lista_encadeada_copiada)

