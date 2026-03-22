# Declarar as variáveis
casa = 1
graos_na_casa = 1
total_graos = 0

# Inicio 
# O tabuleiro de xadrez tem exatamente 64 casas
for casa in range(1, 65):
    # Acumula o valor atual da casa no total
    total_graos = total_graos + graos_na_casa
    
    # Opcional: print para ver a evolução (cuidado, são 64 linhas!)
    # print(f"Casa {casa}: {graos_na_casa} grãos")
    
    # Prepara o valor para a próxima casa (dobra o valor)
    graos_na_casa = graos_na_casa * 2

print(f"O total de grãos em um tabuleiro de 64 casas é: {total_graos}")
# Fim