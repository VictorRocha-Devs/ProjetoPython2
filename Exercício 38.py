# Declarar as variáveis
num = 0.0
maior = 0.0
menor = 0.0
i = 1

# Inicio 
while i <= 100:
    num = -1.0
    # Verificação: somente positivos
    while num < 0:
        num = float(input(f"Digite o {i}º número (positivo): "))
        if num < 0:
            print("Valor inválido! Digite apenas números positivos.")
    
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    i = i + 1

print(f"Maior valor: {maior} | Menor valor: {menor}")
# Fim