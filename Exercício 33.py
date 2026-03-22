# Declarar as variáveis
n = 0
i = 1
soma_serie = 0.0

# Inicio 
# Loop de verificação: N deve ser pelo menos 1
while n <= 0:
    n = int(input("Digite um número inteiro positivo para N: "))
    if n <= 0:
        print("Erro! O valor de N deve ser maior que zero para compor a série.")

# O loop vai de 1 até N (inclusive)
for i in range(1, n + 1):
    soma_serie = soma_serie + (1 / i)
    # Opcional: print para acompanhar a soma parcial
    # print(f"Termo 1/{i} adicionado. Soma atual: {soma_serie:.4f}")

print(f"O resultado final da série para N={n} é: {soma_serie:.4f}")
# Fim