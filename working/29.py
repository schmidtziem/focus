def calcula_fatorial(n):
  fat = 1
  for i in range(1, n + 1):
    fat *= i
  return fat


print(calcula_fatorial(5))  # Saída: 120
