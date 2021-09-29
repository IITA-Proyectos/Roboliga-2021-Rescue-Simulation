import math
from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import DistanceSensor

robot = Robot() # Create robot object
timestep = 32   # timestep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0
tiempo_anterior = 0

#Create your objects here
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timestep)

# Funciones basicas
def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

def rotar(angulo):
    global angulo_actual
    global tiempo_anterior

    #  iniciar_rotacion
    girar(0.5)
    # Mientras no llego al angulo solicitado sigo girando
    if (abs(angulo - angulo_actual) > 1):
        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        # tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep
        tiempo_transcurrido = timestep/1000
        # print(timestep,gyro.getValues()[1])
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
        return False
    else:
        print("Rotacion finalizada, angulo actual:", angulo_actual)
        return True


# Inicializacion del sistema

while robot.step(timestep) != -1:
    # Primera rotacion
    print(angulo_actual)
    if rotar(90):
        print("Mision cumplida")
        avanzar(0)
        break



