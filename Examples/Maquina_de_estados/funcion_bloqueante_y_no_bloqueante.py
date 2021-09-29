#!/bin/python
import time


contador = 0

def tarea():
    global contador
    print(contador)
    contador+=1
    time.sleep(0.1)

def bloqueante():
    global contador
    while (contador < 10):
        tarea()   # increamento el contador

def no_bloqueante():
    global contador
    if (contador < 10):
        tarea()  # incremento el contador
        return False
    else:
        return True


# Funcion no bloqueante
print("hola")
while True:
    if ( no_bloqueante() == True):
        print("mundo")

    if(contador >= 10):
        break


#Reinicio contador para evaluar el segundo caso
contador = 0

# Funcion bloqueante
print("hola")
while True:
    bloqueante()
    if(contador >= 10):
      print("mundo")
      break


