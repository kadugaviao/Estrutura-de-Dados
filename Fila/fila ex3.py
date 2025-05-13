class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.qtd = 0

def inserir_fila(fila, value):
    if fila.qtd == fila.capacidade:
        print("Fila Cheia")
        return None
    
    indexFim = (fila.inicio + fila.qtd) % fila.capacidade

    fila.fila[indexFim] = value
    fila.qtd += 1

def inserir_escrito_remover():
    fila = FilaCircular(5)
    print("\nInsira 5 valores na fila:")
    for i in range(5):
        nome = input(f"{i + 1}º valor: ")
        inserir_fila(fila, nome)

    print(f"Fila Original:")
    print(f"Fila: {fila.fila}")
    print(f"Início: {fila.inicio}")
    print(f"Quantidade: {fila.qtd}")

    print("\nRemovendo 2 valores da fila:")
    fila_retira(fila)
    fila_retira(fila)

    print("\nNova Fila:")
    print(f"Fila: {fila.fila}")
    print(f"Início: {fila.inicio}")
    print(f"Quantidade: {fila.qtd}")


def fila_retira(fila):
    if fila.qtd <= 0:
        print("Fila Vazia...")
        return None
    
    fila.fila[fila.inicio] = None
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.qtd -= 1

inserir_escrito_remover()