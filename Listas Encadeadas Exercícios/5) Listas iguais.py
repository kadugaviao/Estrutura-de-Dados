class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def lista_insere(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento

def igual(l1, l2):
    while l1 is not None and l2 is not None:
        if l1.info != l2.info:
            return False
        l1 = l1.prox
        l2 = l2.prox

    return l1 is None and l2 is None


def imprime_lista(lst):
    while lst is not None:
        print(lst.info, end=" -> ")
        lst = lst.prox
    print("None")

lista_encadeada_1 = None
lista_encadeada_2 = None

lista_encadeada_1 = lista_insere(lista_encadeada_1, 1)
lista_encadeada_1 = lista_insere(lista_encadeada_1, 2)
lista_encadeada_1 = lista_insere(lista_encadeada_1, 3)

lista_encadeada_2 = lista_insere(lista_encadeada_2, 1)
lista_encadeada_2 = lista_insere(lista_encadeada_2, 2)
lista_encadeada_2 = lista_insere(lista_encadeada_2, 3)

print("Lista 1:")
imprime_lista(lista_encadeada_1)

print("Lista 2:")
imprime_lista(lista_encadeada_2)

if igual(lista_encadeada_1, lista_encadeada_2):
    print("As listas são iguais!")
else:
    print("As listas são diferentes!")
