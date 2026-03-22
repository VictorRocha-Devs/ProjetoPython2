# Declarar as variáveis
n1 = int = 0
n2 = int = 0

# Inicio 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    resultado = n1 - n2
else:
    resultado = n2 - n1

print(f"A diferença é: {resultado}")
# Fim