# Declarar as variáveis
n = -1
fatorial = 1
i = 0

# Inicio 
# Loop de verificação: não aceita números negativos
while n < 0:
    n = int(input("Digite um número inteiro positivo para o fatorial: "))
    if n < 0:
        print("Erro! O número deve ser maior ou igual a zero.")

if n == 0:
    fatorial = 1
else:
    for i in range(1, n + 1):
        fatorial = fatorial * i

print(f"O fatorial de {n} é: {fatorial}")
# Fim