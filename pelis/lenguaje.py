from . import db
from flask import Blueprint, render_template

bp = Blueprint('lenguaje', __name__,url_prefix='/lenguaje')

@bp.route('/')
def lenguaje():
    consulta = """
        SELECT name,language_id FROM language 
        ORDER BY name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    pagina = render_template('lenguaje.html', lenguajes=lista_lenguaje) 

    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
            con=db.get_db()
            consulta = """
            SELECT name, language_id as idLeng FROM language
            WHERE language_id = ?
            """

            consulta2 = """
           SELECT f.title as pelicula, f.film_id FROM film f 
           JOIN language l on f.language_id = l.language_id
           WHERE l.language_id = ?
            """

            resultado= con.execute(consulta,(id,))   
            lenguaje = resultado.fetchone()
            
            resultado= con.execute(consulta2,(id,))   
            lista_pelis = resultado.fetchall()

            
            pagina = render_template('detalleLenguaje.html', leng=lenguaje, pelis=lista_pelis)

            return pagina      