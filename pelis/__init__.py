from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'



@app.route('/bb')
def bb():
    return 'laamm'


from . import actor
app.register_blueprint(actor.bp)

from . import lenguaje
app.register_blueprint(lenguaje.bp)

from . import Categoria 
app.register_blueprint(Categoria.bp)

from . import Peliculas 
app.register_blueprint(Peliculas.bp)