# Declarar as variáveis
n1 = 0.0
n2 = 0.0
n3 = 0.0
n4 = 0.0
media = 0.0

# Inicio 
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"Média: {media}")

if media >= 6.0:
    print("APROVADO")
elif media >= 3.0:
    print("EXAME")
else:
    print("RETIDO")
# Fim