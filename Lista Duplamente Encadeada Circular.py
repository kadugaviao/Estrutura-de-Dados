from random import randint

class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None

def insert_lst(lst, value):
    novo_elemento = Lista(value)
    
    if lst is None:
        novo_elemento.prox = novo_elemento
        novo_elemento.ant = novo_elemento
        return novo_elemento
    
    atual = lst
    ultimo = atual.ant
    ultimo.prox = novo_elemento
    novo_elemento.ant = ultimo
    novo_elemento.prox = atual
    atual.ant = novo_elemento

    return lst

def remove_node(lst, value):
    if lst is None:
        return None
    
    atual = lst
    while True:
        if atual.info == value:
            if atual.prox == atual:
                return None
            else:
                anterior = atual.ant
                proximo = atual.prox
                anterior.prox = proximo
                proximo.ant = anterior
                if atual == lst:
                    lst = proximo
            return lst
        atual = atual.prox
        if atual == lst:
            return lst
        
def count_list(lst):
    if lst is None:
        return 0
    
    i = 1
    atual = lst.prox
    while atual != lst:
        i += 1
        atual = atual.prox
    return i

def knight_battle(nomes):
    lst_cavaleiros = None
    vida_cavaleiros = {}

    for nome in nomes:
        vida_cavaleiros[nome] = randint(50, 100)
        lst_cavaleiros = insert_lst(lst_cavaleiros, nome)

    cavaleiro_atual = lst_cavaleiros

    while count_list(lst_cavaleiros) > 1:
        atacante = cavaleiro_atual.info
        prox_cavaleiro = cavaleiro_atual.prox
        defensor = prox_cavaleiro.info

        dano = randint(5, 10)
        vida_cavaleiros[defensor] -= dano

        print(f"{atacante} atacou {defensor} causando {dano} de dano! {defensor} tem {vida_cavaleiros[defensor]} de vida restante.")

        if vida_cavaleiros[defensor] <= 0:
            print(f"{defensor} foi eliminado!")
            lst_cavaleiros = remove_node(lst_cavaleiros, defensor)
            
            if defensor in vida_cavaleiros:
                del vida_cavaleiros[defensor]

        cavaleiro_atual = cavaleiro_atual.prox

    vencedor = cavaleiro_atual.info
    print(f"O campeão é {vencedor} com {vida_cavaleiros[vencedor]} de vida restante!")

nomes = ["Rei Arthur", "Gawain", "Percival", "Lancelot", "Galahad"]
knight_battle(nomes)
