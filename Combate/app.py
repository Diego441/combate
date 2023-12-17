# app.py

from flask import Flask, render_template
from combate import Combate
import personaje
import rutas

app = Flask(__name__)

jugador = personaje.Personaje(nombre="Jugador", vida=20, damage=10, nivel=1)

# Ruta para la pantalla de inicio (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la pantalla del mapa (mapa.html)
@app.route('/mapa')
def mapa():
    # Obtener el estado actualizado de los combates
    estado_combates = rutas.obtener_mapa_combates()
    # Pasar el estado de los combates al template
    return render_template('mapa.html', mapa_combates=estado_combates)

# Ruta para la pantalla del combate (combate.html)
@app.route('/combate')
def combate():
    # Crear una instancia de Combate con el jugador y un enemigo generado
    instancia_combate = Combate(jugador=jugador)
    return render_template('combate.html', jugador=instancia_combate.jugador, enemigo=instancia_combate.enemigo)

# Ruta para la pantalla de victoria (victoria.html)
@app.route('/victoria')
def victoria():
    # Puedes agregar lógica aquí si es necesario, como actualizar el estado del jugador
    return render_template('victoria.html')

if __name__ == '__main__':
    app.run(debug=True)

