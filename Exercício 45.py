# Declarar as variáveis
i = 1
divisor = 0
soma_serie = 0.0

# Inicio 
for i in range(1, 16):
    divisor = i * i
    
    # Se o termo for par, ele subtrai. Se for ímpar, ele soma.
    if i % 2 == 0:
        soma_serie = soma_serie - (i / divisor)
    else:
        soma_serie = soma_serie + (i / divisor)

print(f"O resultado da série alternada até o 15º termo é: {soma_serie:.4f}")
# Fim