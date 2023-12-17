# app.py

from flask import Flask, render_template
from combate import Combate
import personaje
import rutas
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///savedata.db'
db = SQLAlchemy(app)

jugador = personaje.Personaje(nombre="Jugador", vida=20, damage=10, nivel=1)
nuevo_mapa = rutas.Mapa(max_fases=10)

# Ruta para la pantalla de inicio (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la pantalla del mapa (mapa.html)
@app.route('/mapa')
def mapa():
    mapa = rutas.Mapa(max_fases=10)
    # Obtener el estado actualizado de los combates
    estado_combates = nuevo_mapa.obtener_estado_combates()
    # Pasar el estado de los combates al template
    return render_template('mapa.html', mapa_combates=estado_combates, fases_completadas=nuevo_mapa.fases_completadas)

# Ruta para la pantalla del combate (combate.html)
@app.route('/combate')
def combate():
    # Crear una instancia de Combate con el jugador y un enemigo generado
    instancia_combate = Combate(jugador=jugador)
    return render_template('combate.html', jugador=instancia_combate.jugador, enemigo=instancia_combate.enemigo)

@app.route('/victoria')
def victoria():
    # Obtener la fase actual desde la instancia de Mapa
    fase_actual = nuevo_mapa.fase_actual

    # Desbloquear la siguiente fase
    nuevo_mapa.desbloquear_siguiente_fase(fase_actual)

    # Renderizar la plantilla de victoria
    return render_template('victoria.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

