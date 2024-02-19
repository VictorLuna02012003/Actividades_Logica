def correo(name, last_name, date):
    
    Lname = name[:2]
    Last = last_name[len(last_name)-2:]
    LDate = date[:2]

    return print(Lname + Last + LDate + "@gmail.com")

nombre = str(input('Ingresa tu nombre: ')).lower()
apellido = str(input('Ingresa tu apellido: ')).lower()
fecha = str(input('Ingresa tu fecha de nacimiento (DD/MM/YYYY): '))
correo(nombre, apellido, fecha)