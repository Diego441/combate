import random

class Mapa:
    def __init__(self, max_fases=10):
        num_fases = random.randint(5, max_fases)  # Número aleatorio de fases, con un máximo definido
        self.mapa_combates = {'Fase 1': ['Combate A']}  # Fase 1 siempre tiene un solo combate
        self.fase_actual = 'Fase 1'

        # Generar fases adicionales
        for i in range(2, num_fases + 1):
            self.mapa_combates[f'Fase {i}'] = ['Combate A', 'Combate B']  # Cada fase tiene dos combates

        self.fases_completadas = []
        self.combates_desbloqueados = ['Fase 1']

    def obtener_estado_combates(self):
        estado_combates = {}
        for fase, combates in self.mapa_combates.items():
            estado_combates[fase] = {
                'combates': combates,
                'disponible': fase in self.combates_desbloqueados
            }
        return estado_combates

    def desbloquear_siguiente_fase(self, fase_actual):
        self.fases_completadas.append(fase_actual)
        indice_fase_actual = list(self.mapa_combates.keys()).index(fase_actual)

        # Bloquear todas las fases, incluida la actual
        self.combates_desbloqueados = []

        # Desbloquear únicamente la siguiente fase
        if indice_fase_actual + 1 < len(self.mapa_combates):
            fase_siguiente = list(self.mapa_combates.keys())[indice_fase_actual + 1]
            self.combates_desbloqueados.append(fase_siguiente)
            self.fase_actual = fase_siguiente





