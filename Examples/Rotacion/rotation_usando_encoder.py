from controller import Robot, GPS
from controller import Motor
from controller import PositionSensor

robot = Robot() # Create robot object
timeStep = 32   # timeStep = numero de milisegundos entre actualizaciones mundiales (del mundo)
noventaGrados = 2.3

#Create your objects here
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

encoderIzquierdo = ruedaIzquierda.getPositionSensor()    # Encoder initialization
encoderDerecho = ruedaDerecha.getPositionSensor()
encoderIzquierdo.enable(timeStep)
encoderDerecho.enable(timeStep)


#Create your code here
def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

while robot.step(timeStep) != -1:

    # Defino la posision que deberia llegar el encoder
    ruedaDerecha.setPosition(float(noventaGrados))
    # Configuro la velocidad de las ruedas
    girar(0.5)
    print("Diferencia del encoder:", encoderDerecho.getValue() - noventaGrados  )
    # Si se roto los 90 grados con un margen de 0.01 me detengo
    if(abs(encoderDerecho.getValue() - noventaGrados) < 0.01):
        print("Detenerse")
        avanzar(0)
        break

