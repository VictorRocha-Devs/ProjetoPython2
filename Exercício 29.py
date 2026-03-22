# Declarar as variáveis
tipo = 0
valor = 0.0
corrigido = 0.0

# Inicio 
print("Tipos: 1-Poupança | 2-Renda Fixa")
tipo = int(input("Digite o tipo: "))
valor = float(input("Digite o valor do investimento: "))

if tipo == 1:
    corrigido = valor * 1.03
    print(f"Valor corrigido: R$ {corrigido:.2f}")
elif tipo == 2:
    corrigido = valor * 1.05
    print(f"Valor corrigido: R$ {corrigido:.2f}")
else:
    print("Tipo inválido.")
# Fim