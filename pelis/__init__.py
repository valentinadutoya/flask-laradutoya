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


@app.route('/actor')
def Actor():
    consulta = """
        SELECT first_name, last_name FROM actor
        ORDER BY last_name, first_name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_Actor = res.fetchall()
    pagina = render_template('Actor.html', actores=lista_Actor)

    return pagina


@app.route('/lenguaje')
def lenguaje():
    consulta = """
        SELECT name FROM language 
        ORDER BY name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    pagina = render_template('lenguaje.html', lenguajes=lista_lenguaje) 

    return pagina