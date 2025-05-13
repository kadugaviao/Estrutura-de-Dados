class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.qtd = 0


def insert_cliente(fila, nome):
    if fila.qtd >= fila.capacidade:
        print("Fila Cheia...")
        return None
    
    index_fim = (fila.inicio + fila.qtd) % fila.capacidade

    fila.fila[index_fim] = nome
    fila.qtd += 1

def remove(fila):
    if fila.qtd <= 0:
        print("Fila Vazia...")
        return None
    
    primeiro_da_fila = fila.fila[fila.inicio]

    fila.fila[fila.inicio] = None
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.qtd -= 1

    return primeiro_da_fila

fila = Fila(12)

insert_cliente(fila, "João")
insert_cliente(fila, "Ricardo")
insert_cliente(fila, "Joselito")
insert_cliente(fila, "Pedro")
insert_cliente(fila, "Balduino")
insert_cliente(fila, "Ernestina")

for i in range(5):
    print(f"-=-=-=-=-=-=-= Iniciando rodada {i} -=-=-=-=-=-=-=")
    removidos = []

    for j in range(3):
        removido = remove(fila)
        removidos.append(removido)

        print(f" > Criança {removido} foi no brinquedo!")

    for j in range(len(removidos)):
        insert_cliente(fila, removidos[j])
        print(f" > Criança {removidos[j]} foi para o final")

