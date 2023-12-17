# rutas.py

# Define funciones relacionadas con las rutas del juego
from app import app, jugador
import random  # Importa random para la generación de enemigos aleatorios

# Define el mapa de rutas
mapa = {
    1: ["Combate 1"],
    2: ["Combate 2", "Combate 3"],
    3: ["Combate 4", "Combate 5"],
    # Agrega más niveles y combates aquí
}

# Función para avanzar al siguiente nivel al ganar un combate
def avanzar_nivel():
    nivel_actual = jugador.nivel
    if nivel_actual in mapa:
        rutas_nivel_actual = mapa[nivel_actual]
        # Agregar las nuevas rutas al jugador
        jugador.rutas_desbloqueadas.extend(rutas_nivel_actual)
        # Avanzar al siguiente nivel
        jugador.nivel += 1


