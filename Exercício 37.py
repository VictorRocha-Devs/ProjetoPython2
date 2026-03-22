# Declarar as variáveis
n = 0
anterior = 0
atual = 1
proximo = 0
i = 0

# Inicio 
# Loop de verificação: precisamos de pelo menos 2 termos para mostrar a sequência
while n < 2:
    n = int(input("Digite quantos termos da sequência de Fibonacci deseja ver (mínimo 2): "))
    if n < 2:
        print("Erro! Introduza um número igual ou maior que 2.")

print(f"Sequência de Fibonacci com {n} termos:")

# Mostra os dois primeiros termos que já conhecemos
print(anterior)
print(atual)

# O loop começa em 3 porque já mostrámos os 2 primeiros
for i in range(3, n + 1):
    proximo = anterior + atual
    print(proximo)
    
    # "Caminha" com as variáveis para o próximo cálculo
    anterior = atual
    atual = proximo

# Fim