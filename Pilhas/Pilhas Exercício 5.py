class Lista: 
    def __init__(self, info=None):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self, topo=None):
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

def pilha_push(pilha, value):
    novo_elemento = Lista(value)
    novo_elemento.prox = pilha.topo
    pilha.topo = novo_elemento

def pilha_pop(pilha):
    if pilha.topo is not None:
        pilha.topo = pilha.topo.prox
    else:
        print("A pilha está vazia, não há elementos para desempilhar...")

def pilha_remover_item(pilha, value):
    auxiliar = Pilha()
    encotrar = False

    while pilha.topo is not None:
        if pilha.topo.info == value and not encotrar:
            pilha_pop(pilha)
            encotrar = True
        else:
            pilha_push(auxiliar, pilha.topo.info)
            pilha_pop(pilha)

    while auxiliar.topo is not None:
        pilha_push(pilha, auxiliar.topo.info)
        pilha_pop(auxiliar)

    if not encotrar:
        print(f"Valor '{value}' não encotrar na pilha...")

pilha = Pilha()
pilha_push(pilha, 5)
pilha_push(pilha, 4)
pilha_push(pilha, 3)
pilha_push(pilha, 2)
pilha_push(pilha, 1)

print("Pilha antes da remoção:")
pilha_show(pilha)

pilha_remover_item(pilha, 3)

print("\nPilha após remover o valor 3:")
pilha_show(pilha)