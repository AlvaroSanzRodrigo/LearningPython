import math

annoIntroducido = int(input("Introduzca un año \n"))

if (annoIntroducido/4).is_integer():
    print(annoIntroducido, " es bisiesto")
else:
    print(annoIntroducido, " no es bisiesto")
