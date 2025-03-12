class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def lista_insere(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento
    return novo_elemento

def inverte(lst):
    anterior = None
    atual = lst

    while atual is not None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo

    return anterior

def lista_imprime(lst):
    atual = lst

    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox 
    print("None")
        
lista_encadeada = None
lista_encadeada = lista_insere(lista_encadeada, 5)
lista_encadeada = lista_insere(lista_encadeada, 3)
lista_encadeada = lista_insere(lista_encadeada, 1)

print("Lista Original:")
lista_imprime(lista_encadeada)

lista_encadeada = inverte(lista_encadeada)

print("Lista Invertida:")
lista_imprime(lista_encadeada)
