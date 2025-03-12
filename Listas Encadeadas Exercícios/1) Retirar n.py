class Lista:

    def __init__(self, info):
        self.info = info
        self.prox = None

def retira_n(lst, n):
    while lst is not None and lst.info == n:
        lst = lst.prox

    atual = lst 
    while atual is not None and atual.prox is not None:
        if atual.prox.info == n:
            atual.prox = atual.prox.prox
        else:
            atual = atual.prox
    
    return lst

head = Lista(1)
head.prox = Lista(2)
head.prox.prox = Lista(3)
head.prox.prox.prox = Lista(2)
head.prox.prox.prox.prox = Lista(4)
head.prox.prox.prox.prox.prox = Lista(2)

def print_list(lst):
    while lst:
        print(lst.info, end=" -> ")
        lst = lst.prox
    print("None")

print("Lista Original: ")
print_list(head)

head = retira_n(head, 2)

print("Lista após remover:")
print_list(head)