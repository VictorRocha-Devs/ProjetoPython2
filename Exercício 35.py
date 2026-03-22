# Declarar as variáveis
n1 = 0
n2 = 0
maior = 0
menor = 0
soma = 0
i = 0

# Inicio 
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma = soma + i

print(f"A soma dos ímpares entre {menor} e {maior} é: {soma}")
# Fim