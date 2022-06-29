import os
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "BONILLA"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")


@app.route("/", methods=["GET"])
def index():
    """
   Crea la página de índice con todos sus atributos.

        Parámetros
        ----------
        title: título de la imagen

        Devoluciones
        -------
        La página de índice renderizada
    """
    # Crea la imagen de entrada
    title = "Create the input image"
    return render_template("/layouts/index.html", title=title)

"""
Se esta ejecutando el modulo de forma independiente y podemos 
realizar las acciones apropiadas correspondientes
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)