import os

print(8 * "=")
operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

while True:
    os.system("clear") # Limpa a tela
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha uma operação: ")
    op = int(input())
    op_string = list(operations.keys())[op] # Lista de operações, o [op] é o índice da operação escolhida
    print("")
    print(f"{op_string} escolhida\n")
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    print("")
    
    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2
    else:
        print("Operação inválida")
        

    print("")
    print(f"O resultado da operação entre {v1} e {v2} com a operação {op_string} é {result}")
    print(8 * "=")

    comando = int(input("Deseja continuar? [Digite 1 para sair] "))
    if comando == 1:
        break
