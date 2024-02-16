import random 
def PPT(respuesta):
    maquina = random.randint(1,3)
    res_maquina = ["Piedra", "Papel", "Tijera"]

    if respuesta == 1:
        if maquina == 1:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Empate")
        elif maquina == 2:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Perdiste")
        elif maquina == 3:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Ganaste")
    elif respuesta == 2:
        if maquina == 1:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Ganaste")
        elif maquina == 2:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Empate")
        elif maquina == 3:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Perdiste")
    elif respuesta == 3:
        if maquina == 1:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Perdiste")
        elif maquina == 2:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Ganaste")
        elif maquina == 3:
            print(res_maquina[respuesta-1],"\t|\t", res_maquina[maquina-1])
            print("Empate")
    else:
        print("No se encuentra esa opcion")

print("1.- Piedra\t\t2.- Papel\t\t3.- Tijera")
opcion = int(input("Ingresa una opcion: "))
PPT(opcion)