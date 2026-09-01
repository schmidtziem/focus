preço = float(input('Me fale o preço do produto: '))
desconto = preço * 5 / 100
valor = preço - desconto

if preço > 100:
    print(f'O preço final com 5% de desconto é : {valor }')