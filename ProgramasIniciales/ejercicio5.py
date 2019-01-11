

salario = int(input("ingrese su sueldo mensual\n"))

if(salario>0 and salario<12450):
    print("19%")
elif(salario>12450 and salario<20200):
    print("24%")
elif(salario>20200 and salario<35200):
    print("30%")
elif(salario>35200 and salario<60000):
    print("37%")
elif(salario>60000):
    print("45%")


