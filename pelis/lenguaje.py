from . import db
from flask import Blueprint, render_template

bp = Blueprint('lenguaje', __name__,url_prefix='/lenguaje')

@bp.route('/')
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