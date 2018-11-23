contrasennaValida = False
contrasennaMayuscula = False
contrasennaMinuscula = False
contrasennaAlfa = False
contrasennaSpace = False
contrasennaNumeric = False

while not contrasennaValida:
    contrasenna = input("Introduce contrasenna a validar")
    if len(contrasenna) > 12:
        for n in contrasenna:
            if n.islower():
                contrasennaMinuscula = True
            if n.isupper():
                contrasennaMayuscula = True
            if n.isspace():
                contrasennaSpace = True
            if not n.isalpha():
                if not n.isnumeric():
                    contrasennaAlfa = True
            if n.isnumeric():
                contrasennaNumeric = True
    if contrasennaMayuscula and contrasennaMinuscula and not contrasennaSpace and contrasennaAlfa and contrasennaNumeric:
        contrasennaValida = True
if contrasennaValida:
    print("Contraseña valida")
    SystemExit(0)