from controller import Robot, DistanceSensor

robot = Robot()

timestep = 32

# Cargo el controlador para el sensor de distancia
distance_sensor1 = robot.getDevice("distance sensor1")
distance_sensor1.enable(timestep)

# Cargo el controlador para el sensor de distancia
distance_sensor2 = robot.getDevice("distance sensor2")
distance_sensor2.enable(timestep)

while robot.step(timestep) != -1:

    # Obtengo el valor del sensor de distancia
    distance1 = distance_sensor1.getValue()
    # Muestro el valor de distancia por consola
    print("Distance hacia adelante 1: " + str(distance1))

    # Obtengo el valor del sensor de distancia
    distance2 = distance_sensor2.getValue()
    # Muestro el valor de distancia por consola
    print("Distance hacia la derecha 2: " + str(distance2))