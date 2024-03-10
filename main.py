def verifica_sequencia(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

n = int(input("Digite um número: "))
if verifica_sequencia(n):
    print(f'O número {n} pertence à sequência de Fibonacci.')
else:
    print(f'O número {n} não pertence à sequência de Fibonacci.')