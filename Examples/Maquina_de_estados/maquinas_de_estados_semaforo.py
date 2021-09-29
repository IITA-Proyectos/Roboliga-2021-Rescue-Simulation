#!/bin/python
import time

estado = "Inicial"

contador = 0

loop_ = 0

while True:
    # Valido si estoy en el estado inicial
    if estado == "Inicial":
        # Tareas que realizo en el estado inicial
        if ( contador == 1):
            print("Rojo")
            estado = "primero"

    # Valido si estoy en el estado primero
    elif estado == "primero":
        # Tareas que realizo en el estado "primero"
        if ( contador == 5):
            print("Amarillo")
            estado = "segundo"
            break
            # Cuantas veces pasa por el while hasta llegar aqui ??

    # Valido si estoy en el estado "segundo"
    elif estado == "segundo":
        # Tareas que realizo en el estado "segundo"
        if ( contador == 3):
            print("Verde")
            estado = "Inicial"
            contador = 0
            loop_ = loop_ + 1
            print ("Una vuelta pa..............................Nashe")
    else:
        print("Estado no definido")

    if (loop_ >= 4):
        break

    print(contador)
    contador+=1

    time.sleep(0.5)
