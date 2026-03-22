# Declarar as variáveis
base = 0
expoente = -1
resultado = 1
i = 0

# Inicio 
base = int(input("Digite a base: "))

# Verificação: expoente não pode ser negativo neste exercício simples
while expoente < 0:
    expoente = int(input("Digite o expoente (positivo): "))
    if expoente < 0:
        print("Por favor, digite um expoente maior ou igual a zero.")

for i in range(expoente):
    resultado = resultado * base

print(f"O resultado de {base} elevado a {expoente} é: {resultado}")
# Fim