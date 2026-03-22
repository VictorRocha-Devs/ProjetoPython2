# Declarar as variáveis
n1 = 0
n2 = 0
maior = 0
menor = 0
i = 0
j = 0
cont_divisores = 0

# Inicio 
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Descobrir o intervalo (quem é o menor e o maior)
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print(f"Números primos entre {menor} e {maior}:")

# Loop para percorrer cada número do intervalo
for i in range(menor, maior + 1):
    # Números menores que 2 não são primos
    if i >= 2:
        cont_divisores = 0
        
        # Segundo loop: testa divisores de 1 até o próprio número i
        for j in range(1, i + 1):
            if i % j == 0:
                cont_divisores = cont_divisores + 1
        
        # Se encontrou exatamente 2 divisores (1 e ele mesmo), é primo
        if cont_divisores == 2:
            print(i)
# Fim