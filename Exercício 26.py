# Declarar as variáveis
n1 = 0
n2 = 0
maior = 0
menor = 0

# Inicio 
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Primeiro descobrimos quem é o maior
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

# Verificamos se o resto da divisão do maior pelo menor é zero
if maior % menor == 0:
    print(f"O número {maior} é múltiplo de {menor}.")
else:
    print(f"O número {maior} NÃO é múltiplo de {menor}.")
# Fim