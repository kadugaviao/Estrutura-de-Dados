class Pilha:
    def __init__(self):
        self.vet = []

def pilha_vazia(pilha):
    return len(pilha.vet) == 0

def pilha_push(pilha, valor):
    pilha.vet.append(valor)

def pilha_pop(pilha):
    if pilha_vazia(pilha):
        print("A pilha já está vazia!")
        return None
    return pilha.vet.pop()

def pilha_top(pilha):
    if pilha_vazia(pilha):
        print("A pilha está vazia!")
        return None
    return pilha.vet[-1]

def aplicar_operador(operador, op2, op1=None):
    if operador == 'not':
        return not op2
    elif operador == 'and':
        return op1 and op2
    elif operador == 'or':
        return op1 or op2
    elif operador == 'xor':
        return op1 != op2

def precedence(operador):
    if operador == 'not':
        return 3
    elif operador == 'and':
        return 2
    elif operador == 'or' or operador == 'xor':
        return 1
    return 0

def avaliar_expressao(expressao):
    operandos = Pilha()
    operadores = Pilha()
    i = 0

    while i < len(expressao):
        if expressao[i] == ' ':
            i += 1
            continue

        if expressao[i:i+4] == "True":
            pilha_push(operandos, True)
            i += 4
        elif expressao[i:i+5] == "False":
            pilha_push(operandos, False)
            i += 5
        elif expressao[i] == '(':
            pilha_push(operadores, '(')
            i += 1
        elif expressao[i] == ')':
            while not pilha_vazia(operadores) and pilha_top(operadores) != '(':
                op = pilha_pop(operadores)
                if op == 'not':
                    if pilha_vazia(operandos):
                         print(f"Erro: Falta operando para o operador '{op}'")
                         return None
                    val = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, val)) 
                else:
                    if pilha_vazia(operandos):
                         print(f"Erro: Falta segundo operando para o operador '{op}'")
                         return None
                    op2 = pilha_pop(operandos)
                    if pilha_vazia(operandos):
                         print(f"Erro: Falta primeiro operando para o operador '{op}'")
                         return None
                    op1 = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, op2, op1))

            if not pilha_vazia(operadores) and pilha_top(operadores) == '(':
                pilha_pop(operadores)
            else:
                print("Erro: Parênteses desbalanceados (falta '(' correspondente)")
                return None
            i += 1
        elif expressao[i:i+3] == "not":
            pilha_push(operadores, "not")
            i += 3
        elif expressao[i:i+3] == "and":
            while not pilha_vazia(operadores) and \
                  pilha_top(operadores) != '(' and \
                  precedence(pilha_top(operadores)) >= precedence("and"):
                op = pilha_pop(operadores)
                if op == 'not':
                    if pilha_vazia(operandos): print(f"Erro: Falta operando para '{op}'"); return None
                    val = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, val))
                else:
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 2 para '{op}'"); return None
                    op2 = pilha_pop(operandos)
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 1 para '{op}'"); return None
                    op1 = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, op2, op1))
            pilha_push(operadores, "and")
            i += 3
        elif expressao[i:i+2] == "or":
            while not pilha_vazia(operadores) and \
                  pilha_top(operadores) != '(' and \
                  precedence(pilha_top(operadores)) >= precedence("or"):
                op = pilha_pop(operadores)
                if op == 'not':
                    if pilha_vazia(operandos): print(f"Erro: Falta operando para '{op}'"); return None
                    val = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, val))
                else:
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 2 para '{op}'"); return None
                    op2 = pilha_pop(operandos)
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 1 para '{op}'"); return None
                    op1 = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, op2, op1))
            pilha_push(operadores, "or")
            i += 2
        elif expressao[i:i+3] == "xor":
            while not pilha_vazia(operadores) and \
                  pilha_top(operadores) != '(' and \
                  precedence(pilha_top(operadores)) >= precedence("xor"):
                op = pilha_pop(operadores)
                if op == 'not':
                    if pilha_vazia(operandos): print(f"Erro: Falta operando para '{op}'"); return None
                    val = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, val))
                else:
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 2 para '{op}'"); return None
                    op2 = pilha_pop(operandos)
                    if pilha_vazia(operandos): print(f"Erro: Falta operando 1 para '{op}'"); return None
                    op1 = pilha_pop(operandos)
                    pilha_push(operandos, aplicar_operador(op, op2, op1))
            pilha_push(operadores, "xor")
            i += 3
        else:
            print(f"Erro: Elemento inesperado na expressão: {expressao[i]}")
            return None

    while not pilha_vazia(operadores):
        op = pilha_pop(operadores)
        if op == '(' or op == ')':
            print("Erro: Parênteses desbalanceados (sobraram na pilha)")
            return None
        if op == 'not':
            if pilha_vazia(operandos): print(f"Erro: Falta operando final para '{op}'"); return None
            val = pilha_pop(operandos)
            pilha_push(operandos, aplicar_operador(op, val))
        else:
            if pilha_vazia(operandos): print(f"Erro: Falta operando 2 final para '{op}'"); return None
            op2 = pilha_pop(operandos)
            if pilha_vazia(operandos): print(f"Erro: Falta operando 1 final para '{op}'"); return None
            op1 = pilha_pop(operandos)
            pilha_push(operandos, aplicar_operador(op, op2, op1))

    resultado_final = pilha_pop(operandos)
    if not pilha_vazia(operandos):
        print("Erro: Operandos restantes na pilha após avaliação.")
        return None
    return resultado_final

if __name__ == "__main__":
    while True:
        try:
            expr = input("Digite a expressão booleana (ex: 'True and not False or (True xor False)') ou 'sair' para encerrar: ")
            if expr.lower() == 'sair':
                print("Encerrando o programa.")
                break

            resultado = avaliar_expressao(expr)

            if resultado is not None:
                print(f"Resultado: {resultado}")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")