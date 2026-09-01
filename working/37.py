# 1. Criamos a lista com os 10 números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Olhamos cada número da lista
for numero in numeros:
    # 3. Se o resto da divisão por 2 for zero, ele é par
    if numero % 2 == 0:
        print(numero)
