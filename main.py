import math


def calculo():
    # Entrada de dados
    massa = float(input("Digite a massa da pessoa + equipamento (kg): "))
    gravidade = 9.81

    # Cálculo do peso
    peso = massa * gravidade

    # Constantes do ambiente e equipamento
    densidade_ar = 1.13
    area_parapente = 24  # Modelo EN-B (intermediário seguro)
    cd = 1.2             # Coeficiente de arrasto aproximado do parapente

    # Cálculo da velocidade terminal
    vt_ms = math.sqrt((2 * peso) / (densidade_ar * area_parapente * cd))
    vt_kh = vt_ms * 3.6

    # Exibição dos resultados
    print(f"Peso total da pessoa + equipamento: {peso:.2f} N")
    print(f"Velocidade terminal (m/s): {vt_ms:.2f} m/s")
    print(f"Velocidade terminal (km/h): {vt_kh:.2f} km/h")


# Executa a função
calculo()
