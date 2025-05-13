class ListaNode:
    def __init__(self, info):
        self.info = info 
        self.prox = None

class Pilha:
    def __init__(self, topo = None):
        self.topo = topo

def pilha_show(pilha): 
    if pilha.topo is None:
        print("Pilha Vazia...")
        return None
    
    atual = pilha.topo
    while atual is not None:
        print(atual.info)
        atual = atual.prox
    print("None")

def pilha_inserir(pilha, value):
    if pilha.topo is None:
        novo_elemento = ListaNode(value)
        pilha.topo = novo_elemento

        return pilha
    
    novo_elemento = ListaNode(value)
    novo_elemento.prox = pilha.topo
    pilha.topo = novo_elemento

def pilha_inserir_num(pilha):
    for i in range(5):
        num = int(input("Digite um número: "))
        pilha_inserir(pilha, num)

def pilha_pop_all(pilha):
    if pilha.topo is None:
        print("Pilha Vazia...")
        return None
    else:
        while pilha.topo is not None:
            print(pilha.topo.info)
            pilha.topo = pilha.topo.prox
        print("Pilha Desempilhada...")

pilha = Pilha()
pilha_inserir_num(pilha)

print("\nPilha:")
pilha_show(pilha)

print("\nDesempilhando...")
pilha_pop_all(pilha)