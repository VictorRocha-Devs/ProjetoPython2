# Declarar as variáveis
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0

# Inicio 
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = (b ** 2) - (4 * a * c)

if delta >= 0:
    # Usamos ** 0.5 para calcular a raiz quadrada
    raiz_delta = delta ** 0.5
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    print(f"As raízes são: {x1} e {x2}")
else:
    print("Não existem raízes reais.")
# Fim