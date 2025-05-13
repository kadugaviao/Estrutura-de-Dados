class Alunos:
    def __init__(self, matricula, p1, p2, p3):
        self.matricula = matricula
        self.notas = [p1, p2, p3]
        self.prox = None

def lista_vazia(lst):
    return lst is None

def media_notas(notas):
    total = 0

    for i in notas:
        total += i
    return total / len(notas)

def insere_ordenado(lst, matricula, p1, p2, p3):
    novo_elemento = Alunos(matricula, p1, p2, p3)
    media_novo = media_notas(novo_elemento.notas)

    if lista_vazia(lst) or media_novo > media_notas(lst.notas):
        novo_elemento.prox = lst
        return novo_elemento
    
    atual = lst
    while atual.prox is not None and media_notas(atual.prox.notas) >= media_novo:
        atual = atual.prox
    
    novo_elemento.prox = atual.prox
    atual.prox = novo_elemento
    return lst

def imprime_alunos(lst):
    if lista_vazia(lst):
        print("Lista Vazia...")
        return 
    
    atual = lst
    while not lista_vazia(atual):
        m = media_notas(atual.notas)
        print(f"Matricula: {atual.matricula}; Média: {m:.2f}")
        atual = atual.prox

lista = None
lista = insere_ordenado(lista, 201, 8.75, 9.0, 10)
lista = insere_ordenado(lista, 202, 6.2, 4.3, 8.1)
lista = insere_ordenado(lista, 203, 4.1, 0.0, 2.0)
lista = insere_ordenado(lista, 204, 7.0, 7.0, 7.0)

imprime_alunos(lista)

    

