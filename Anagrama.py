def Anagrama(PLB1, PLB2):
    descomp1 = []
    descomp2 = []

    verdadero_Falso = True

    for i in PLB1:
        descomp1.append(i)

    for e in PLB2:
        descomp2.append(e)


    descomp1.sort()
    descomp2.sort()


    if descomp1 == descomp2:
        print('Es un Anagrama')
        verdadero_Falso = True
        return verdadero_Falso
    else:
        print('No es un Anagrama')
        verdadero_Falso = False
        print(verdadero_Falso)

pal1 = str(input('Ingresa una palabra: ')).lower()
pal2 = str(input('Ingresa otra palabra: ')).lower()

if pal1 == pal2:
    print('La palabras introducidas son iguales, No es un Anagrama')
else:
    Anagrama(pal1, pal2)