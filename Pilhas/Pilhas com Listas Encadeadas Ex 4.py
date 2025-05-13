class Lista:
    def __init__(self, info):
        self.info = info 
        self.prox = None

class Pilha:
    def __init__(self, topo = None):
        self.topo = topo

def pilha_push(pilha, value):
    novo_elemento = Lista(value)
    novo_elemento.prox = pilha.topo
    pilha.topo = novo_elemento
    
def pilha_pop(pilha):
    if pilha.topo is not None:
        pilha.topo = pilha.topo.prox
    else:
        print("Não há nada para esvaziar na pilha...")

def imprimir_recursivo(elemento_pilha):
    if elemento_pilha is not None:
        imprimir_recursivo(elemento_pilha.prox)
        print(elemento_pilha.info, end="")

def pilha_add_text(pilha):
    print("Digite os caracteres. Use '#' para desfazer. Pressione ENTER para terminar.")
    while True:
        caractere = input("Digite um caractere: ")

        if caractere == "":
            break
        elif caractere == "#":
            pilha_pop(pilha)
        else:
            pilha_push(pilha, caractere)

    print("Texto Final: ", end="")
    imprimir_recursivo(pilha.topo)
    print()

pilha = Pilha()
pilha_add_text(pilha)
