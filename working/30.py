limite = int(input("Digite um número: "))

soma = 0


for numero in range(1, limite + 1):
    soma += numero

print(f"A soma de todos os números até {limite} é: {soma}")
