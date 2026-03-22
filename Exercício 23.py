# Declarar as variáveis
a = 0 
b = 0 
c = 0 
d = 0 

# Inicio 
a = int(input("Digite o 1º valor (menor): "))
b = int(input("Digite o 2º valor (meio): "))
c = int(input("Digite o 3º valor (maior): "))
d = int(input("Digite o 4º valor (qualquer): "))

if d > c:
    print(f"Ordem: {a}, {b}, {c}, {d}")
elif d > b:
    print(f"Ordem: {a}, {b}, {d}, {c}")
elif d > a:
    print(f"Ordem: {a}, {d}, {b}, {c}")
else:
    print(f"Ordem: {d}, {a}, {b}, {c}")
# Fim