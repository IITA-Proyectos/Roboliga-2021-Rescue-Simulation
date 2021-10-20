import math
from controller import Robot
from controller import Motor
from controller import PositionSensor

robot = Robot() # Create robot object
timeStep = 32   # timeStep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0

#Motor initialization
ruedaIzquierda = robot.getDevice("wheel1 motor")  
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

#Gps
gps = robot.getDevice("gps")
gps.enable(timeStep)
tilesize = 0.06
robot.step(timeStep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

#Create your functions here
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

#Real Code
while robot.step(timeStep) != -1:
    x = gps.getValues()[0]/tilesize
    y = gps.getValues()[2]/tilesize
#Falta poner que avanze hasta el giro
#GIRO 1: Gira para entrar al laberinto
    if rotar(90):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((-5.2 <= x <= -4.5) and (y <= -1.0)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 2: Gira y avanza hasta el fondo del mapa
    if rotar(87):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((-5.2 <= x <= -4.5) and (2.8 <= y <= 3.3)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(7)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 3: Gira y avanza hasta la zona del pozo
    if rotar(270):#Gira 272 porque viene medio chueco
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((5.2 >= x >= 4.7) and (2.8 <= y <= 3.3)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 4: Gira y avanza un poco, subiendo (que en realidad es bajando) por y hasta que llega a la última curva
    if rotar(270): #Gira 270 porque ya viene acomodado
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((5.2 >= x >= 4.7) and (0.8 <= y <= 1.3)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 5: Gira y avanza a la izquierda para llegar al último tramo
    if rotar(270):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((3.2 >= x >= 2.7) and (0.8 <= y <= 1.3)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 6: Gira y avanza hacia arriba por "y" para acomodarse en el último giro al pozo
    if rotar(90):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((2.7 <= x >= 3.2) and (-0.8 <= y <= -1.10)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        #print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")

#GIRO 7: Llega al pozo. Gira y avanza, luego cae.
    print("Inicio etapa 7")
    if rotar(90):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
    while not ((2.7 <= x <= 4.2) and (-2.8 <= y <= -1.3)):
        x = gps.getValues()[0]/tilesize
        y = gps.getValues()[2]/tilesize
        print("Avanzamos, pa")
        avanzar(6)
        robot.step(timeStep) 
        print("x:",x, "y:",y)
    print("Llegamos pa")
    break