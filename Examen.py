#Programa que genera datos de un concurso. Participan pescadores de una serie de provincias(numero indeterminado de pescadores ).
#Presenta max 4 peces (los 4 mejores, puede que tenga mas o menos
#Datos = Nombres_Provincias, numero_pescadores, datos_pescador(nombre, provincia, 4 mejores capturas)
#a) Nombre y provincia del pescador con mayor peso total (suma de las 4 capturas)
#b) Nombre y provincia del pescador que ha pesacado el pes mas grande (Maximo de las capturas de todos los pescadores)
#c) Provincia con mas participantes, provincia con mas pescas y provincia cuyos pescadores han pescado mas peso
#d)
from sys import maxsize


def menu(opciones):
    for key,value in opciones.items():
        print(key,value)

def introducir_provincias(nombre_provincia):
    while True:
        nombre_provincia = str(input("Introduzca el nombre de la provincia (si desea parar pulse espacio): "))
        if nombre_provincia == " ":
            break
        else:
            provincias.append(nombre_provincia)

    nro_pescadores = int(input("¿Cuantos pescadores se han presentado? "))


    return [provincias], nro_pescadores

def introducir_datos(datos):
    for i in range(nro_pescadores):
        nombre_pescador = str(input("Introduzca el nombre del pescador: "))
        datos.append(nombre_pescador)
        provincia_pescador = str(input("Introduzca la provincia del pescador: "))
        if provincia_pescador not in provincias:
            break
        else:
            datos.append(provincia_pescador)
            while True:
                capturas = int(input("Introduzca el peso de las capturas del pescador(introduzca -1 para terminar): "))
                if capturas == -1:
                    break
                else:
                    datos.append(capturas)
    return datos

def pescador_mayor_peso(datos):
    peso_max = -maxsize -1
    total = 0
    ganador = []
    pesos = []
    for i in datos:
        total = 0
        for j in i[COLUMNA_PRIMERA_PESCA: COLUMNA_PESCAS_MAXIMA + 1]:
            total += j
            if total > peso_max:
                peso_max = total
                ganador = [i][0]
        pesos.append(total)


    return (max(pesos)), ganador

def pescador_mayor_pez(datos):
    pez_maximo = -maxsize - 1
    peces = []
    for i in datos:
        for j in i[COLUMNA_PRIMERA_PESCA: COLUMNA_PESCAS_MAXIMA + 1]:
            if j > pez_maximo:
                pez_maximo = j
                ganador = [i][0]
        peces.append(pez_maximo)

    return max(peces), ganador

def provincia_mas_pescadores(datos):
    """Cordoba = 0
    Malaga = 0
    Sevilla = 0
    Cadiz = 0

    for i in datos:
        for j in range(i[COLUMNA_PROVINCIA]):
            if j == "CORDOBA":
                Cordoba += 1
            elif j == "MALAGA":
                Malaga += 1
            elif j == "SEVILLA":
                Sevilla += 1
            elif j == "CADIZ":
                Cadiz += 1
            else:
                return False

    return max(Cordoba,Malaga,Sevilla,Cadiz)"""


if __name__ == "__main__":
    COLUMNA_PROVINCIA = 1
    #NRO_PESCADORES = 6
    COLUMNA_PESCAS_MAXIMA = 5
    COLUMNA_PRIMERA_PESCA = 2
    pescadores = []
    #provincias = ["CORDOBA", "MALAGA", "SEVILLA", "CADIZ"]
    opciones = {"1 =":"Introduzca las provincias y el numero de pescadores", "2 =":"Introducir datos", "3 =":"Pescador con mayor peso total",
                "4 =":"Pescador con el pez mas grande", "5 =":"Provincia con mas participantes", "6 =":"Provincia con mas pescas",
                "7 =":"Provincia con mas peso", "8 =":"Funcion", "9 =":"Salida"}
    datos = []
    #datos = [["Ivan", "CORDOBA", 4,5,7,7,2],["Josee", "SEVILLA", 7,2,10],["Raul", "CORDOBA", 8,12,30,23],["Juan", "MALAGA", 4]]
    provincias = []


    print("Concurso de pesca")
    print("-----------------")
    while True:
        menu(opciones)
        opcion_elegida = int(input("Introduzca la opcion que desea: "))

        match opcion_elegida:
            case 1:
                print(introducir_provincias(provincias))
            case 2:
                print(introducir_datos(datos))
            case 3:
                peso_max, ganador_1 = pescador_mayor_peso(datos)
                print(f"El peso total maximo es {peso_max}kg y pertenece a {ganador_1[0]}")
                print()
            case 4:
                pez, ganador_2= pescador_mayor_pez(datos)
                print(f"El pez mas grande pesa {pez}kg y pertenece a {ganador_2[0]}")
                print()
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("Saliendo del programa")
                break
            case _:
                print("No se ha introducido la opcion correcta")