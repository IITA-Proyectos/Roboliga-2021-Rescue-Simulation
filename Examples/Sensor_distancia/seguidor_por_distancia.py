import math
from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import DistanceSensor

robot = Robot() #
timeStep = 32   # timeStep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0

# Cargo controlador de los motores
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

# Cargo el controlador para el sensor de distancia
distance_sensor1 = robot.getDevice("distance sensor1")
distance_sensor1.enable(timeStep)

# Cargo el controlador para el sensor de distancia
distance_sensor2 = robot.getDevice("distance sensor2")
distance_sensor2.enable(timeStep)


#Create your code here
def avanzar(vel):

    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

def rotar(angulo):
    global angulo_actual
    tiempo_anterior = 0
    angulo = angulo % 360

    #  iniciar_rotacion
    girar(0.5)
    # Mientras no llego al angulo solicitado sigo girando
    while (abs(angulo - angulo_actual) > 0.67):
        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep
        radsIntimestep = abs(gyro.getValues()[1]) * tiempo_transcurrido   # rad/seg * mseg * 1000
        degsIntimestep = radsIntimestep * 180 / math.pi
        # print("rads: " + str(radsIntimestep) + " | degs: " + str(degsIntimestep))
        angulo_actual += degsIntimestep

        # Si se pasa de 360 grados se ajusta la rotacion empezando desde 0 grados
        angulo_actual = angulo_actual % 360

        # Si es mas bajo que 0 grados, le resta ese valor a 360
        if angulo_actual < 0:
            angulo_actual += 360
        tiempo_anterior = tiempo_actual
        robot.step(timeStep)

    print("Rotacion finalizada, angulo actual:", angulo_actual)
    return True

init = True

while robot.step(timeStep) != -1:

    if init :
        rotar(90)
        init = False


    print("Distance hacia adelante 1: " + str(distance_sensor1.getValue()), "Distancia 2", str(distance_sensor2.getValue()))
    if distance_sensor1.getValue() < 0.05 :
        print("Angulo actual:", angulo_actual)
        print("Angulo actual + 90 :", angulo_actual + 90)
        rotar(angulo_actual+90)
        despues_de_rotar = True

    if despues_de_rotar:

    if distance_sensor1.getValue() < 0.05 :
        print("Angulo actual:", angulo_actual)
        print("Angulo actual + 90 :", angulo_actual + 90)
        rotar(angulo_actual+90)

    avanzar(1)





