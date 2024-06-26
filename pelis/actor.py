from . import db
from flask import Blueprint, render_template

bp = Blueprint('actor', __name__,url_prefix='/actor')

@bp.route('/')
def Actor():
    consulta = """
        SELECT first_name, last_name, actor_id  FROM actor
        ORDER BY last_name, first_name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_Actor = res.fetchall()
    pagina = render_template('Actor.html', actores=lista_Actor)

    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
            con=db.get_db()
            consulta = """
            SELECT a.first_name,a.last_name, a.actor_id FROM actor a 
            WHERE a.actor_id = ?
            """

            consulta2 = """
            SELECT f.title, f.film_id, fa.actor_id  
            FROM film_actor fa 
            JOIN film f ON fa.film_id = f.film_id
            WHERE fa.actor_id = ?
            """

            resultado= con.execute(consulta,(id,))   
            actor = resultado.fetchone()
            
            resultado= con.execute(consulta2,(id,))   
            lista_pelis = resultado.fetchall()

            
            pagina = render_template('detalleActor.html', act=actor, pelis =lista_pelis)

            return pagina      