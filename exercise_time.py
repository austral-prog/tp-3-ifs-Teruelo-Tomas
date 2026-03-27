def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas_completas = total_segundos // (60 ** 2)
    minutos_completos = total_segundos % (60 ** 2) // 60
    segundos_restantes = total_segundos % 60

    print(horas_completas)
    print(minutos_completos)
    print(segundos_restantes)
time()