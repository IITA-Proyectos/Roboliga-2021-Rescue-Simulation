import math
from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import Robot, DistanceSensor, GPS
import numpy

# Crear una matriz de 5 x 7 rellena de 0
grilla = numpy.zeros((10,10))
print(grilla)


robot = Robot() # Create robot object
timeStep = 32   # timeStep = numero de milisegundos entre actualizaciones mundiales (del mundo)
tile_size = 0.12 # Tamaño de casilla
angulo_actual = 0

# Distance sensor initialization
distancia_sensor1 = robot.getDevice("distance sensor1")
distancia_sensor1.enable(timeStep)
maxima_distancia = 0.4


#Motor initialization
ruedaIzquierda = robot.getDevice("wheel1 motor")  
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Gyroscope initialization
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

#Gps initialization
gps = robot.getDevice("gps")
gps.enable(timeStep)
tilesize = 0.06
robot.step(timeStep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

# Create your functions here
def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

def rotar(angulo):
    global angulo_actual
    tiempo_anterior = 0
    #  iniciar_rotacion
    girar(1.2)  
    # Mientras no llego al angulo solicitado sigo girando  
    while (abs(angulo - angulo_actual) > 1):
        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep
        radsIntimestep = abs(gyro.getValues()[1]) * tiempo_transcurrido   # rad/seg * mseg * 1000
        degsIntimestep = radsIntimestep * 180 / math.pi
        print("rads: " + str(radsIntimestep) + " | degs: " + str(degsIntimestep))
        angulo_actual += degsIntimestep
        # Si se pasa de 360 grados se ajusta la rotacion empezando desde 0 grados
        angulo_actual = angulo_actual % 360
        # Si es mas bajo que 0 grados, le resta ese valor a 360
        if angulo_actual < 0:
            angulo_actual += 360
        tiempo_anterior = tiempo_actual
        robot.step(timeStep) 
    print("Rotacion finalizada.")
    angulo_actual = 0
    return True

def MovimientoPa(angle,x1,x2,y1,y2,vel):
    if rotar(angle):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((x1 <= x <= x2) and (y1 <= y <= y2)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(vel)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

# Code here
if robot.step(timeStep) != -1:
    # Calculo los valores de X e Y
    x = gps.getValues()[0]/tilesize
    y = gps.getValues()[2]/tilesize

    # Calculo la baldoza en la que estoy parado teniendo en cuenta el offset inicial
    tile_x = (x + numpy.sign(x) * tile_size/2) / tile_size
    tile_y = (y + numpy.sign(y) * tile_size/2) / tile_size
    # Imprimo el 1 en el lugar que corresponde teniendo en cuenta los valores anteriores
    grilla(tile_x,tile_y) = 1
    print(grilla)
    # print("(x,y):",x,y)
    print("Baldoza (x,y):", int(tile_x), int(tile_y))

    # Obtengo el valor del sensor de distancia
    distance1 = distancia_sensor1.getValue()/2

    # Muestro el valor de distancia por consola
    print("Distancia hacia adelante 1: " + str(distance1))

    # Calculo la distancia a la pared
    pared = round(distance1 / tile_size,1)
    print("Cantidad de baldozas hasta la pared:", pared)

    #GIRO 1: Gira para entrar al laberinto
    MovimientoPa(90,-5.2,-4.5,-1.0,0,6)
    print("Inicio etapa 1")
    
    #GIRO 2: Gira y avanza hasta el fondo del mapa
    MovimientoPa(87,-5.2,-4.5,2.8,3.3,7)
    print("Inicio etapa 2")

    #GIRO 3: Gira y avanza hasta la zona del pozo
    MovimientoPa(270,5.2,4.7,2.8,3.3,6)
    print("Inicio etapa 3")

    #GIRO 4: Gira y avanza un poco, subiendo (que en realidad es bajando) por y hasta que llega a la última curva
    MovimientoPa(270,5.2,4.7,0.8,1.3,6)
    print("Inicio etapa 4")

    #GIRO 5: Gira y avanza a la izquierda para llegar al último tramo
    MovimientoPa(270,3.2,2.7,0.8,1.3,6)
    print("Inicio etapa 5")

    #GIRO 6: Gira y avanza hacia arriba por "y" para acomodarse en el último giro al pozo
    MovimientoPa(90,2.7,3.2,-0.8,-1.10,6)
    print("Inicio etapa 6")

    #GIRO 7: Llega al pozo. Gira y avanza, luego cae.
    MovimientoPa(90,2.7,4.2,-2.8,-1.3,6)
    print("Inicio etapa 7")