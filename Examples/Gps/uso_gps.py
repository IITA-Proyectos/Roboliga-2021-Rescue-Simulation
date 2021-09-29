from controller import Robot, GPS

timestep = 32
tilesize = 0.06

robot = Robot()

# Cargamos el GPS
gps = robot.getDevice("gps")
gps.enable(timestep)

destino_x = 0.0
destino_y = -4.0

#Create your objects here
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf')) 
ruedaDerecha.setPosition(float('inf'))


def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)


robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

while robot.step(timestep) != -1:

    x = round( gps.getValues()[0]/tilesize - startX, 1 )
    y = round( gps.getValues()[2]/tilesize - startY, 1 )

    if ( x == destino_x) and ( y == destino_y ):
        # Print si y == destino_y Y x == destino_x
        print ( "Llegue a destino.")
        avanzar(0)
        break
    else:
        avanzar(1.0)

    print("Imprimo la posicion actual x:", x,"y:", y)
