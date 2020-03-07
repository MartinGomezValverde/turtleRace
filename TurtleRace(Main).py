import turtle
import random

class Circuit():
    turtles = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('green', 'blue', 'red', 'orange')
    
    def __init__(self, widht, height):
        
        self.__screen = turtle.Screen()
        self.__screen.setup(widht, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -(widht / 2) + 20
        self.__finishLine = +(widht / 2) - 20
        
        self.__Turtles()
        
    def __Turtles(self):        
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.color(self.__colorTurtle[i]) # Definimos su color 
            newTurtle.shape('turtle')
            newTurtle.penup() # No pintará el recorrido para llegar a 'start line'
            newTurtle.setpos(self.__startLine, self.__posStartY[i]) # Definimos su posición de salida con una separación standarizada.
            
            self.turtles.append(newTurtle)
            
    def compite(self):  
        existWinner = False
        while not existWinner:
            for turtle in self.turtles:
                progress = random.randint(1, 6) # Creamos el progreso random
                turtle.forward(progress)
                
                if turtle.position()[0] >= self.__finishLine:
                    existWinner = True
                    print("{} turtle has won!".format(turtle.color()[0]))
                    break
        
if __name__ == "__main__":
    circuit = Circuit(640, 480)
    circuit.compite()