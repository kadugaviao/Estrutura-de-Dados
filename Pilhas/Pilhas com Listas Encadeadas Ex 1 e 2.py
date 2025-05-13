class ListaNode:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self, cap = 10, topo = None):
        self.cap = cap
        self.topo = topo
        self.num_elementos = 0

def pilha_push(pilha, value):
    if pilha.num_elementos >= pilha.cap:
        print("Capacidade maxima alcançada...")
        return

    if pilha.topo is None:
        novo_elemento = ListaNode(value)
        pilha.topo = novo_elemento
        pilha.num_elementos += 1

        return pilha
    
    pilha.num_elementos += 1
    novo_elemento = ListaNode(value)
    novo_elemento.prox = pilha.topo
    pilha.topo = novo_elemento

def pilha_show(pilha):
    if pilha is None:
        print("Lista Vazia")
        return None
    
    atual = pilha.topo 
    while atual is not None:
        print(atual.info)
        atual = atual.prox
    print("None")

def pilha_pop(pilha):
    if pilha.topo is None:
        print("Pilha Vazia...")
    else:
        pilha.topo = pilha.topo.prox 
        pilha.num_elementos -= 1

def pilha_pop_all(pilha):
    if pilha.topo is None:
        print("Pilha Vazia...")
    else:
        while pilha.topo is not None:
            print(pilha.topo.info)
            pilha.num_elementos -= 1
            pilha.topo = pilha.topo.prox
        print("None")
        

pilha = Pilha(10)
pilha_push(pilha, 1)
pilha_push(pilha, 2)
pilha_push(pilha, 3)
pilha_push(pilha, 4)
pilha_push(pilha, 5)
pilha_push(pilha, 6)
pilha_push(pilha, 7)
pilha_push(pilha, 8)
pilha_push(pilha, 9)
pilha_push(pilha, 10)
pilha_push(pilha, 11)

print("\nPilha:")
pilha_show(pilha)
print(f"Quantidade de elementos: {pilha.num_elementos}")

pilha_pop(pilha)
print("\nRemoção Ultimo Elemento:")
pilha_show(pilha)
print(f"Quantidade de elementos: {pilha.num_elementos}")

print("\nRemoção Total:")
pilha_pop_all(pilha)
print(f"Quantidade de elementos: {pilha.num_elementos}")

print("\nPilha Vazia:")
pilha_show(pilha)
