class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.qtd = 0


def insert_cliente(fila, nome):
    if fila.qtd > fila.capacidade:
        print("\nNão tem mais ninguem a ser atendido...")
        return None
    
    indexFim = (fila.inicio + fila.qtd) % fila.capacidade

    fila.fila[indexFim] = nome
    fila.qtd += 1

def fila_retira(fila):
    if fila.qtd <= 0:
        print("\nNão tem mais ninguem a ser atendido...")
        return None
    
    print(f"\n{fila.fila[fila.inicio]} vai ser atendido agora!")
    fila.fila[fila.inicio] = None
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.qtd -= 1

def atender_proximo(fila):
    if fila.qtd <= 0:
        print("\nNão tem mais ninguem a ser atendido...")
        return None
    
    print(f"\n{fila.qtd} ainda precisam ser atendidos...")
    print(f"\n{fila.fila[fila.inicio]} será o proximo a ser atendido!")

fila = Fila(10)
insert_cliente(fila, "Gerson")
insert_cliente(fila, "José")
insert_cliente(fila, "Pedro")
insert_cliente(fila, "Mario")
print(fila.fila)

atender_proximo(fila)
fila_retira(fila)
print(fila.fila)

atender_proximo(fila)
fila_retira(fila)
print(fila.fila)

atender_proximo(fila)
fila_retira(fila)
print(fila.fila)

atender_proximo(fila)
fila_retira(fila)
print(fila.fila)

fila_retira(fila)