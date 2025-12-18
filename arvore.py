andares = input("Digite o número de andares da árvore de Natal: ")
while not andares.isdigit() or int(andares) <= 0:
    andares = input("Por favor, digite um número inteiro positivo para os andares: ")

andares = int(andares)

def desenha_arvore(andares):
    for i in range(andares):
        if i == 0: # Se for o andar 1
            num_espacos = ' ' * (andares - i - 2)
            print(num_espacos + '🌟')
        num_espacos = ' ' * (andares - i - 1)
        num_asteriscos = '*' * (2 * i + 1) # Para ser sempre impar
        print(num_espacos + num_asteriscos)
    print(' ' * (i) + '|')

desenha_arvore(andares)