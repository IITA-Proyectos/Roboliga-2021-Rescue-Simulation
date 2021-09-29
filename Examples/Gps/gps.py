from controller import Robot, GPS

timestep = 32
tilesize = 0.06

robot = Robot()

# Cargamos el GPS
gps = robot.getDevice("gps")
gps.enable(timestep)

robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

while robot.step(timestep) != -1:

    x = gps.getValues()[0]/tilesize - startX
    y = gps.getValues()[2]/tilesize - startY

    print("Imprimo la posicion actual x:",round(x,1),"y:",round(y,1))
