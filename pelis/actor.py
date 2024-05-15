from . import db
from flask import Blueprint, render_template

bp = Blueprint('actor', __name__,url_prefix='/actor')

@bp.route('/')
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
