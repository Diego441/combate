# combate.py

from personaje import Personaje
import random

class Combate:
    def __init__(self, jugador):
        self.jugador = jugador
        self.enemigo = self.crear_enemigo()
        # Aquí podrías añadir más atributos como recompensas, reglas especiales, etc.

    def crear_enemigo(self):
        # Esta función ahora es un método de la clase Combate
        nombres_enemigos = ["Enemigo A", "Enemigo B", "Enemigo C"]
        vida_enemigo = random.randint(10, 30)
        damage_enemigo = random.randint(1, 5)
        nivel_enemigo = 1  # Ajusta el nivel del enemigo si es necesario
        
        # Crea una instancia de enemigo aleatorio
        enemigo = Personaje(nombre=random.choice(nombres_enemigos), vida=vida_enemigo, damage=damage_enemigo, nivel=nivel_enemigo)
        
        return enemigo



