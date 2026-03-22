# Declarar as variáveis
h1 = 0
m1 = 0
h2 = 0
m2 = 0
total_minutos = 0

# Inicio 
h1 = int(input("Hora de início: "))
m1 = int(input("Minuto de início: "))
h2 = int(input("Hora de término: "))
m2 = int(input("Minuto de término: "))

inicio = (h1 * 60) + m1
fim = (h2 * 60) + m2

if fim < inicio:
    total_minutos = (1440 - inicio) + fim
else:
    total_minutos = fim - inicio

h_res = total_minutos // 60
m_res = total_minutos % 60

print(f"Duração do jogo: {h_res} horas e {m_res} minutos.")
# Fim