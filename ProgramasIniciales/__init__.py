from random import randint

x = input("escriba el primer numero desde donde quieres que empieze el programa")
z = input("escriba hasta donde quiere jugar")

xint = int(x)
zint = int(z)

numSecreto = randint(xint,zint)
fallado = True
while fallado:
    nuestronum = input("mete el numero que creas correcto")
    nuestronumint = int(nuestronum)

    if nuestronumint == numSecreto:
        print("Correcto")
        fallado = False
    elif nuestronumint < numSecreto:
        print("el numero es mayor")
    else:
        print("el numero es menor")

SystemExit(0)