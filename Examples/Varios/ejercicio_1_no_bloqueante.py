import math
from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import DistanceSensor

robot = Robot() # Create robot object
timestep = 32   # timestep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0
tiempo_anterior = 0
tilesize = 0.06


#Create your objects here
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timestep)

# Cargo el controlador para el sensor de distancia
distance_sensor1 = robot.getDevice("distance sensor1")
distance_sensor1.enable(timestep)

# Cargo el controlador para el sensor de distancia
distance_sensor2 = robot.getDevice("distance sensor2")
distance_sensor2.enable(timestep)

# Cargo el controlador del GPS
gps = robot.getDevice("gps")
gps.enable(timestep)

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

robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

proximo_estado=0

while robot.step(timestep) != -1:

    # Primera rotacion
    if proximo_estado == 0:
       print(angulo_actual)
       if rotar(90):
           print("Estado 1 concluido. Paso al siguiente estado")
           proximo_estado=1

    elif proximo_estado == 1:
        # 1er tramo hasta la pared
        if(distance_sensor1.getValue() > 0.05):
           avanzar(1.0)
        else:
            proximo_estado=2

    elif proximo_estado == 2:
        # Segunda rotacion
        if rotar(180):
            print("Segunda rotacion concluida. Paso al estado 3.")
            proximo_estado=3

    elif(proximo_estado == 3):
        # 2do tramo avanzo hasta la pared
        if(distance_sensor1.getValue() > 0.05):
            avanzar(1)
        else:
            proximo_estado=4

    elif proximo_estado == 4:
    # Tercera rotacion
        if rotar(90):
            print("Tercera rotacion concluida. Paso al estado 4.")
            proximo_estado=5

    # Ultimo tramo hasta la posicion x1
    elif proximo_estado == 5:
        x = gps.getValues()[0]/tilesize - startX
        y = gps.getValues()[2]/tilesize - startY
        if x < 6.0 :
           print("Imprimo la posicion actual x:",round(x,1),"y:",round(y,1))
           avanzar(1)
        else:
           proximo_estado = 6
    else:
        avanzar(0)
        print("Mision cumplida")



