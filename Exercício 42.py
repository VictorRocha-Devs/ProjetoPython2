# Declarar as variáveis
numerador = 0
denominador = 1
soma_serie = 0.0

# Inicio 
# O numerador vai de 1 até 50
for numerador in range(1, 51):
    soma_serie = soma_serie + (numerador / denominador)
    # O denominador aumenta de 2 em 2 (1, 3, 5, 7...)
    denominador = denominador + 2

print(f"O resultado da série é: {soma_serie:.4f}")
# Fim