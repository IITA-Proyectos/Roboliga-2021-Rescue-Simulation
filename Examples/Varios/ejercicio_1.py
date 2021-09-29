import math
from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import DistanceSensor

robot = Robot() # Create robot object
timestep = 32   # timestep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0
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
    tiempo_anterior = 0

    #  iniciar_rotacion
    girar(0.5)  
    # Mientras no llego al angulo solicitado sigo girando  
    while (abs(angulo - angulo_actual) > 1):
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
        robot.step(timestep) 
    print("Rotacion finalizada, angulo actual:", angulo_actual) 
    return True


# Inicializacion del sistema

robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

while robot.step(timestep) != -1:

    # Primera rotacion
    rotar(90)
    print("Rotacion de 90 terminada, me detengo")
    avanzar(0)

    # 1er tramo hasta la pared
    print("Avanzo hasta la pared")
    while(distance_sensor1.getValue() > 0.05):
       avanzar(1.0)
       robot.step(timestep)

    # Segunda rotacion
    rotar(180)

    # 2do tramo avanzo hasta la pared
    while(distance_sensor1.getValue() > 0.1):
        avanzar(1)
        robot.step(timestep)
    
    # Tercera rotacion        
    rotar(90)
    
    # Ultimo tramo hasta la posicion x1
    print("Rotacion de 90 terminada, me detengo")
    x = gps.getValues()[0]/tilesize - startX
    y = gps.getValues()[2]/tilesize - startY
    while x < 6.0 :
        x = gps.getValues()[0]/tilesize - startX
        y = gps.getValues()[2]/tilesize - startY
        print("Imprimo la posicion actual x:",round(x,1),"y:",round(y,1))
        avanzar(1)
        robot.step(timestep)
    
    avanzar(0)
    print("Mision cumplida")
    break
    
    
    
