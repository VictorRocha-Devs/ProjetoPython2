# Declarar as variáveis
n = -1
soma_serie = 1.0
fatorial = 1
i = 0
j = 0

# Inicio 
# Loop de verificação: N deve ser pelo menos 1
while n < 1:
    n = int(input("Digite um valor inteiro positivo para N (termo da série): "))
    if n < 1:
        print("Erro! O valor de N deve ser 1 ou maior.")

# Loop principal para percorrer os termos de 1 até N
for i in range(1, n + 1):
    fatorial = 1
    # Loop interno para calcular o fatorial do número i atual
    for j in range(1, i + 1):
        fatorial = fatorial * j
    
    # Adiciona o termo 1/i! à soma
    soma_serie = soma_serie + (1 / fatorial)

print(f"O resultado da série para N={n} é: {soma_serie:.6f}")
# Fim