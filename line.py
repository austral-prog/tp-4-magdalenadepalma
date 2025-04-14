def line():
    import math
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {a}\nEl coeficiente B de su ecuación de la recta es: {b}\nEl coeficiente X1 de su ecuación de la recta es: {x1}\nEl coeficiente X2 de su ecuación de la recta es: {x2}\n")
    print(f"Para la siguiente ecuación:\n\tY = {a}X + {b}\n")
    print(f"Dados los siguientes puntos:")
    y1 = a * x1 + b
    y2 = a * x2 + b
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})\n")
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(f"La distancia entre ellos es: {distancia}")
