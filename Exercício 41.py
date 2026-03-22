# Declarar as variáveis
dado1 = 0
dado2 = 0
soma = 0

# Inicio 
print("Possibilidades para a soma ser 7:")

# O primeiro dado vai de 1 a 6
for dado1 in range(1, 7):
    # O segundo dado também vai de 1 a 6
    for dado2 in range(1, 7):
        soma = dado1 + dado2
        if soma == 7:
            print(f"Dado 1: {dado1} | Dado 2: {dado2} -> Soma: {soma}")
# Fim