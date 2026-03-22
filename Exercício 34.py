# Declarar as variáveis
n = 0
i = 0
resultado = 0

# Inicio 
n = int(input("Digite o número para ver a tabuada: "))

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
# Fim