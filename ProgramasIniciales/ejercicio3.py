import math

sumatory = 0
numA = int(input("ingrese el numero inicial\n"))
numB = int(input("ingrese un numero final\n"))
if 0 <= numA <= numB:
    for i in range(numA, numB + 1):
        sumatory = sumatory + math.sqrt(i)
    print(sumatory)
else:
    print("Valor final menor al inicial")
