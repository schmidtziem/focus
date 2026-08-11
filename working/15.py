numero1 = int(input('Me fale um numero: '))
numero2 = int(input('Me fale outro numero: '))
numero3 = int(input('Me fale mais um numero: '))

maior = numero1

if numero1 > maior:
    numero2 = maior

elif numero3 > maior:
    numero3 = maior


print(f'O numero maior é: {maior}')
