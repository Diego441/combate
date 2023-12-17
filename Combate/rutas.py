# rutas.py

# Define funciones relacionadas con las rutas del juego
from app import jugador

# Estructura inicial del mapa de combates
mapa_combates = {
    'Fase 1': ['Combate A'],
    'Fase 2': ['Combate A', 'Combate B'],
    'Fase 3': ['Combate A', 'Combate B'],
    # ... y así sucesivamente hasta la fase que desees
}

# Registro de las fases completadas y los combates desbloqueados
fases_completadas = []
combates_desbloqueados = ['Fase 1']  # Inicialmente solo la Fase 1 está disponible

# Función para obtener el estado actual de los combates
def obtener_mapa_combates():
    estado_combates = {}
    for fase, combates in mapa_combates.items():
        estado_combates[fase] = {
            'combates': combates,
            'disponible': fase in combates_desbloqueados
        }
    return estado_combates

# Función para actualizar el mapa de combates después de una victoria
def desbloquear_siguiente_fase(fase_actual):
    # Marcar la fase actual como completada
    fases_completadas.append(fase_actual)
    
    # Desbloquear la siguiente fase
    indice_fase_actual = list(mapa_combates.keys()).index(fase_actual)
    if indice_fase_actual + 1 < len(mapa_combates):
        fase_siguiente = list(mapa_combates.keys())[indice_fase_actual + 1]
        combates_desbloqueados.append(fase_siguiente)


