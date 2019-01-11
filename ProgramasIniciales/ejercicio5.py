

salario = int(input("ingrese su sueldo mensual\n"))
salarioFinal = 0

if(salario>0 and salario<12450):
    print("19%")
    salarioFinal = salario*19/100
    print(salarioFinal)
elif(salario>12450 and salario<20200):
    print("24%")
    salarioFinal = salario*24/100
    print(salarioFinal)
elif(salario>20200 and salario<35200):
    print("30%")
    salarioFinal = salario*30/100
    print(salarioFinal)
elif(salario>35200 and salario<60000):
    print("37%")
    salarioFinal = salario*37/100
    print(salarioFinal)
elif(salario>60000):
    print("45%")
    salarioFinal = salario*45/100
    print(salarioFinal)


