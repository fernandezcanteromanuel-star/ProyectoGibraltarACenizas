# Generamos unas coordenadas x, y
from math import sqrt

class Punto:
    #Definimos las coordenadas de nuestro plano con funciones que nos permitan
    #hacer las operaciones necesarias
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #Función para medir distancias entre puntos
    def distancia(self, p2):
        dist = sqrt((self.x - p2.x)**2+(self.y-p2.y)**2)
        return dist




