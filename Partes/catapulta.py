# Definimos nuestra catapulta de forma simple
import math
from random import random


class Catapulta:
    def __init__(self, peso, altura, masa_brazo,
                angulo_lanzamiento, precision):

        self.peso = peso
        self.altura = altura
        self.masa_brazo = masa_brazo
        self.angulo_lanzamiento = angulo_lanzamiento
        self.precision = precision

    def disparar(self):
        if 0 <= self.precision <= 1:
            if self.precision > random():
                return "Casa inglesa destruida"
            else:
                return "El proyectil no impactó"
        else:
            raise ValueError("La precisión solo está definida de 0 a 1")
        
    def mostrar_aciertos(self):
        

#Definimos catapulta para una prueba:
Catapulta1 = Catapulta(40, 5, 10, 45, 0.7)

#Formamos un while para hacer un número de disparos

i = int(input('Número de disparos que se quieren hacer: '))
n = 1

while n <= i:
    print(Catapulta1.mostrar_aciertos())
    n += 1