def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    impuesto_1 = (precio_base * 21) / 100
    subtotal = (precio_base + impuesto_1)
    propina = (subtotal * 10) / 100
    precio_final = subtotal + propina

    print(impuesto_1)
    print(subtotal)
    print(propina)
    print(precio_final)
price()