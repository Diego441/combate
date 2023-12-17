# app.py

from flask import Flask, render_template
from personaje import Personaje
from combate import crear_enemigo

app = Flask(__name__)

jugador = Personaje(nombre="Jugador", vida=20, damage=10, nivel=1)

# Ruta para la pantalla de inicio (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la pantalla del mapa (mapa.html)
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

# Ruta para la pantalla del combate (combate.html)
@app.route('/combate')
def combate():
    enemigo = crear_enemigo()
    return render_template('combate.html', jugador=jugador, enemigo=enemigo)

if __name__ == '__main__':
    app.run(debug=True)

