import math
from controller import Robot
from controller import Motor
from controller import PositionSensor

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

    #  iniciar_rotacion
    girar(0.5)
    # Mientras no llego al angulo solicitado sigo girando con una precision de 1 grado
    while ( abs(angulo - angulo_actual) > 1):

        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep

        radsIntimestep = abs(gyro.getValues()[1]) * tiempo_transcurrido   # rad/seg * mseg * 1000
        degsIntimestep = radsIntimestep * 180 / math.pi     # Convierto radianes a grados

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
    avanzar(0)
    return True


while robot.step(timeStep) != -1:
    if rotar(90):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
        break


