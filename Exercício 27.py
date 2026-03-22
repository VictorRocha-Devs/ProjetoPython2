# Declarar as variáveis
voltas = 0
extensao_metros = 0.0
tempo_minutos = 0.0
distancia_total_km = 0.0
tempo_horas = 0.0
velocidade_media = 0.0

# Inicio 
voltas = int(input("Digite o número de voltas: "))
extensao_metros = float(input("Digite a extensão do circuito (metros): "))
tempo_minutos = float(input("Digite o tempo de duração (minutos): "))

# Cálculo da distância total convertendo metros para km
distancia_total_km = (voltas * extensao_metros) / 1000

# Cálculo do tempo convertendo minutos para horas
tempo_horas = tempo_minutos / 60

# Cálculo da velocidade média
velocidade_media = distancia_total_km / tempo_horas

print(f"A velocidade média foi de: {velocidade_media:.2f} km/h")
# Fim