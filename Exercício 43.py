# Declarar as variáveis
altura_ana = 1.10
altura_maria = 1.50
crescimento_ana = 0.03
crescimento_maria = 0.02
anos = 0

# Inicio 
while altura_ana <= altura_maria:
    altura_ana = altura_ana + crescimento_ana
    altura_maria = altura_maria + crescimento_maria
    anos = anos + 1

print(f"Serão necessários {anos} anos para Ana ser maior que Maria.")
print(f"Altura final - Ana: {altura_ana:.2f}m | Maria: {altura_maria:.2f}m")
# Fim