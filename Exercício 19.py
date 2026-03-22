# Declarar as variáveis
r1 = 0.0
r2 = 0.0
maior = 0.0

# Inicio 
r1 = float(input("Digite o primeiro número real: "))
r2 = float(input("Digite o segundo número real: "))

if r1 > r2:
    maior = r1
else:
    maior = r2

print(f"O maior valor é: {maior}")
# Fim