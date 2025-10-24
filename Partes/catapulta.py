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
        n = int(input("Número de veces que se quiere disparar: "))
        i = 0
        aciertos_fallos = {"Aciertos":0, "Fallos":0}
        while n > i:
            if Catapulta.disparar(self) == "Casa inglesa destruida":
                aciertos_fallos["Aciertos"] += 1
            else:
                aciertos_fallos["Fallos"] += 1
            i +=1
        return aciertos_fallos
        

#Definimos catapulta para una prueba:
Catapulta1 = Catapulta(40, 5, 10, 45, 0.7)
print(Catapulta1.mostrar_aciertos())



