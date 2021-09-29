#!/bin/python
import time

estado = "Inicial"

contador = 0

while True:
    # Valido si estoy en el estado inicial
    if estado == "Inicial":
        # Tareas que realizo en el estado inicial
        print("Estado inicial Contador:", contador)
        if ( contador == 1):
            print("Hola")
            estado = "primero"

    # Valido si estoy en el estado primero
    elif estado == "primero":
        # Tareas que realizo en el estado "primero"
        print("En primero Contador:", contador)
        if ( contador == 3 ):
            print("Mundo")
            estado = "segundo"

    # Valido si estoy en el estado "segundo"
    elif estado == "segundo":
        # Tareas que realizo en el estado "segundo"
        print("En segundo Contador:", contador)
        if ( contador == 5 ):
            print("Termine. Salgo del While")
            break
    else:
        print("Estado no definido")

    contador+=1
    time.sleep(2)

print("Programa terminado")






