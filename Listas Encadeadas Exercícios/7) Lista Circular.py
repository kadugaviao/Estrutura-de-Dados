class ListaCircular:
    def __init__(self, info):
        self.info = info
        self.prox = self 

def lista_insere(lista, valor):
    novo_elemento = ListaCircular(valor)

    if lista is None:
        return novo_elemento  
    
    atual = lista
    while atual.prox != lista:
        atual = atual.prox

    atual.prox = novo_elemento
    novo_elemento.prox = lista  

    return lista  

def lista_retirar(lista, valor):
    if lista is None:
        return None
    
    atual = lista
    anterior = None

    while True: 
        if atual.info == valor:
            if anterior is None:  
                if atual.prox == lista:  
                    return None  
                else:
                    novo_inicio = atual.prox
                    ultimo = lista
                    while ultimo.prox != lista:
                        ultimo = ultimo.prox
                    ultimo.prox = novo_inicio 
                    return novo_inicio
            else:
                anterior.prox = atual.prox
                return lista
            
        anterior = atual
        atual = atual.prox

        if atual == lista:  
            break
    
    return lista

def imprime_lista(lista):
    if lista is None:
        print("Lista vazia")
        return
    
    atual = lista
    while True:
        print(atual.info, end=" -> ")
        atual = atual.prox
        if atual == lista:
            break
    print("(volta ao início)")

lista_encadeada = None
lista_encadeada = lista_insere(lista_encadeada, 1)
lista_encadeada = lista_insere(lista_encadeada, 2)
lista_encadeada = lista_insere(lista_encadeada, 3)
lista_encadeada = lista_insere(lista_encadeada, 4)

print("Lista Circular após inserções:")
imprime_lista(lista_encadeada)

lista_encadeada = lista_retirar(lista_encadeada, 2)  
print("Lista Circular após remover o 2:")
imprime_lista(lista_encadeada)

lista_encadeada = lista_retirar(lista_encadeada, 1) 
print("Lista Circular após remover o 1:")
imprime_lista(lista_encadeada)
