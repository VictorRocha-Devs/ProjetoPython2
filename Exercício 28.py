# Declarar as variáveis
preco = 0.0
venda = 0.0
novo_preco = 0.0

# Inicio 
preco = float(input("Digite o preço atual: "))
venda = float(input("Digite a média de venda mensal: "))

if venda < 500 and preco < 30:
    novo_preco = preco * 1.10
elif (venda >= 500 and venda < 1000) and (30 <= preco < 80):
    novo_preco = preco * 1.15
elif venda >= 1000 and preco >= 80:
    novo_preco = preco * 0.95
else:
    novo_preco = preco

print(f"O novo preço é: R$ {novo_preco:.2f}")
# Fim